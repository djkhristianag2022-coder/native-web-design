#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guardián de {NOMBRE_STARTUP}: hook PreToolUse que hace cumplir reglas del Protocolo (CLAUDE.md §5).

Reglas:
  R1  auditor-red-team solo escribe en auditorias/.
  R2  Nadie más escribe en auditorias/, salvo appsec (*-dictamen-appsec.md) y
      pentester-autorizado (*-dictamen-pentest.md). Incluye al Chief of Staff (sesión principal).
  R3  Ningún agente ni la sesión principal puede marcar una autorización de pentest como
      FIRMADA o APROBADA: esos campos los escribe solo el fundador, a mano.
  R4  pentester-autorizado: herramientas de red en Bash y WebFetch solo hacia hosts listados en
      el bloque `autorizacion-maquina` de una autorización FIRMADA + APROBADA y dentro de su ventana.

  WebFetch de solo lectura a fuentes de referencia (OWASP, NVD, MITRE, FIRST, PortSwigger) está permitido.

Es una red de seguridad, no una garantía: no detecta toda forma posible de tráfico de red.
Entrada: JSON del hook en stdin (campos tool_name, tool_input, cwd, agent_type).
Salida: JSON con permissionDecision "deny" o nada (deja seguir el flujo normal de permisos).
"""
import datetime as dt
import glob
import json
import os
import re
import sys

AUDITOR = "auditor-red-team"
PENTESTER = "pentester-autorizado"
ESCRITURA = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
HERRAMIENTAS_RED = r"\b(curl|wget|nmap|masscan|nikto|sqlmap|ffuf|gobuster|dirb|dirsearch|wfuzz|nuclei|httpx|hydra|zap|zap-cli|burp|nc|ncat|netcat|testssl(\.sh)?|sslscan|whatweb|wpscan|feroxbuster|amass|subfinder|dnsx|openssl\s+s_client)\b"
REFERENCIA = {"owasp.org", "cheatsheetseries.owasp.org", "nvd.nist.gov", "cve.org", "www.cve.org", "cwe.mitre.org",
              "attack.mitre.org", "first.org", "www.first.org", "portswigger.net", "csrc.nist.gov"}
# Escritura dirigida a una ruta: redirección, o comando de escritura con la ruta como argumento
# (en el mismo segmento del pipeline). Los textos que solo mencionan la ruta no cuentan.
def bash_escribe_en(cmd, ruta_re):
    redireccion = rf">>?\s*['\"]?[^\s;&|]*{ruta_re}"
    comando = rf"\b(tee|mv|cp|rm|truncate|dd|install|rsync|ln|touch|chmod)\b[^;&|\n]*{ruta_re}|\bsed\b[^;&|\n]*\s-i[^;&|\n]*{ruta_re}"
    return re.search(redireccion, cmd) or re.search(comando, cmd)


def denegar(motivo):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": f"[guardián {{NOMBRE_STARTUP}}] {motivo}",
    }}, ensure_ascii=False))
    sys.exit(0)


def relativa(ruta, raiz):
    if not ruta:
        return ""
    absoluta = os.path.normpath(ruta if os.path.isabs(ruta) else os.path.join(raiz, ruta))
    return os.path.relpath(absoluta, raiz)


def en_auditorias(rel):
    return rel == "auditorias" or rel.startswith("auditorias" + os.sep)


def puede_escribir_auditoria(agente, rel):
    if agente == AUDITOR:
        return True
    if agente == "appsec" and rel.endswith("-dictamen-appsec.md"):
        return True
    if agente == PENTESTER and rel.endswith("-dictamen-pentest.md"):
        return True
    return False


def contenido_escrito(ti):
    partes = [ti.get("content", ""), ti.get("new_string", ""), ti.get("new_source", "")]
    for e in ti.get("edits", []) or []:
        partes.append(e.get("new_string", ""))
    return "\n".join(p for p in partes if p)


def autorizaciones_vigentes(raiz):
    """Devuelve el conjunto de hosts autorizados ahora mismo."""
    hosts = set()
    ahora = dt.datetime.now(dt.timezone.utc)
    for ruta in glob.glob(os.path.join(raiz, "proyectos", "*", "seguridad", "autorizacion-pentest.md")):
        texto = open(ruta, encoding="utf-8").read()
        m = re.search(r"<!--\s*autorizacion-maquina(.*?)-->", texto, re.S)
        if not m:
            continue
        campos = dict(re.findall(r"^\s*([a-z_]+)\s*:\s*(.*?)\s*$", m.group(1), re.M))
        if campos.get("estado_cliente") != "FIRMADA" or campos.get("estado_fundador") != "APROBADA":
            continue
        try:
            ini = dt.datetime.fromisoformat(campos["ventana_inicio"])
            fin = dt.datetime.fromisoformat(campos["ventana_fin"])
        except (KeyError, ValueError):
            continue
        if ini.tzinfo is None or fin.tzinfo is None or not (ini <= ahora <= fin):
            continue
        for h in campos.get("activos", "").split(","):
            h = h.strip().lower()
            if h:
                hosts.add(h)
    return hosts


def hosts_en(texto):
    encontrados = set(h.lower() for h in re.findall(r"(?:https?|wss?|ftp)://([^/\s:'\"?#]+)", texto))
    encontrados |= set(h.lower() for h in re.findall(
        r"(?<![\w./-])((?:\d{1,3}\.){3}\d{1,3}|(?:[a-z0-9-]+\.)+[a-z]{2,})(?![\w-])", texto, re.I))
    return {h for h in encontrados if not re.search(r"\.(md|py|sh|json|txt|csv|ya?ml|html?|js|ts)$", h)}


def main():
    try:
        datos = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)
    herramienta = datos.get("tool_name", "")
    ti = datos.get("tool_input", {}) or {}
    agente = datos.get("agent_type") or "chief-of-staff"
    raiz = os.environ.get("CLAUDE_PROJECT_DIR") or datos.get("cwd") or os.getcwd()

    if herramienta in ESCRITURA:
        rel = relativa(ti.get("file_path") or ti.get("notebook_path", ""), raiz)
        if agente == AUDITOR and not en_auditorias(rel):
            denegar(f"R1: auditor-red-team solo escribe en auditorias/ (intento: {rel}).")
        if en_auditorias(rel) and not puede_escribir_auditoria(agente, rel):
            denegar(f"R2: {agente} no puede escribir en auditorias/ (independencia de la auditoría).")
        if rel.endswith("autorizacion-pentest.md"):
            c = contenido_escrito(ti)
            if re.search(r"estado_cliente\s*:\s*FIRMADA|estado_fundador\s*:\s*APROBADA", c):
                denegar("R3: los campos FIRMADA/APROBADA de la autorización de pentest solo los escribe el fundador a mano.")

    elif herramienta == "Bash":
        cmd = ti.get("command", "")
        if bash_escribe_en(cmd, r"auditorias/") and agente not in (AUDITOR, "appsec", PENTESTER):
            denegar(f"R2: {agente} no puede modificar auditorias/ desde la terminal.")
        if bash_escribe_en(cmd, r"autorizacion-pentest\.md"):
            denegar("R3: la autorización de pentest no se modifica desde la terminal.")
        if agente == PENTESTER and re.search(HERRAMIENTAS_RED, cmd):
            objetivos = hosts_en(cmd)
            permitidos = autorizaciones_vigentes(raiz)
            if not objetivos:
                denegar("R4: comando de red sin host identificable; declara el host explícito de un activo autorizado.")
            fuera = sorted(objetivos - permitidos)
            if fuera:
                denegar(f"R4: hosts fuera de una autorización FIRMADA+APROBADA y vigente: {', '.join(fuera)}.")

    elif herramienta == "WebFetch" and agente == PENTESTER:
        objetivos = hosts_en(ti.get("url", "")) - REFERENCIA
        fuera = sorted(objetivos - autorizaciones_vigentes(raiz))
        if fuera:
            denegar(f"R4: WebFetch hacia hosts no autorizados: {', '.join(fuera)}.")

    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye las dos distribuciones del equipo a partir de las fuentes del repositorio.

  plugin/                      Plugin de Claude Code / Cowork (subagentes, comandos, guardián)
  .claude-plugin/marketplace.json  Marketplace que publica el plugin desde este repo
  dist/equipo-web/ + .zip      Skill para el chat de claude.ai (sin subagentes ni hooks)

Fuentes: CLAUDE.md, .claude/agents/, .claude/commands/, plantillas/, config/, scripts/hooks/guardian.py.

Uso:
  python3 scripts/construir_distribucion.py             # construye
  python3 scripts/construir_distribucion.py --verificar # falla si lo construido no coincide con las fuentes
"""
import filecmp
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = "equipo-web"          # namespace: /equipo-web:fase, equipo-web:appsec
MARKETPLACE = "equipo-agentes"
SKILL_CHAT = "equipo-web"      # el nombre de la carpeta debe coincidir con el de la skill
VERSION = "1.0.0"


def leer(rel):
    with open(os.path.join(RAIZ, rel), encoding="utf-8") as f:
        return f.read()


def escribir(destino, rel, texto):
    ruta = os.path.join(destino, rel)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)


def copiar_dir(src_rel, destino, dst_rel):
    shutil.copytree(os.path.join(RAIZ, src_rel), os.path.join(destino, dst_rel), dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", ".gitkeep"))


def reemplazar(texto, viejo, nuevo):
    if viejo not in texto:
        raise SystemExit(f"Fuente cambió; no se encontró: {viejo[:70]!r}")
    return texto.replace(viejo, nuevo)


def listar(rel, ext=".md"):
    return sorted(f for f in os.listdir(os.path.join(RAIZ, rel)) if f.endswith(ext))


# ───────────────────────────── Plugin ─────────────────────────────

AVISO_COMANDO = (
    "> **Plugin `" + PLUGIN + "`.** Antes de empezar, carga la skill `" + PLUGIN + ":protocolo` con la "
    "herramienta Skill: contiene el protocolo del Chief of Staff (equivale a `CLAUDE.md`), la configuración "
    "y las plantillas. Los agentes se invocan con `subagent_type` = `" + PLUGIN + ":<slug>` "
    "(p. ej., `" + PLUGIN + ":auditor-red-team`).\n\n"
)

MODO_PLUGIN = f"""## Modo plugin (leer primero)

Estás usando el equipo como plugin `{PLUGIN}`, no desde su repositorio fuente. Diferencias:

1. **Inicializar el espacio de trabajo.** El directorio de trabajo es el proyecto del usuario. Si no contiene `config/empresa.md`, `config/mercados.md`, `config/stack-matriz.md`, `config/aprobaciones-permanentes.md` y `plantillas/`, cópialos desde `recursos/` en la carpeta base de esta skill (la ruta aparece al cargarla) **sin sobrescribir** archivos existentes. Desde ese momento, los archivos del proyecto son la fuente de verdad. Crea `proyectos/` y `auditorias/` si no existen.
2. **Agentes:** invócalos con la herramienta Agent y `subagent_type` = `{PLUGIN}:<slug>` (p. ej., `{PLUGIN}:estratega-negocio`).
3. **Comandos:** `/{PLUGIN}:nuevo-proyecto`, `/{PLUGIN}:fase`, `/{PLUGIN}:auditoria`, `/{PLUGIN}:auditoria-seguridad`, `/{PLUGIN}:reporte-cliente`, `/{PLUGIN}:naming`.
4. **Guardián:** el plugin instala el hook PreToolUse que hace cumplir la regla 11. Protege `auditorias/` y las autorizaciones de pentest del proyecto del usuario.
5. **No edites el plugin instalado:** se regenera desde el repositorio fuente.

---

"""


def protocolo_plugin():
    t = leer("CLAUDE.md")
    t = reemplazar(t, "si una tarea corresponde a un especialista, la delegas con la herramienta Agent usando su `slug` como `subagent_type`.",
                   f"si una tarea corresponde a un especialista, la delegas con la herramienta Agent usando `{PLUGIN}:<slug>` como `subagent_type`.")
    t = reemplazar(t, "`scripts/hooks/guardian.py` (hook PreToolUse en `.claude/settings.json`)",
                   "el guardián del plugin (`hooks/hooks.json` → `scripts/guardian.py`)")
    t = reemplazar(t, "Pruebas: `python3 scripts/hooks/test_guardian.py`. Cualquier cambio al guardián o a `.claude/settings.json` requiere aprobación del fundador.",
                   "Cualquier cambio al guardián requiere aprobación del fundador y se hace en el repositorio fuente.")
    t = re.sub(r"### 8\. Mantenimiento del sistema\n.*?(?=### 9\.)",
               "### 8. Mantenimiento del sistema\n\nEl plugin se genera desde su repositorio fuente con `scripts/construir_distribucion.py`. No edites la copia instalada.\n\n",
               t, flags=re.S)
    cabecera = f"""---
name: protocolo
description: Protocolo del Chief of Staff del equipo de 31 agentes (estrategia, marca, UX, ingeniería, crecimiento, legal y seguridad) para proyectos web de consultoría integral. Cárgalo antes de usar cualquier comando /{PLUGIN}:* y cuando el usuario quiera abrir, avanzar o auditar un proyecto web con el equipo.
---

"""
    return cabecera + MODO_PLUGIN + t


def comando_plugin(nombre):
    t = leer(f".claude/commands/{nombre}")
    fin = t.index("\n---\n", 4) + 5
    cuerpo = t[fin:]
    for viejo in ["según `CLAUDE.md` (sección Protocolo)", "según `CLAUDE.md`"]:
        cuerpo = cuerpo.replace(viejo, f"según el protocolo de la skill `{PLUGIN}:protocolo`")
    return t[:fin] + "\n" + AVISO_COMANDO + cuerpo.lstrip("\n")


def construir_plugin(destino):
    p = os.path.join(destino, "plugin")
    escribir(p, ".claude-plugin/plugin.json", json.dumps({
        "name": PLUGIN,
        "version": VERSION,
        "description": "Equipo de 31 agentes (1 Chief of Staff + 30 especialistas) para desarrollo web con consultoría integral: 7 fases con puertas, auditoría red team, seguridad (appsec, pentest autorizado, GRC), legal y privacidad en las Américas. Todo en español.",
        "author": {"name": "Fundador"},
        "keywords": ["agencia-web", "multiagente", "consultoria", "seguridad", "espanol"],
    }, ensure_ascii=False, indent=2) + "\n")
    copiar_dir(".claude/agents", p, "agents")
    for c in listar(".claude/commands"):
        escribir(p, f"commands/{c}", comando_plugin(c))
    escribir(p, "skills/protocolo/SKILL.md", protocolo_plugin())
    copiar_dir("config", p, "skills/protocolo/recursos/config")
    copiar_dir("plantillas", p, "skills/protocolo/recursos/plantillas")
    escribir(p, "scripts/guardian.py", leer("scripts/hooks/guardian.py"))
    hooks = json.loads(leer(".claude/settings.json"))["hooks"]
    for grupo in hooks["PreToolUse"]:
        for h in grupo["hooks"]:
            h["command"] = 'python3 "${CLAUDE_PLUGIN_ROOT}"/scripts/guardian.py'
    escribir(p, "hooks/hooks.json", json.dumps({"hooks": hooks}, indent=2) + "\n")
    escribir(p, "README.md", f"""# Plugin `{PLUGIN}`

Generado automáticamente por `scripts/construir_distribucion.py`. No lo edites a mano: edita las fuentes del repositorio y vuelve a construir.

## Instalar

En Claude Code (2.1.275 o posterior):

    /plugin install {PLUGIN} --marketplace djkhristianag2022-coder/native-web-design

Guía completa (Claude Code, Cowork y chat de claude.ai): `USO.md` en la raíz del repositorio.
""")
    escribir(destino, ".claude-plugin/marketplace.json", json.dumps({
        "name": MARKETPLACE,
        "owner": {"name": "Fundador"},
        "metadata": {"description": "Marketplace privado del equipo de agentes", "version": VERSION},
        "plugins": [{
            "name": PLUGIN,
            "source": "./plugin",
            "description": "Equipo de 31 agentes para proyectos web con consultoría integral (en español).",
            "version": VERSION,
        }],
    }, ensure_ascii=False, indent=2) + "\n")


# ───────────────────────────── Skill de chat ─────────────────────────────

SKILL_CHAT_MD = f"""---
name: {SKILL_CHAT}
description: Equipo de consultoría y desarrollo web de 31 roles (Chief of Staff y 30 especialistas en estrategia, marca, UX, ingeniería, crecimiento, legal y seguridad) que trabaja por fases 0-6 con puertas de aprobación del fundador. Úsala cuando el usuario quiera abrir un proyecto web nuevo, ejecutar una fase, auditar, preparar un reporte de cliente o hacer naming, o cuando mencione el equipo, el Chief of Staff o un agente por su nombre (p. ej., estratega-negocio, appsec).
---

# Equipo web — modo chat

Eres el **Chief of Staff** del equipo. Esta skill es la versión para el chat de claude.ai del sistema multiagente del repositorio fuente. Todo se trabaja en español.

## Archivos de referencia (en esta skill)

| Archivo | Para qué |
|---|---|
| `protocolo.md` | Protocolo completo del Chief of Staff (fases, puertas, reglas no negociables, niveles de aprobación, matriz de responsabilidades). **Léelo al empezar.** |
| `agentes/<slug>.md` | Definición de cada uno de los 30 especialistas. |
| `comandos/<nombre>.md` | Procedimiento de cada comando: `nuevo-proyecto`, `fase`, `auditoria`, `auditoria-seguridad`, `reporte-cliente`, `naming`. |
| `plantillas/` | Brief, ADR, handoff, memo de decisión, checklists de puerta 0-6, reporte mensual, autorización de pentest. |
| `config/` | `empresa.md` (valor de `{{NOMBRE_STARTUP}}`), `mercados.md`, `stack-matriz.md`, `aprobaciones-permanentes.md`. |

## Cómo operar en el chat

El chat no tiene subagentes ni hooks. Por eso:

1. **Roles por turnos.** Cuando una fase requiere a un especialista, lee `agentes/<slug>.md` y trabaja como ese rol hasta cerrar su entregable y su handoff. Encabeza cada bloque con el rol: `### [estratega-negocio]`. Termina un rol antes de empezar otro.
2. **Comandos en lenguaje natural.** Si el usuario dice "nuevo proyecto <cliente>", "fase 2 de <cliente>", "audita la fase 1", "reporte de <cliente> de 2026-12" o "ronda de naming", sigue el archivo correspondiente de `comandos/`.
3. **Estado del proyecto.** El chat no tiene repositorio. Mantén `brief.md`, `estado.md` y `registro-decisiones.md` como archivos (o artefactos) y recomienda al usuario guardarlos en un Proyecto de claude.ai dedicado al cliente, para retomarlos en otra conversación. Al retomar, pide o lee esos archivos antes de continuar.
4. **Entregables.** Si hay ejecución de código, crea los archivos con las rutas del protocolo (`proyectos/<cliente>/...`) y entrégalos. Si no, entrégalos como documentos en la conversación con su ruta como título.
5. **Auditoría con independencia limitada.** `auditor-red-team` corre aquí en el mismo contexto que produjo el trabajo. Haz la auditoría como una pasada separada y adversarial, sin defender el trabajo previo. Indica en el memo: "auditoría en modo chat (sin aislamiento)". Para las puertas 4 y 5, recomienda repetir la auditoría con el plugin en Claude Code, donde el auditor es un subagente aislado.
6. **Seguridad ofensiva: nunca en el chat.** No hay guardián técnico aquí. `pentester-autorizado` solo planifica y revisa reportes; las pruebas se ejecutan con el plugin en Claude Code, con autorización firmada.
7. **Memo único por puerta.** Cierra cada fase con un solo `memo-decision.md` de una página y espera aprobación explícita.

## Reglas que no cambian en el chat

- Cero datos, cifras, testimonios o reseñas inventados; lo no verificado se marca `SUPUESTO` y toda cifra externa lleva URL y fecha.
- Cero acciones externas sin aprobación del fundador (leer fuentes públicas es Nivel 0).
- Sin patrones oscuros. Ningún lanzamiento con hallazgos críticos o altos abiertos.
- Usa `{{NOMBRE_STARTUP}}` y resuélvelo con `config/empresa.md`.
"""


def construir_skill_chat(destino):
    s = os.path.join(destino, "dist", SKILL_CHAT)
    escribir(s, "SKILL.md", SKILL_CHAT_MD)
    escribir(s, "protocolo.md", leer("CLAUDE.md"))
    copiar_dir(".claude/agents", s, "agentes")
    copiar_dir(".claude/commands", s, "comandos")
    copiar_dir("plantillas", s, "plantillas")
    copiar_dir("config", s, "config")


def empaquetar_zip(destino):
    base = os.path.join(destino, "dist")
    zip_ruta = os.path.join(base, f"{SKILL_CHAT}.zip")
    with zipfile.ZipFile(zip_ruta, "w", zipfile.ZIP_DEFLATED) as z:
        for carpeta, _, archivos in sorted(os.walk(os.path.join(base, SKILL_CHAT))):
            for a in sorted(archivos):
                ruta = os.path.join(carpeta, a)
                info = zipfile.ZipInfo(os.path.relpath(ruta, base), date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                with open(ruta, "rb") as f:
                    z.writestr(info, f.read())


# ───────────────────────────── Principal ─────────────────────────────

def construir(destino):
    for rel in ["plugin", os.path.join("dist", SKILL_CHAT)]:
        shutil.rmtree(os.path.join(destino, rel), ignore_errors=True)
    construir_plugin(destino)
    construir_skill_chat(destino)
    empaquetar_zip(destino)


def comparar(a, b):
    difs = []
    for raiz_a, _, archivos in os.walk(a):
        for f in archivos:
            ra = os.path.join(raiz_a, f)
            rb = os.path.join(b, os.path.relpath(ra, a))
            if not os.path.exists(rb) or not filecmp.cmp(ra, rb, shallow=False):
                difs.append(os.path.relpath(ra, a))
    return difs


def main():
    if "--verificar" in sys.argv:
        tmp = tempfile.mkdtemp()
        construir(tmp)
        difs = []
        for rel in ["plugin", "dist", ".claude-plugin"]:
            difs += [os.path.join(rel, d) for d in comparar(os.path.join(tmp, rel), os.path.join(RAIZ, rel))]
            difs += [os.path.join(rel, d) + " (sobra)" for d in comparar(os.path.join(RAIZ, rel), os.path.join(tmp, rel))
                     if not d.endswith(".gitkeep")]
        shutil.rmtree(tmp)
        if difs:
            print("Distribución desactualizada; ejecuta scripts/construir_distribucion.py:\n  " + "\n  ".join(sorted(set(difs))))
            sys.exit(1)
        print("Distribución al día con las fuentes.")
        return
    construir(RAIZ)
    print(f"Plugin en plugin/, marketplace en .claude-plugin/, skill de chat en dist/{SKILL_CHAT}.zip")


if __name__ == "__main__":
    main()

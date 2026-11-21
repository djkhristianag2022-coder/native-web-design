#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida que cada .claude/agents/*.md tenga frontmatter correcto y las 8 secciones.

Uso: python3 scripts/validar_agentes.py   (código de salida 1 si hay errores)
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECCIONES = [
    "Identidad y nivel", "Misión en el equipo", "Estándares y cuerpos de conocimiento",
    "Entradas requeridas", "Entregables", "Definición de terminado",
    "Límites y escalamiento", "Formato de handoff",
]
CAMPOS = ["name", "description", "tools", "model"]
MODELOS = {"opus", "sonnet", "inherit"}
HERRAMIENTAS = {"Read", "Write", "Edit", "Bash", "Grep", "Glob", "WebSearch", "WebFetch"}
ESPERADOS = 30


def nombre_actual():
    t = open(os.path.join(RAIZ, "config", "empresa.md"), encoding="utf-8").read()
    m = re.search(r"\| `\{NOMBRE_STARTUP\}` \| ([^|]+?) \|", t)
    return m.group(1).strip() if m else None


def validar(ruta):
    errores = []
    texto = open(ruta, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return ["sin frontmatter YAML"]
    fm = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            k, v = linea.split(":", 1)
            fm[k.strip()] = v.strip()
    for c in CAMPOS:
        if not fm.get(c):
            errores.append(f"falta campo '{c}'")
    if set(fm) - set(CAMPOS):
        errores.append(f"campos extra: {sorted(set(fm) - set(CAMPOS))}")
    slug = os.path.basename(ruta)[:-3]
    if fm.get("name") != slug:
        errores.append(f"name '{fm.get('name')}' != archivo '{slug}'")
    if fm.get("model") not in MODELOS:
        errores.append(f"model inválido '{fm.get('model')}'")
    tools = [t.strip() for t in fm.get("tools", "").split(",")]
    malas = [t for t in tools if t not in HERRAMIENTAS]
    if malas:
        errores.append(f"herramientas desconocidas {malas}")
    cuerpo = texto[m.end():]
    encontradas = re.findall(r"^## (.+)$", cuerpo, re.M)
    if encontradas != SECCIONES:
        errores.append(f"secciones {encontradas} != esperadas")
    if "{NOMBRE_STARTUP}" not in cuerpo:
        errores.append("no referencia {NOMBRE_STARTUP}")
    nombre = nombre_actual()
    if nombre and nombre in texto:
        errores.append("nombre literal de la empresa (usar {NOMBRE_STARTUP})")
    return errores


def main():
    archivos = sorted(glob.glob(os.path.join(RAIZ, ".claude", "agents", "*.md")))
    total = 0
    for a in archivos:
        e = validar(a)
        total += len(e)
        print(f"{'OK ' if not e else 'ERR'} {os.path.basename(a)}" + ("" if not e else " → " + "; ".join(e)))
    if len(archivos) != ESPERADOS:
        print(f"ERR se esperaban {ESPERADOS} agentes, hay {len(archivos)}")
        total += 1
    print(f"\n{len(archivos)} agentes · {total} errores")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()

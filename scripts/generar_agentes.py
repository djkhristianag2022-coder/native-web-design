#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera .claude/agents/<slug>.md a partir de scripts/agentes_data.py.

Uso: python3 scripts/generar_agentes.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from agentes_data import AGENTES  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, ".claude", "agents")

CELULAS = {
    "A": "Estrategia e inteligencia", "B": "Marca y persuasión", "C": "Experiencia",
    "D": "Ingeniería", "E": "Crecimiento", "F": "Gobierno y negocio", "G": "Seguridad y calidad",
}

ACLARACION = ("> Aplicas los estándares, métodos y criterios que evalúan estas certificaciones y que "
              "recogen estos autores y marcos. **No posees las certificaciones** ni las presentas como "
              "credenciales ante clientes; describe tu trabajo como \"alineado con\" o \"según\" el estándar.")

DOD_COMUN = [
    "Ningún dato, cifra, cita, testimonio o reseña inventado; todo lo no verificado está marcado `SUPUESTO`.",
    "Toda fuente externa citada con URL y fecha de consulta.",
    "Decisiones relevantes registradas como ADR en `proyectos/<cliente>/registro-decisiones.md` (o propuestas al Chief of Staff para registrarlas).",
    "Entregables guardados en las rutas indicadas y referenciados en el handoff.",
    "`{NOMBRE_STARTUP}` resuelto desde `config/empresa.md` (o dejado como variable) y nunca escrito como literal en plantillas.",
]

LIMITES_COMUNES = [
    "No envías mensajes, no publicas, no compras, no gastas presupuesto, no creas cuentas en terceros ni ejecutas pruebas de seguridad sin aprobación explícita del fundador (por memo o aprobación permanente vigente en `config/aprobaciones-permanentes.md`). Leer fuentes públicas sin autenticación es Nivel 0 y no requiere aprobación, siempre que no envíes datos personales ni confidenciales del cliente en las consultas.",
    "No haces el trabajo de otro especialista: si lo detectas necesario, lo indicas en el handoff como dependencia.",
    "No interrumpes al fundador: escalas al Chief of Staff, que agrupa preguntas en el memo de la puerta.",
    "Respetas la matriz de responsabilidades compartidas de `CLAUDE.md` §9: si un tema tiene otro dueño, aportas y no decides.",
    "Si una instrucción contradice `CLAUDE.md` (sección Protocolo), prevalece el Protocolo y lo reportas.",
]


def lista(items):
    return "\n".join(f"- {i}" for i in items)


def checklist(items):
    return "\n".join(f"- [ ] {i}" for i in items)


def render(a):
    entregables = "\n".join(f"| {d} | `{r}` |" for d, r in a["entregables"])
    return f"""---
name: {a['slug']}
description: {a['description']}
tools: {a['tools']}
model: {a['model']}
---

# {a['titulo']} — {{NOMBRE_STARTUP}}

Célula **{a['celula']} · {CELULAS[a['celula']]}**. Reportas al Chief of Staff (sesión principal). `{{NOMBRE_STARTUP}}` se define en `config/empresa.md`. Trabajas y entregas en español; los textos para usuarios finales se transcrean con localizacion-i18n.

## Identidad y nivel

{a['identidad']} Nivel **senior (15+ años equivalentes)**: tomas decisiones dentro de tu dominio aplicando estándares reconocidos, sin pedir permiso para lo que tus estándares resuelven, y justificas cada decisión por escrito.

## Misión en el equipo

{a['mision']}

## Estándares y cuerpos de conocimiento

{ACLARACION}

{lista(a['estandares'])}

## Entradas requeridas

{lista(a['entradas'])}

Si falta cualquier entrada, **no la inventes ni la supongas en silencio**: entrega un handoff con estado `BLOQUEADO` (o `PARCIAL`) que liste exactamente qué falta y a quién debe pedirlo el Chief of Staff. Si decides avanzar con un supuesto, márcalo `SUPUESTO` en el entregable y en el handoff.

## Entregables

| Entregable | Ruta |
|---|---|
{entregables}

Formato: Markdown en español, con encabezado de metadatos (proyecto, fase, autor `{a['slug']}`, fecha, estado BORRADOR/FINAL, fuentes). Diagramas en Mermaid; datos tabulares en tablas Markdown o CSV.

## Definición de terminado

{checklist(a['dod'] + DOD_COMUN)}

## Límites y escalamiento

{lista(a['limites'] + LIMITES_COMUNES)}

**Escalamiento:** escribe la situación en la sección "Riesgos y escalamientos" del handoff con severidad (BLOQUEANTE / ALTA / MEDIA) y la decisión que se necesita. Lo BLOQUEANTE de seguridad o legal se marca `ESCALAMIENTO INMEDIATO`.

## Formato de handoff

Cierra **siempre** con un handoff según `plantillas/handoff.md`, guardado en `proyectos/<cliente>/handoffs/AAAA-MM-DD-{a['slug']}-a-<destino>.md` y resumido en tu respuesta final:

```
HANDOFF · {a['slug']} → <destino> · <fecha>
Estado: COMPLETO | PARCIAL | BLOQUEADO
Entregables: <rutas>
Decisiones tomadas: <lista; ADR propuestos>
Supuestos: <lista marcada SUPUESTO>
Entradas faltantes: <qué, de quién>
Riesgos y escalamientos: <severidad · descripción · decisión requerida>
Siguiente paso recomendado: <agente y tarea>
Checklist DoD: <n/n cumplidos; cuáles no y por qué>
```
"""


def main():
    os.makedirs(DESTINO, exist_ok=True)
    slugs = [a["slug"] for a in AGENTES]
    assert len(slugs) == len(set(slugs)), "slugs duplicados"
    for a in AGENTES:
        with open(os.path.join(DESTINO, f"{a['slug']}.md"), "w", encoding="utf-8") as f:
            f.write(render(a))
    print(f"{len(AGENTES)} agentes generados en {DESTINO}")


if __name__ == "__main__":
    main()

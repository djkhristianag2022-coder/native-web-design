# Plan de fase 0 — Diagnóstico · 00-startup

> Chief of Staff · 2026-11-21 · Modo **en seco** (ADR-002).

## Objetivo
Entender el mercado, las obligaciones legales y la viabilidad de {NOMBRE_STARTUP} en el continente americano con suficiente evidencia para decidir la estrategia (fase 1).

## Agentes, entregables y dependencias

| Orden | Agente | Entregable | Depende de |
|---|---|---|---|
| 1 (paralelo) | legal-privacidad | `mercados-aplicables.md` | brief |
| 1 (paralelo) | investigador-mercado | `mercado-tam-sam-som.md`, `competencia.md`, `tendencias.md`, `fuentes.md` | brief |
| 1 (paralelo) | investigador-ux | `personas.md`, `guia-entrevista.md`, `encuesta.md` | brief |
| 1 (paralelo) | estratega-negocio | `discovery.md` | brief |
| 2 | analista-financiero | `viabilidad.md`, `modelos/` | 1 |
| 2 | cuentas-ventas | `alcance-comercial.md` (BORRADOR) | 1 |
| 3 | Chief of Staff | `resumen-fase.md` | 2 |
| 4 | auditor-red-team | `auditorias/00-startup/fase-0-*.md` | 3 |
| 5 | Chief of Staff | `memo-decision.md` | 4 |

## Criterios de la puerta
Los de `plantillas/checklist-puerta-0.md` (9 específicos + 8 transversales).

## Restricción en seco
Sin WebSearch/WebFetch ni contacto externo. Cifras = `PENDIENTE DE INVESTIGACIÓN`. Normas citadas desde conocimiento interno = `NO VERIFICADO`.

---
description: Ejecuta una fase (0-6) completa de un proyecto hasta su puerta y memo de decisión.
argument-hint: <número-de-fase 0-6> <slug-cliente>
---

> **Plugin `equipo-web`.** Antes de empezar, carga la skill `equipo-web:protocolo` con la herramienta Skill: contiene el protocolo del Chief of Staff (equivale a `CLAUDE.md`), la configuración y las plantillas. Los agentes se invocan con `subagent_type` = `equipo-web:<slug>` (p. ej., `equipo-web:auditor-red-team`).

Actúa como Chief of Staff según el protocolo de la skill `equipo-web:protocolo`. Argumentos: **$ARGUMENTS** (primer argumento = número de fase, segundo = slug del cliente).

1. Verifica en `proyectos/<slug>/estado.md` que la puerta de la fase anterior esté **aprobada por el fundador** (salvo fase 0). Si no, detente e infórmalo.
2. Lee el brief, `registro-decisiones.md`, el `resumen-fase.md` y el memo aprobado de la fase anterior.
3. Toma de la tabla de fases del Protocolo los agentes de la fase solicitada (o el núcleo mínimo si el ADR-001 lo define así) y escribe `<carpeta-fase>/plan.md` con los criterios de `plantillas/checklist-puerta-<n>.md`.
4. Delega con la herramienta Agent; paraleliza lo independiente; pasa a cada agente rutas y handoffs previos.
5. Resuelve contradicciones entre entregables; si no se pueden resolver con estándares, llévalas al memo.
6. Integra en `<carpeta-fase>/resumen-fase.md` y registra ADRs.
7. Puerta:
   - `auditor-red-team` → `auditorias/<slug>/fase-<n>-dictamen.md`.
   - Si la fase es 4 o 5: además `appsec` → `fase-<n>-dictamen-appsec.md` y `pentester-autorizado` → `fase-<n>-dictamen-pentest.md`. El pentester solo actúa si existe `seguridad/autorizacion-pentest.md` firmada y aprobada; si no, su dictamen es BLOQUEADO y la puerta no puede aprobarse.
   - Fase 5: no se aprueba con hallazgos críticos o altos abiertos.
8. Redacta `<carpeta-fase>/memo-decision.md` (una página) y detente a esperar aprobación explícita.

Carpetas: 0 `00-diagnostico`, 1 `01-estrategia`, 2 `02-marca-contenido`, 3 `03-experiencia`, 4 `04-construccion`, 5 `05-lanzamiento`, 6 `06-crecimiento`.

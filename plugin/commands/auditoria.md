---
description: Solicita a auditor-red-team un dictamen independiente (pre-mortem, verificación de datos y checklist) de una fase.
argument-hint: <slug-cliente> <número-de-fase>
---

> **Plugin `equipo-web`.** Antes de empezar, carga la skill `equipo-web:protocolo` con la herramienta Skill: contiene el protocolo del Chief of Staff (equivale a `CLAUDE.md`), la configuración y las plantillas. Los agentes se invocan con `subagent_type` = `equipo-web:<slug>` (p. ej., `equipo-web:auditor-red-team`).

Como Chief of Staff, invoca al agente `auditor-red-team` para el proyecto y fase: **$ARGUMENTS**.

Pásale: ruta `proyectos/<slug>/`, carpeta de la fase, lista de entregables y handoffs, y `plantillas/checklist-puerta-<n>.md`.

Instrucciones para el auditor:
- Pre-mortem: "Es dentro de 12 meses y este proyecto fracasó; ¿por qué?" → `auditorias/<slug>/fase-<n>-premortem.md`.
- Verifica contra su fuente al menos el 30 % de las cifras externas, priorizando las que sostienen decisiones → `fase-<n>-verificacion-datos.md`.
- Busca activamente: datos inventados, testimonios/reseñas ficticias, patrones oscuros, supuestos no marcados, contradicciones entre agentes.
- Dictamen APROBADO / CON OBSERVACIONES / RECHAZADO con evidencia por ítem → `fase-<n>-dictamen.md`.

No modifiques el dictamen. Resume al fundador el veredicto y los bloqueantes, sin interpretar a favor del equipo.

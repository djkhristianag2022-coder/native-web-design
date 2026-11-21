---
description: Ejecuta la ronda de naming de {NOMBRE_STARTUP} (o de un cliente) y prepara el memo para elegir el nombre definitivo.
argument-hint: [slug-cliente — por defecto 00-startup]
---

> **Plugin `equipo-web`.** Antes de empezar, carga la skill `equipo-web:protocolo` con la herramienta Skill: contiene el protocolo del Chief of Staff (equivale a `CLAUDE.md`), la configuración y las plantillas. Los agentes se invocan con `subagent_type` = `equipo-web:<slug>` (p. ej., `equipo-web:auditor-red-team`).

Como Chief of Staff, ejecuta la ronda de naming para **$ARGUMENTS** (si no hay argumento, el proyecto es `00-startup`, es decir, {NOMBRE_STARTUP}). Dirige `estratega-marca`; colaboran `investigador-mercado`, `legal-privacidad` y `localizacion-i18n`.

1. `estratega-marca`: criterios de naming a partir de la plataforma de marca (si no existe, detente: el naming requiere al menos posicionamiento preliminar de fase 1), territorios, lista larga (≥ 40) → `02-marca-contenido/naming/lista-larga.md`.
2. `localizacion-i18n`: filtro lingüístico ES-LatAm/EN/PT-BR/FR-CA (pronunciación, connotaciones, jerga regional) → `naming/filtro-linguistico.md`.
3. `investigador-mercado`: conflictos con competidores y uso en el mercado; disponibilidad aparente de dominios y handles (solo consulta, **sin registrar nada**) → `naming/conflictos-disponibilidad.md`.
4. `legal-privacidad`: búsqueda preliminar en IMPI, USPTO, CIPO, INPI-BR (y EUIPO para fase 2), clases de Niza 35 y 42 → `naming/busqueda-marcas.md`. Indicar ⚖️ que se requiere opinión de registrabilidad de abogado de marcas.
5. `estratega-marca`: lista corta (3-5) con evaluación ponderada → `naming/lista-corta.md`.
6. `auditor-red-team`: dictamen del proceso → `auditorias/<slug>/naming-dictamen.md`.
7. Memo de una página → `02-marca-contenido/naming/memo-decision.md`: recomendación, opciones, riesgos, y acciones externas solicitadas (compra de dominios, solicitudes de marca) con costo.
8. **Solo tras aprobación explícita del fundador:** actualizar `config/empresa.md` (valor y estado DEFINITIVO) y registrar ADR. Ningún otro archivo se edita: todos usan `{NOMBRE_STARTUP}`.

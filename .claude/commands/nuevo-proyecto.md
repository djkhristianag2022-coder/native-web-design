---
description: Abre un proyecto nuevo, crea su estructura y ejecuta la fase 0 (Diagnóstico) hasta su puerta y memo de decisión.
argument-hint: <slug-cliente> [descripción breve]
---

Actúa como Chief of Staff según `CLAUDE.md` (sección Protocolo). Proyecto: **$ARGUMENTS**.

1. **Estructura.** Si `proyectos/<slug>/` no existe, créala según la sección 6 del Protocolo: `brief.md` (desde `plantillas/brief.md`), `estado.md`, `registro-decisiones.md` (desde `plantillas/registro-decisiones.md`), `handoffs/`, carpetas `00-diagnostico/` … `06-crecimiento/`, `seguridad/` y `auditorias/<slug>/`.
2. **Brief.** Completa el brief solo con lo que dio el fundador. Lo desconocido va como `DESCONOCIDO` y entra a "Preguntas abiertas". No inventes.
3. **Tamaño.** Decide si es proyecto pequeño (núcleo mínimo) o estándar y regístralo como ADR-001.
4. **Plan de fase 0.** Escribe `00-diagnostico/plan.md` con objetivo, agentes, entregables, dependencias y criterios tomados de `plantillas/checklist-puerta-0.md`.
5. **Delegación fase 0** (con la herramienta Agent, pasando ruta del proyecto y brief a cada uno):
   - En paralelo: `legal-privacidad` (mercados aplicables + verificación de vigencia), `investigador-mercado` (TAM/SAM/SOM, competencia, tendencias), `investigador-ux` (proto-personas, guías), `estratega-negocio` (discovery).
   - Después, con esos insumos: `analista-financiero` (viabilidad preliminar) y `cuentas-ventas` (alcance comercial en BORRADOR).
6. **Integrar** en `00-diagnostico/resumen-fase.md`; registrar ADRs; actualizar `estado.md`.
7. **Puerta.** Invoca `auditor-red-team` con la fase 0 → `auditorias/<slug>/fase-0-dictamen.md`. Si es RECHAZADO, vuelve al paso 5 solo con los agentes implicados.
8. **Memo.** Redacta `00-diagnostico/memo-decision.md` (una página, `plantillas/memo-decision.md`) con todas las preguntas de la fase agrupadas.
9. **Detente.** Muestra el memo al fundador y espera aprobación explícita. No ejecutes la fase 1.

Modo **en seco**: si el fundador pide "en seco", no ejecutes búsquedas web ni acciones externas; produce los entregables con la estructura, preguntas e hipótesis, marcando toda cifra como `PENDIENTE DE INVESTIGACIÓN`.

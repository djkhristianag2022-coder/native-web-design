# Checklist de puerta — Fase 4: Construcción

> Plantilla de {NOMBRE_STARTUP}. La aplica `auditor-red-team` (independiente) antes de que el Chief of Staff redacte el memo. Agentes de la fase: Célula D + appsec + qa-automatizacion.

**Proyecto:** `proyectos/<cliente>/` · **Fecha:** AAAA-MM-DD · **Auditor:** auditor-red-team

## Criterios específicos de la fase

| # | Criterio | Veredicto | Evidencia (ruta:línea o URL) |
|---|---|---|---|
| 1 | ADR de stack con matriz completa (≥ 3 opciones) y plan de salida. | ☐ Cumple ☐ No cumple ☐ N/A | |
| 2 | Build reproducible; CI con lint, pruebas, SAST, SCA y escaneo de secretos. | ☐ Cumple ☐ No cumple ☐ N/A | |
| 3 | Cero secretos en el repositorio (historial incluido). | ☐ Cumple ☐ No cumple ☐ N/A | |
| 4 | Presupuesto de rendimiento cumplido en laboratorio (CWV objetivo). | ☐ Cumple ☐ No cumple ☐ N/A | |
| 5 | Suite E2E en 3 motores de navegador, móvil/escritorio y 4 locales. | ☐ Cumple ☐ No cumple ☐ N/A | |
| 6 | Dictamen de appsec: sin hallazgos críticos/altos abiertos. | ☐ Cumple ☐ No cumple ☐ N/A | |
| 7 | Dictamen de pentester-autorizado (si hay autorización firmada) o constancia de pendiente para fase 5. | ☐ Cumple ☐ No cumple ☐ N/A | |
| 8 | Rollback y restauración de respaldo probados en staging. | ☐ Cumple ☐ No cumple ☐ N/A | |

## Criterios transversales (todas las fases)

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| T1 | Ningún dato, cifra, testimonio o reseña inventado; supuestos marcados | ☐ | |
| T2 | Muestra ≥ 30 % de cifras externas verificada contra su fuente | ☐ | |
| T3 | Todos los agentes entregaron handoff con `plantillas/handoff.md` | ☐ | |
| T4 | Decisiones relevantes registradas en `registro-decisiones.md` | ☐ | |
| T5 | Ninguna acción externa sin aprobación del fundador | ☐ | |
| T6 | Sin patrones oscuros en entregables | ☐ | |
| T7 | `{NOMBRE_STARTUP}` usado como variable; sin registros con nombre PROVISIONAL | ☐ | |
| T8 | Pre-mortem realizado (`auditorias/<cliente>/fase-4-premortem.md`) | ☐ | |

## Dictámenes requeridos
- [ ] Dictamen de `auditor-red-team` en `auditorias/<cliente>/fase-4-dictamen.md`.
- [ ] Dictamen de `appsec` en `auditorias/<cliente>/fase-4-dictamen-appsec.md`.
- [ ] Dictamen de `pentester-autorizado` en `auditorias/<cliente>/fase-4-dictamen-pentest.md` (sin autorización firmada → la puerta no puede ser APROBADA).

## Dictamen
☐ **APROBADO** · ☐ **CON OBSERVACIONES** (lista de observaciones no bloqueantes) · ☐ **RECHAZADO** (bloqueantes)

Bloqueantes:
Observaciones:

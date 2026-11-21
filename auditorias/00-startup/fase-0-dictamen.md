# Dictamen de puerta — Fase 0 · 00-startup

> **auditor-red-team** (simulado en seco) · 2026-11-21 · Independiente: no participó en la producción.

## Veredicto sustantivo: **RECHAZADO** (esperado en modo en seco)
## Veredicto del proceso: **VALIDADO**

## Checklist de puerta 0
| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Brief completo; preguntas abiertas con dueño | Cumple | `brief.md` §8 (6 preguntas) |
| 2 | Mercados aplicables con URL y fecha; vigencia verificada | **No cumple** | `mercados-aplicables.md`: todo NO VERIFICADO |
| 3 | TAM/SAM/SOM con fuentes | **No cumple** | `mercado-tam-sam-som.md`: solo método |
| 4 | ≥ 5 competidores por mercado prioritario | **No cumple** | `competencia.md`: solo tipología |
| 5 | Personas marcadas HIPÓTESIS | Cumple | `personas.md` |
| 6 | Discovery con problema, hipótesis y preguntas | Cumple | `discovery.md` |
| 7 | Viabilidad con escenarios y supuestos | **No cumple** | Modelo sin supuestos; se niega a calcular (correcto) |
| 8 | Alcance comercial en BORRADOR | Cumple | `alcance-comercial.md` |
| 9 | Sin acciones externas | Cumple | `estado.md` |
| T1-T8 | Transversales | Cumplen (T2 no aplica: 0 cifras) | `fase-0-verificacion-datos.md`, `fase-0-premortem.md` |

## Bloqueantes
1. Investigación real de mercado y competencia (criterios 3, 4).
2. Verificación de vigencia legal en mercados priorizados (criterio 2).
3. Supuestos financieros del fundador (criterio 7).

## Observaciones
- El sistema respetó la regla de cero datos inventados en todos los entregables. Era el principal riesgo del modo en seco.
- Recomiendo que el Protocolo defina cómo delegar aprobaciones de bajo riesgo para que el fundador no sea el cuello de botella (pre-mortem #4).

# Viabilidad preliminar — 00-startup

> **Autor:** analista-financiero (simulado en seco) · 2026-11-21 · **BORRADOR**. Sin cifras: los supuestos están vacíos a propósito.

## Estructura del modelo
Modelo reproducible en `modelos/viabilidad.py` con entradas en `modelos/supuestos.csv`. El script **se niega a calcular** si hay supuestos vacíos: así nadie puede tomar como resultado un número sin respaldo.

## Variables clave
| Variable | Fuente esperada |
|---|---|
| Ticket medio por proyecto (por mercado, moneda local y USD) | investigador-mercado (precios de competidores) |
| Proyectos por mes (capacidad) | Chief of Staff (capacidad de supervisión del fundador = cuello de botella) |
| Costo variable por proyecto (uso de modelos de IA, hosting, herramientas) | arquitecto-soluciones, devops-sre |
| Costos fijos mensuales | Fundador |
| CAC por canal | growth-cro, medios-pagados (fase 1) |
| Tasa de retención / recurrencia (mantenimiento, crecimiento) | cuentas-ventas |

## Salidas del modelo
Margen de contribución por proyecto · punto de equilibrio (proyectos/mes) · escenarios pesimista/base/optimista a 12, 24 y 36 meses · tornado de las 5 variables más sensibles.

## Observación preliminar (cualitativa)
La capacidad de revisión del fundador limita la escala: cada puerta exige su aprobación. El modelo debe tratar las horas del fundador por proyecto como restricción explícita.

# Configuración de la empresa — fuente única de verdad

> Este es el **único** lugar donde se define el nombre y los datos base de la empresa.
> Todos los demás archivos usan la variable `{NOMBRE_STARTUP}` y deben resolverla leyendo este archivo.
> Cuando la ronda de naming (`/naming`) cierre con aprobación del fundador, solo se edita la tabla de abajo.

## Variables

| Variable | Valor actual | Estado | Última modificación |
|---|---|---|---|
| `{NOMBRE_STARTUP}` | Native Web Design | PROVISIONAL — sujeto a ronda de naming | 2026-11-21 |
| `{DOMINIO}` | por definir | PENDIENTE (depende de naming y disponibilidad) | — |
| `{FUNDADOR}` | Fundador (único humano del equipo) | Vigente | 2026-11-21 |
| `{IDIOMA_INTERNO}` | Español | Vigente | 2026-11-21 |
| `{MONEDA_REPORTE}` | USD (reporte consolidado); moneda local por proyecto | Vigente (ver `config/mercados.md`) | 2026-11-21 |

## Descripción

{NOMBRE_STARTUP} es una startup de desarrollo web con consultoría integral: estrategia, marca, experiencia, ingeniería con stack agnóstico, crecimiento, gobierno legal y seguridad.

## Modelo operativo

- 100 % agentes de Claude Code: 1 Chief of Staff (sesión principal) + 30 especialistas en `.claude/agents/`.
- Único humano: el fundador. Aprueba cada puerta de fase y **toda** acción externa (enviar, publicar, comprar, gastar, probar seguridad).

## Mercados

- **Fase 1:** continente americano — México, EE. UU., Canadá, Centroamérica, Sudamérica y Caribe.
- **Fase 2:** Europa.
- Idiomas de servicio: español (LatAm), inglés (EE. UU./CA), portugués (BR), francés (CA-QC).
- Detalle por país: `config/mercados.md`.

## Proyecto 0

La propia empresa es el primer cliente: `proyectos/00-startup/` (investigación de mercado, posicionamiento, sitio propio, portafolio y naming definitivo).

## Regla de uso de la variable

- En prosa y plantillas escribir literalmente `{NOMBRE_STARTUP}`.
- Al producir un entregable final para publicación (sitio, propuesta), el agente resuelve el valor desde esta tabla y deja constancia en el handoff de qué valor usó y con qué estado (PROVISIONAL / DEFINITIVO).
- Mientras el estado sea PROVISIONAL, ningún entregable puede registrar dominio, marca, perfiles sociales ni imprimir materiales con el nombre.

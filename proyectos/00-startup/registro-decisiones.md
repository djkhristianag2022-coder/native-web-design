# Registro de decisiones (ADR) — 00-startup

| ID | Fecha | Título | Estado | Decide | Fase |
|---|---|---|---|---|---|
| ADR-001 | 2026-11-21 | Tratar el Proyecto 0 como proyecto estándar (equipo completo) | Aceptada | Chief of Staff | 0 |
| ADR-002 | 2026-11-21 | Ejecutar la fase 0 en seco antes de la investigación real | Aceptada | Fundador (instrucción) | 0 |
| ADR-003 | 2026-11-21 | Priorizar mercados con una matriz ponderada antes de investigar en profundidad | Propuesta | Fundador | 0 |
| ADR-004 | 2026-11-21 | Construir el portafolio inicial solo con trabajo real y declarado como tal | Propuesta | Fundador | 0 |
| ADR-005 | 2026-11-21 | Ajustes al protocolo: niveles de aprobación, guardián técnico y matriz de responsabilidades | Aceptada | Fundador | 0 |

---

## ADR-001: Tratar el Proyecto 0 como proyecto estándar
- **Estado:** Aceptada · **Propone/Decide:** Chief of Staff · **Fase:** 0
### Contexto
El Proyecto 0 abarca investigación multipaís, naming, marca, sitio multilingüe y portafolio. Es la referencia de calidad para todos los proyectos futuros.
### Decisión
Usar el equipo completo, no el núcleo mínimo.
### Consecuencias
Más esfuerzo por fase; a cambio, cada agente ensaya su rol y se detectan huecos del sistema antes del primer cliente real.
### Reversibilidad
Dos sentidos: se puede reducir a núcleo mínimo en cualquier fase.

## ADR-002: Ejecutar la fase 0 en seco
- **Estado:** Aceptada · **Decide:** Fundador (instrucción de verificación) · **Fase:** 0
### Contexto
Se pide validar el sistema antes de usarlo con datos reales.
### Decisión
Ejecutar el flujo completo sin búsquedas web ni acciones externas; toda cifra queda `PENDIENTE DE INVESTIGACIÓN`.
### Consecuencias
El dictamen sustantivo de la puerta será RECHAZADO por falta de datos; lo que se valida es el proceso. Se requiere una segunda corrida real.

## ADR-003: Priorizar mercados con matriz ponderada
- **Estado:** Propuesta · **Propone:** estratega-negocio + investigador-mercado · **Decide:** Fundador
### Contexto
La fase 1 abarca más de 30 países y 4 idiomas. Investigar todo con igual profundidad diluye el esfuerzo y retrasa el lanzamiento.
### Opciones
| Opción | Pros | Contras |
|---|---|---|
| A. Matriz ponderada (tamaño, digitalización, competencia, idioma, complejidad legal, cercanía operativa) para elegir 2-3 mercados "cabeza de playa" | Foco, evidencia comparable | Requiere una investigación ligera de todos primero |
| B. Investigar todos por igual | Visión completa | Lento; datos superficiales |
| C. Elegir mercados por intuición del fundador | Rápido | Sin evidencia; contradice el Protocolo |
### Decisión propuesta
A. Investigación ligera de todos + profunda de los 2-3 mejor puntuados.
### Reversibilidad
Dos sentidos.

## ADR-004: Portafolio inicial solo con trabajo real
- **Estado:** Propuesta · **Propone:** Chief of Staff (regla 1 del Protocolo) · **Decide:** Fundador
### Contexto
Sin clientes previos no hay casos. La tentación de usar maquetas o casos ficticios como portafolio choca con la regla de cero datos inventados y con normas de publicidad (p. ej., FTC sobre reseñas y testimonios falsos; `SUPUESTO — VERIFICAR` alcance con legal-privacidad).
### Opciones
| Opción | Pros | Contras |
|---|---|---|
| A. El propio sitio de {NOMBRE_STARTUP} como caso 1, documentado de punta a punta | Real, demuestra el proceso | Un solo caso |
| B. Proyectos de concepto rotulados "Proyecto conceptual — no es un cliente" | Muestra rango creativo | Menor credibilidad; requiere rotulado claro |
| C. 1-3 proyectos piloto reales (precio reducido o pro bono) con permiso de publicación | Prueba social real | Requiere ventas y tiempo |
### Decisión propuesta
A + B rotulado + C en cuanto sea posible.

## ADR-005: Ajustes al protocolo tras la corrida en seco
- **Fecha:** 2026-11-21 · **Estado:** Aceptada · **Propone:** Chief of Staff (hallazgos del pre-mortem y de la revisión de roles) · **Decide:** Fundador ("Sí, aplica los ajustes al protocolo y haz commit", 2026-11-21) · **Fase:** 0
### Contexto
La corrida en seco mostró que el fundador es el cuello de botella (pre-mortem #4), que no estaba claro si investigar en la web es una acción externa, que las reglas del pentester y del auditor solo dependían del texto de cada agente, y que había seis temas con dueño ambiguo.
### Decisión
1. Niveles de aprobación 0-3 (`CLAUDE.md` §2) y registro `config/aprobaciones-permanentes.md`. Leer fuentes públicas es Nivel 0.
2. Aprobación por lotes de las acciones externas en cada memo.
3. Guardián técnico `scripts/hooks/guardian.py` (regla 11), con pruebas.
4. Matriz de responsabilidades compartidas (`CLAUDE.md` §9): parches → devops-sre; consentimiento → analitica-datos; foto y video → director-creativo; etc.
5. Lo fiscal y contable requiere profesional humano local (regla 12).
### Consecuencias
Menos interrupciones al fundador; las dos reglas de seguridad más críticas pasan a tener control técnico. El guardián no detecta toda forma de tráfico de red, así que la regla escrita sigue siendo la referencia.
### Reversibilidad
Dos sentidos: se revierte retirando el hook de `.claude/settings.json` y las secciones §2 (niveles), §5 reglas 11-12 y §9 de `CLAUDE.md`.

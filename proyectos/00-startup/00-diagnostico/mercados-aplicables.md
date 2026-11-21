# Mercados y leyes aplicables — 00-startup

> **Autor:** legal-privacidad (simulado en seco por el Chief of Staff) · 2026-11-21 · **BORRADOR**
> **Verificación de vigencia: NO REALIZADA** (en seco, sin acceso a fuentes oficiales). Toda fila es `NO VERIFICADO` hasta consultar la fuente primaria. No es asesoría legal.

## 1. Qué aplica a {NOMBRE_STARTUP} como empresa

| Tema | Por qué aplica | Depende de | Estado |
|---|---|---|---|
| Ley de constitución, fiscal y facturación | País donde se constituya la empresa | **Pregunta abierta 1** | BLOQUEADO |
| Privacidad del sitio propio (formularios de contacto, analítica, newsletter) | Recolecta datos de prospectos en todos los mercados donde se promueva | Mercados priorizados | Ver §2 |
| Marca del nombre definitivo | Protección del nombre en mercados de operación | Naming (fase 2) | Ver §3 |
| Contratos de servicio con clientes (MSA, SOW, DPA) | Se actuará como **encargado** de datos de los clientes (sitios, CRM, analítica) | País de la empresa y del cliente | Pendiente fase 1 |
| Publicidad y prueba social | Portafolio, testimonios y claims del sitio propio | Mercados | Ver ADR-004 |
| Accesibilidad del sitio propio | Normas de cada mercado; además es demostración de capacidad | Mercados | Objetivo interno: WCAG 2.2 AA |

## 2. Privacidad: leyes candidatas por mercado (de `config/mercados.md`)

| Mercado | Ley | Punto a verificar al inicio del proyecto | Estado |
|---|---|---|---|
| México | LFPDPPP 2025 | Reglamento y lineamientos tras la extinción del INAI; autoridad competente | NO VERIFICADO ⚖️ |
| EE. UU. | CCPA/CPRA + leyes estatales; CAN-SPAM | Lista vigente de estados con ley integral y umbrales de aplicación (es probable que una startup pequeña no supere umbrales; verificar) | NO VERIFICADO |
| Canadá | PIPEDA; CASL para correo comercial | Estado de una eventual reforma federal | NO VERIFICADO |
| Quebec | Ley 25; Carta de la lengua francesa | Consentimiento para cookies; obligación de francés | NO VERIFICADO ⚖️ |
| Brasil | LGPD | Encarregado; reglamentos ANPD para agentes de pequeño porte | NO VERIFICADO |
| Colombia | Ley 1581/2012 | Obligación de RNBD según tamaño | NO VERIFICADO |
| Argentina | Ley 25.326 | Estado del proyecto de reforma | NO VERIFICADO |
| Chile | Ley 21.719 | **Vigencia en revisión legislativa**: fecha efectiva | EN REVISIÓN ⚖️ |
| Perú | Ley 29733 + reglamento | Obligaciones del nuevo reglamento | NO VERIFICADO |
| Centroamérica y Caribe | Por país | Evaluar solo los países priorizados | NO EVALUADO |

## 3. Marcas (para naming)
Oficinas por mercado: IMPI (MX), USPTO (EE. UU.), CIPO (CA), INPI (BR); EUIPO en fase 2. Clases de Niza probables: 35 y 42 (`SUPUESTO`, confirmar). La búsqueda preliminar no sustituye la opinión de registrabilidad ⚖️.

## 4. Recomendaciones
1. Responder la pregunta abierta 1 (país de constitución): desbloquea fiscalidad, contratos y marca prioritaria.
2. En la corrida real, verificar con fuente oficial solo las leyes de los 2-3 mercados priorizados (ADR-003) y dejar el resto en `config/mercados.md` como NO VERIFICADO.
3. Presupuestar una consulta con abogado local en el país de constitución y en el primer mercado prioritario ⚖️.

# Matriz de mercados — {NOMBRE_STARTUP}

> **Responsable:** `legal-privacidad` (mantenimiento y verificación de vigencia).
> **Colaboran:** `localizacion-i18n` (idioma/formatos), `analista-financiero` (moneda/facturación), `accesibilidad` (normas de accesibilidad).
>
> **Estado de verificación:** versión base redactada el 2026-11-21 a partir del conocimiento interno del modelo, **sin verificación contra fuente primaria**. Toda fila se considera `SUPUESTO — VERIFICAR` hasta que `legal-privacidad` registre URL oficial y fecha de consulta en la columna "Fuente". Al iniciar cada proyecto, `legal-privacidad` verifica la vigencia de cada ley aplicable y actualiza esta tabla.
>
> Nada de este archivo es asesoría legal. Todo tema marcado ⚖️ requiere validación de un abogado local antes de comprometerse con el cliente.

## 1. Privacidad y protección de datos

| País / región | Ley principal | Autoridad | Notas clave para sitios web | Estado | Fuente (URL + fecha) |
|---|---|---|---|---|---|
| México | LFPDPPP (nueva ley publicada en el DOF en marzo 2025) | Secretaría Anticorrupción y Buen Gobierno (asumió funciones del extinto INAI) | Aviso de privacidad integral/simplificado; derechos ARCO; consentimiento para datos sensibles ⚖️ | SUPUESTO — VERIFICAR reglamento y lineamientos | pendiente |
| EE. UU. (federal) | Sin ley general; FTC Act §5, COPPA, CAN-SPAM, TCPA | FTC / FCC | Prácticas desleales; menores de 13; email comercial | SUPUESTO — VERIFICAR | pendiente |
| EE. UU. (estatal) | CCPA/CPRA (California) y leyes estatales integrales (VA, CO, CT, UT, TX, OR, etc.) | CPPA (CA) y fiscales generales estatales | Aviso en punto de recolección; opt-out de venta/compartir; señales GPC ⚖️ | SUPUESTO — VERIFICAR lista vigente de estados | pendiente |
| Canadá (federal) | PIPEDA (C-27/CPPA no aprobada a la fecha conocida) | OPC | Consentimiento significativo; notificación de brechas | SUPUESTO — VERIFICAR | pendiente |
| Canadá — Quebec | Ley 25 (modernización de la ley de privacidad del sector privado) | CAI | Responsable de privacidad designado; EIPD; consentimiento explícito para cookies no esenciales; transferencias fuera de QC ⚖️ | SUPUESTO — VERIFICAR | pendiente |
| Brasil | LGPD (Lei 13.709/2018) | ANPD | Bases legales; encarregado (DPO); derechos del titular; transferencias internacionales | SUPUESTO — VERIFICAR | pendiente |
| Colombia | Ley 1581 de 2012 + Decreto 1377/2013 | SIC | Autorización previa; RNBD para ciertos responsables ⚖️ | SUPUESTO — VERIFICAR | pendiente |
| Argentina | Ley 25.326 | AAIP | Registro de bases; proyecto de reforma en trámite | SUPUESTO — VERIFICAR | pendiente |
| Chile | Ley 21.719 (nueva ley; reemplaza 19.628) | Agencia de Protección de Datos Personales | **Vigencia en revisión legislativa**: confirmar fecha efectiva antes de cada proyecto ⚖️ | EN REVISIÓN | pendiente |
| Perú | Ley 29733 + nuevo reglamento | ANPD (MINJUSDH) | Registro de bancos de datos; transferencias | SUPUESTO — VERIFICAR | pendiente |
| Centroamérica y Caribe | Mosaico (p. ej. Costa Rica Ley 8968, Panamá Ley 81, Rep. Dominicana Ley 172-13) | Varía | Analizar país por país al activar el mercado | NO EVALUADO | pendiente |
| UE (fase 2) | RGPD, Directiva ePrivacy, DSA, AI Act | APD nacionales / CE | Consentimiento previo para cookies; DPIA; obligaciones de IA por riesgo | FASE 2 | pendiente |

## 2. Matriz operativa por país

| País | Idioma(s) del sitio | Locale / hreflang | Moneda (ISO 4217) | Accesibilidad aplicable | Consumo / comercio electrónico | Facturación |
|---|---|---|---|---|---|---|
| México | es-MX | `es-MX` | MXN | Ley General para la Inclusión de las Personas con Discapacidad; referencia WCAG 2.2 AA | LFPC / PROFECO (precios con IVA, términos claros) | CFDI 4.0 (SAT); IVA 16 % |
| EE. UU. | en-US (+ es-US opcional) | `en-US`, `es-US` | USD | ADA Títulos II/III (jurisprudencia WCAG; regla DOJ Título II con WCAG 2.1 AA para entidades públicas); Sección 508 para gobierno federal | FTC (reseñas falsas prohibidas, auto-renovación), leyes estatales | Sin factura electrónica obligatoria; sales tax por estado (nexo) ⚖️ |
| Canadá (excepto QC) | en-CA, fr-CA | `en-CA`, `fr-CA` | CAD | AODA (Ontario, WCAG 2.0 AA), Accessible Canada Act (federal) | Competition Act; leyes provinciales | GST/HST |
| Canadá — Quebec | fr-CA obligatorio | `fr-CA` | CAD | AODA no aplica; norma SGQRI 008 sector público; referencia WCAG | Carta de la lengua francesa (Ley 96): el francés debe estar disponible y no ser inferior ⚖️ | GST + QST |
| Brasil | pt-BR | `pt-BR` | BRL | Lei Brasileira de Inclusão (13.146/2015), eMAG (gobierno) | Código de Defesa do Consumidor; Decreto de comercio electrónico | NF-e / NFS-e (transición al estándar nacional); reforma tributaria IBS/CBS en curso ⚖️ |
| Colombia | es-CO | `es-CO` | COP | Ley 1618/2013; NTC 5854 | Estatuto del Consumidor (Ley 1480) | Factura electrónica DIAN |
| Argentina | es-AR | `es-AR` | ARS (cotizar en USD con cautela por tipo de cambio) | Ley 26.653 (accesibilidad web, sector público) | Ley 24.240 de Defensa del Consumidor | Factura electrónica ARCA (ex-AFIP) |
| Chile | es-CL | `es-CL` | CLP | Ley 21.015 / Ley 20.422 | Ley 19.496 (SERNAC) | DTE (SII) |
| Perú | es-PE | `es-PE` | PEN | Ley 29973 | Código de Protección y Defensa del Consumidor (Ley 29571) | CPE (SUNAT) |
| Centroamérica / Caribe | es-419 / en / fr / nl según país | `es-419` como fallback LatAm | Varía (USD en PA, SV, EC) | Por país | Por país | Por país |
| UE (fase 2) | según país | según país | EUR y locales | European Accessibility Act (aplicable desde 28-jun-2025), EN 301 549 | Directiva de derechos del consumidor, DSA | ViDA / e-factura por país |

## 3. Reglas de uso

1. **Al iniciar un proyecto** (fase 0), `legal-privacidad` produce `proyectos/<cliente>/00-diagnostico/mercados-aplicables.md` con solo las filas que apliquen, cada una con URL oficial y fecha de consulta.
2. Una fila sin fuente verificada no puede usarse para cerrar una puerta: se lleva al memo del fundador como riesgo.
3. Cambios a este archivo se registran en `proyectos/00-startup/registro-decisiones.md` con un ADR tipo "Actualización regulatoria".

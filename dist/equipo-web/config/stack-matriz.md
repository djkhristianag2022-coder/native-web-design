# Matriz de decisión de stack — {NOMBRE_STARTUP}

> **Responsable:** `arquitecto-soluciones`. **Consultados:** `frontend-performance`, `backend-integraciones`, `ingeniero-plataformas`, `devops-sre`, `appsec`, `analista-financiero`.
> El equipo es **agnóstico**: no hay stack por defecto. Cada proyecto elige con esta matriz y deja un ADR en `proyectos/<cliente>/registro-decisiones.md`.

## 1. Criterios y pesos por defecto

| # | Criterio | Peso por defecto | Qué se evalúa | Evidencia exigida |
|---|---|---|---|---|
| C1 | Costo total (TCO 36 meses) | 20 % | Licencias, hosting, desarrollo, mantenimiento, salida | Modelo de `analista-financiero` |
| C2 | Rendimiento | 20 % | Core Web Vitals alcanzables (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 al p75), TTFB, peso de página | Benchmarks o prototipo medido |
| C3 | Seguridad | 20 % | Superficie de ataque, historial de CVE, actualizaciones, soporte de cabeceras/CSP, ASVS L2 | Revisión de `appsec` |
| C4 | Mantenimiento | 15 % | Madurez, comunidad, LTS, disponibilidad de talento, deuda técnica | Fuentes con fecha |
| C5 | Autonomía del cliente | 15 % | ¿Puede el cliente editar contenido sin nosotros? Curva de aprendizaje, editor visual | Perfil del equipo del cliente (brief) |
| C6 | Encaje funcional e integraciones | 10 % | i18n multilingüe, pagos locales, CRM, comercio | Lista de requisitos del brief |

Los pesos pueden ajustarse **solo** con justificación en el ADR (p. ej., un e-commerce sube C6; una ONG con equipo no técnico sube C5).

## 2. Escala

1 = inaceptable · 2 = débil · 3 = adecuado · 4 = fuerte · 5 = excelente. Puntaje = Σ (peso × nota). Cualquier criterio con nota 1 descalifica la opción, sin importar el total. Seguridad con nota ≤ 2 exige dictamen explícito de `appsec`.

## 3. Familias de opciones a considerar (no exhaustivo)

| Familia | Ejemplos | Suele ganar cuando |
|---|---|---|
| Estático / islas | Astro, Eleventy, HTML/CSS puro | Sitio de marketing, contenido, rendimiento máximo |
| Framework JS full-stack | Next.js, Nuxt, SvelteKit, Remix | Interactividad, apps, personalización |
| CMS tradicional | WordPress, Drupal | Equipo editorial grande, ecosistema de plugins, presupuesto ajustado |
| CMS headless | Sanity, Contentful, Strapi, Payload | Multicanal, multilingüe, editores + frontend moderno |
| SaaS visual | Webflow, Wix Studio, Framer | Autonomía máxima del cliente, time-to-market |
| E-commerce | Shopify, WooCommerce, Medusa, BigCommerce | Venta en línea; validar pagos locales (Mercado Pago, Pix, OXXO) |
| Enterprise DXP | AEM, Sitecore, Optimizely | Grandes corporativos con gobierno de contenido complejo |

## 4. Plantilla de evaluación (copiar al ADR)

| Criterio | Peso | Opción A | Opción B | Opción C |
|---|---|---|---|---|
| C1 Costo | | | | |
| C2 Rendimiento | | | | |
| C3 Seguridad | | | | |
| C4 Mantenimiento | | | | |
| C5 Autonomía | | | | |
| C6 Encaje | | | | |
| **Total ponderado** | 100 % | | | |
| Descalificadores | | | | |

## 5. Reglas

- Mínimo 3 opciones de familias distintas, salvo que el brief imponga una plataforma (se documenta como restricción).
- Toda nota cita evidencia; sin evidencia, la nota es 3 y se marca `SUPUESTO`.
- El ADR incluye plan de salida (cómo migrar si la decisión falla).

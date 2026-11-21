---
description: Revisión de seguridad completa de un proyecto: appsec (código, dependencias, cabeceras), pentest autorizado y estado GRC.
argument-hint: <slug-cliente>
---

Como Chief of Staff, coordina la revisión de seguridad del proyecto **$ARGUMENTS**.

1. **Control de autorización (obligatorio antes de cualquier prueba dinámica).** Lee `proyectos/<slug>/seguridad/autorizacion-pentest.md`. Verifica: firma del cliente, aprobación del fundador, lista de activos, ventana vigente, contactos, y que el bloque `autorizacion-maquina` coincida con las secciones 2 y 5 del documento (el guardián solo lee ese bloque). No modifiques tú los estados de firma o aprobación: solo el fundador. Si algo falta, **no invoques a `pentester-autorizado`** para pruebas; registra BLOQUEADO y pide al fundador la autorización en el memo.
2. `appsec`: actualizar modelo de amenazas, ASVS L2, SAST, SCA, escaneo de secretos, cabeceras/CSP → `seguridad/revisiones/` y dictamen `auditorias/<slug>/fase-<n>-dictamen-appsec.md`.
3. `pentester-autorizado` (solo con autorización válida): plan dentro del alcance → pruebas en la ventana → reporte CVSS → dictamen. Nunca sistemas de terceros.
4. `grc-seguridad`: actualizar matriz de controles y registro de riesgos.
5. `secops-incidentes`: confirmar monitoreo, WAF y plan IR vigentes.
6. Consolida en `seguridad/resumen-seguridad-AAAA-MM-DD.md`: hallazgos por severidad, estado de remediación, riesgos residuales.
7. Si hay hallazgos **críticos o altos** abiertos: el sitio no se lanza (o, si ya está en producción, es `ESCALAMIENTO INMEDIATO` al fundador con plan de contención).

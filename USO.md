# Cómo usar el equipo desde cualquier sesión

El equipo (1 Chief of Staff + 30 especialistas) se puede usar de tres formas. Elige según dónde trabajes.

| Dónde trabajas | Qué usar | Subagentes reales | Guardián | Comandos |
|---|---|---|---|---|
| Sesión de Claude Code abierta **en este repositorio** (web, escritorio, móvil o terminal) | Nada que instalar | Sí | Sí | `/nuevo-proyecto`, `/fase`… |
| Claude Code o Cowork **en cualquier otro repositorio o carpeta** (p. ej., el código de un cliente) | **Plugin** `equipo-web` | Sí | Sí | `/equipo-web:nuevo-proyecto`, `/equipo-web:fase`… |
| **Chat normal** de claude.ai (web o app) | **Skill** `equipo-web` | No: Claude adopta cada rol por turnos | No | En lenguaje natural: "nuevo proyecto…", "fase 2…" |

**Recomendación:** para desarrollar un proyecto (código, pruebas, seguridad), usa Claude Code o Cowork con el plugin. Para estrategia, marca, contenido y memos desde el móvil, el chat con la skill es suficiente.

---

## 1. En este repositorio (ya funciona)

En claude.ai/code o en la app de Claude, abre una sesión nueva de Claude Code y elige el repositorio `djkhristianag2022-coder/native-web-design`. El protocolo, los 30 agentes, los comandos y el guardián se cargan solos. Los proyectos quedan en `proyectos/<cliente>/` dentro de este repositorio.

## 2. Plugin para Claude Code y Cowork

### Instalar en Claude Code (terminal o sesión)

```
/plugin install equipo-web --marketplace djkhristianag2022-coder/native-web-design
```

En versiones anteriores a 2.1.275, en dos pasos:

```
/plugin marketplace add djkhristianag2022-coder/native-web-design
/plugin install equipo-web@equipo-agentes
```

### Instalar en claude.ai, la app de escritorio o Cowork

1. Ve a **Personalizar → Plugins → Añadir → Añadir marketplace** (los nombres exactos del menú pueden variar según el idioma y la versión de la app).
2. Escribe `djkhristianag2022-coder/native-web-design`.
3. Instala el plugin **equipo-web**.

Como el repositorio es privado, tu cuenta de GitHub debe estar conectada y la Claude GitHub App instalada en él (ya lo está).

### Usar

1. Abre la sesión en la carpeta o repositorio donde vivirá el proyecto.
2. Ejecuta `/equipo-web:nuevo-proyecto <cliente> <descripción>`.
3. La primera vez, el Chief of Staff copia `config/` y `plantillas/` a esa carpeta. Desde entonces esas copias son la fuente de verdad de ese espacio de trabajo. **Revisa `config/empresa.md`**, para que el nombre de la empresa sea el vigente.
4. Sigue con `/equipo-web:fase <n> <cliente>`, `/equipo-web:auditoria`, etc.

### Actualizar

Cuando cambie el repositorio: `/plugin marketplace update equipo-agentes`. En Cowork, actualiza desde la página del plugin.

## 3. Skill para el chat de claude.ai

### Instalar

1. Descarga `dist/equipo-web.zip` de este repositorio (en GitHub: abre el archivo y pulsa *Download raw file*).
2. En claude.ai: **Personalizar → Skills → + → Crear skill → Subir una skill** y elige el zip.
3. Si te lo pide, activa la ejecución de código en **Configuración → Capacidades**: así Claude puede entregar los archivos del proyecto.

### Usar

- Crea un **Proyecto de claude.ai por cliente** y guarda ahí `brief.md`, `estado.md` y `registro-decisiones.md` a medida que salgan. Así cualquier conversación nueva retoma donde quedó.
- Escribe en lenguaje natural: "Abre un proyecto nuevo para <cliente>: …", "Ejecuta la fase 1 de <cliente>", "Audita la fase 1", "Prepara el reporte de diciembre".

### Límites del modo chat

- **Sin subagentes:** Claude trabaja cada rol por turnos en la misma conversación. La auditoría red team no está aislada, y el memo lo indica.
- **Sin guardián técnico ni pruebas de seguridad:** el pentest solo se planifica; se ejecuta con el plugin en Claude Code y con autorización firmada.
- **Puertas 4 y 5 (construcción y lanzamiento):** hazlas en Claude Code o Cowork.

### Actualizar

Cuando cambie el repositorio, descarga el zip nuevo y vuelve a subirlo para reemplazar la skill.

---

## Para el mantenimiento (no para el uso diario)

El plugin y la skill se **generan** desde las fuentes del repositorio. No los edites a mano:

```
python3 scripts/construir_distribucion.py            # regenera plugin/, .claude-plugin/ y dist/
python3 scripts/construir_distribucion.py --verificar # comprueba que están al día
```

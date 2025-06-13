# 🧪 Prueba Técnica - ToDo App Fullstack (FastAPI + Next.js)

Esta prueba técnica consiste en desarrollar una pequeña aplicación fullstack de tipo To-Do List, utilizando **FastAPI** para el backend y **Next.js** para el frontend. El objetivo es evaluar tu nivel de conocimiento en desarrollo frontend, consumo de APIs, estructura de proyecto, y buenas prácticas.

---

### Globales:
- [Python 3.10+](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org/)
- [npm](https://www.npmjs.com/) o [yarn](https://yarnpkg.com/)
- [Git](https://git-scm.com/)

## 🎯 Objetivo

Crear una aplicación que permita:
- Crear tareas
- Listar tareas
- Editar tareas
- Eliminar tareas
- (Bonus) Notificar en tiempo real al frontend cuando una nueva tarea se crea o actualiza

**La aplicación debe estar desarrollada como una Single Page Application (SPA).**

---

## ⚙️ Stack tecnológico

- **Frontend:** Next.js (React)
- **Backend:** FastAPI (Python)
- **Base de Datos:** SQLite
- **(Bonus)** WebSocket para notificaciones en tiempo real
- **Estilos:** TailwindCSS o Material UI (**obligatorio**, no usar CSS puro)

---

## ✅ Requerimientos del Proyecto

### 🔧 Backend (FastAPI)
- CRUD completo: `GET /tasks`, `POST /tasks`, `PUT /tasks/{id}`, `DELETE /tasks/{id}`
- Organización del código por capas:
  - Routers (endpoints)
  - Schemas (Pydantic con validaciones)
  - Models (SQLAlchemy con tipos correctos)
  - Repositorio o servicio para lógica de negocio
- Buenas prácticas:
  - Código limpio, legible y bien documentado (docstrings y comentarios)
  - Aplicación de principios SOLID en la medida de lo posible
  - Separación clara de responsabilidades
- Validaciones en los esquemas Pydantic:
  - `titulo`: requerido, mínimo 1 carácter, máximo 100
  - `descripcion`: opcional, máximo 500 caracteres
  - `completado`: booleano (por defecto False)
- Modelo sugerido:
```python
Tarea:
- id: int (autoincremental)
- titulo: str (requerido, 1-100 caracteres)
- descripcion: str (opcional, hasta 500 caracteres)
- completado: bool (por defecto False)
- fecha_creacion: datetime (generado automáticamente)
```

### 🎨 Frontend (Next.js)
- Página principal que:
  - Liste todas las tareas
  - Permita crear una nueva tarea (formulario con validaciones)
  - Permita editar una tarea existente (formulario con validaciones)
  - Permita eliminar tareas
- Validaciones de formularios:
  - `titulo`: requerido, no vacío
  - `descripcion`: máximo 500 caracteres
- Buen diseño visual (**BONUS usar TailwindCSS, Material UI o cualquier otro framework**)
- Organización clara de:
  - Componentes reutilizables
  - Servicios de conexión con la API
  - Estilos en archivos separados o integrados por Tailwind o Material UI
- Buenas prácticas:
  - Código legible y ordenado
  - Separación de lógica y presentación
  - Manejo adecuado de errores, estados de carga y vacíos
  - Comentarios/documentación del código donde aplique

### ⭐ Bonus opcional
- Implementar un **WebSocket** para que el frontend reciba una notificación cuando se cree o actualice una tarea

---

## 📄 Documentación

- Todo el código debe estar **documentado** con comentarios y docstrings explicando:
  - Qué hace cada función o clase
  - Cómo se conecta cada parte del proyecto
  - Instrucciones claras para ejecutar y probar el proyecto

---

## 🧱 Estructura sugerida del proyecto siguiendo patron MVC

```
technical-test-fe/
├── backend/
│   ├── app/
│   │   ├── core/                     # Configuraciones generales
│   │   │   └── config.py
│   │   ├── views/
│   │   │   └── task_view.py        # (Vistas/Controladores) - Endpoints
│   │   ├── models/
│   │   │   └── task_model.py       # Modelos de BD con SQLAlchemy
│   │   ├── schemas/
│   │   │   └── task_schema.py      # Validaciones con Pydantic
│   │   ├── repository/
│   │   │   └── task_repository.py  # Acceso a datos (consultas a la BD)
│   │   ├── services/
│   │   │   └── task_service.py     # Lógica de negocio (servicios)
│   │   ├── websocket/
│   │   │   └── notifier.py         # Lógica de WebSocket (opcional)
│   │   └── main.py                 # App principal FastAPI
│   └── requirements.txt            # Dependencias del backend
├── frontend/
│   ├── components/                 # Componentes reutilizables
│   ├── pages/                      # Páginas principales (SPA)
│   ├── services/                   # Servicios que llaman a la API
│   └── styles/                     # Configuración Tailwind o Material UI
└── README.md
```

---

## 🚀 Cómo ejecutar el proyecto

### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```

---

## 📬 Endpoints de API (ejemplo)

- `GET /api/v1/tasks/` - Lista todas las tareas
- `POST /api/v1/tasks/` - Crea una tarea
- `PUT /api/v1/tasks/{id}` - Actualiza una tarea
- `DELETE /api/v1/tasks/{id}` - Elimina una tarea


## 🔔 WebSocket (Notificaciones en tiempo real) (Opcional)

Como punto adicional, se implementará un WebSocket en el backend para enviar notificaciones al frontend cuando ocurra algún evento, por ejemplo, cuando se cree o actualice una tarea.

### Backend (FastAPI)
- Usar `WebSocket` de FastAPI.
- Crear un `WebSocketManager` que maneje conexiones activas y mensajes.
- En los endpoints de crear/actualizar tarea, se debe enviar un mensaje al WebSocket.


### Frontend (Next.js)
- Utilizar `WebSocket` nativo del navegador.
- Conectarse al WebSocket al cargar la página y mostrar una notificación o actualizar la UI automáticamente.
- Conexión: `ws://localhost:8000/ws/notifications`

---

## 🧠 Git y control de versiones (obligatorio)

- El repositorio base será proporcionado por el evaluador con la estructura del proyecto
- Clona el repositorio y crea una nueva rama para tu implementación:
```bash
git clone https://github.com/SebastianRaveG/technical-test-fe.git
git checkout -b nombre-tu-rama
```
- Realiza commits atómicos y descriptivos
- Sube tu rama al repositorio remoto:
```bash
git push origin nombre-tu-rama
```
- Finalmente, crea un Pull Request para integrar tus cambios a `main` y descríbelo correctamente

---

## ✅ Evaluación

Se valorará:
- Correcta estructura del código (claridad y separación de capas)
- Aplicación de principios SOLID y buenas prácticas de clean code
- Validaciones correctas en formularios y datos backend
- Frontend con diseño moderno, validaciones funcionales y buena UX
- Comentarios y documentación clara en el código
- Proyecto que corre sin errores desde cero
- Buen uso de Git (ramas, commits, PRs)
- Bonus: WebSocket funcionando e integrado de forma limpia

---

¿Listo para empezar? Puedes completar tu solución en esta estructura o adaptarla con tu propio estilo, siempre y cuando mantengas buenas prácticas y documentación clara.

# Contexto para Gemini (Asistente de Código)

Este documento proporciona a Gemini el contexto esencial sobre el proyecto actual, permitiéndole ofrecer asistencia más precisa, relevante y alineada con nuestras convenciones.

---

## 1. Propósito del Proyecto

**Nombre:** API de Gestión de Cursos (Educativa)
**Objetivo:** Construir una API RESTful simple con Python, Django y Django REST Framework (DRF) para gestionar una lista de cursos. El propósito es aprender y aplicar buenas prácticas de desarrollo de backend.

---

## 2. Stack Tecnológico Principal

- **Lenguaje:** Python 3.11+
- **Framework Backend:** Django, FastAPI
- **Framework API:** Django REST Framework (DRF)
- **Base de Datos:** SQLite (para desarrollo), PostgreSQL (para producción)
- **Gestor de Paquetes:** `pip` con `requirements.txt`
- **Formateador de Código:** `black`
- **Linter:** (Aún no definido, pero se usará uno como Flake8 o Ruff en el futuro)

---

## 3. Estructura del Proyecto (Django)

El proyecto sigue la estructura estándar de Django:

```
proyecto_drf/
├── manage.py
├── proyecto_drf/         # Directorio de configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── cursos/               # App de Django para gestionar cursos
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py    # <-- Lógica de serialización aquí
│   ├── tests.py
│   ├── urls.py           # <-- Rutas específicas de la app
│   └── views.py          # <-- Lógica de las vistas (ViewSets)
└── requirements.txt
```

**Convenciones Clave:**

- **Lógica de Negocio:** Principalmente en `views.py` y `serializers.py`.
- **Modelos:** Definidos en `models.py`.
- **Rutas:** Las rutas de la API se definen en `cursos/urls.py` y se incluyen en `proyecto_drf/urls.py`.
- **Serializers:** Usamos `ModelSerializer` de DRF para la conversión de datos.

---

## 4. Estructura de Proyectos con FastAPI

Para mantener un proyecto FastAPI organizado, escalable y fácil de mantener, se recomienda una estructura modular que separe las responsabilidades. El uso de `APIRouter` es clave para dividir la lógica de negocio en componentes más pequeños.

### 4.1. Árbol de Archivos Recomendado

```
/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers/
│       ├── __init__.py
│       ├── customer.py
│       ├── invoices.py
│       └── transactions.py
├── models.py
├── db.py
└── requirements.txt
```

### 4.2. Descripción de Componentes

- **`app/`**: Directorio principal que contiene la lógica de la aplicación.
  - **`main.py`**: Punto de entrada de la aplicación. Aquí se crea la instancia principal de `FastAPI` y se incluyen los routers de las diferentes áreas de la aplicación.
  - **`dependencies.py`**: Define dependencias comunes que se pueden inyectar en diferentes partes de la aplicación.
  - **`routers/`**: Directorio que agrupa los diferentes `APIRouter`. Cada archivo representa un conjunto de endpoints relacionados con una entidad de negocio.
- **`models.py`**: Define los modelos de datos de la aplicación (Pydantic, SQLModel, etc.).
- **`db.py`**: Contiene la configuración y la lógica para la conexión a la base de datos.
- **`requirements.txt`**: Lista de las dependencias de Python del proyecto.

---

## 5. Objetivos y Tareas Actuales

Actualmente, estoy enfocado en:

1.  **Construir el CRUD completo para el recurso `Curso`.**
2.  **Aprender a usar `ViewSet` y `Router` de DRF para simplificar las vistas.**
3.  **Implementar filtros básicos para la lista de cursos.**
4.  **Añadir documentación automática a la API.**
5.  **Configurar un entorno de desarrollo robusto y replicable.**

---

## 6. Estilo de Código y Preferencias

- **Formato:** Adherencia estricta a `black`. Por favor, genera código que ya esté formateado con `black`.
- **Tipado:** Uso de `type hints` de Python siempre que sea posible para mejorar la claridad y la robustez.
- **Commits:** Mensajes de commit claros y concisos, en español, siguiendo el formato convencional (`feat:`, `fix:`, `docs:`, etc.).
- **Idioma:** Prefiero que la comunicación, los comentarios y la documentación estén en **español**.

---

## 7. Cómo Puedes Ayudarme Mejor

- **Genera código idiomático:** Proporciona ejemplos que sigan las mejores prácticas de Python y Django/DRF/FastAPI.
- **Explica el "porqué":** Cuando sugieras un cambio o una nueva biblioteca, explica brevemente por qué es una buena idea.
- **Ayúdame a refactorizar:** Si ves una oportunidad para mejorar el código existente (simplificarlo, hacerlo más legible, etc.), no dudes en sugerirlo.
- **Piensa en los tests:** Aunque no siempre los pida explícitamente, ten en mente cómo se podría probar el código que generas.
- **Respeta las convenciones:** Usa la estructura y las convenciones definidas en este documento.

---
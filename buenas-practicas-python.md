# 📘 Buenas Prácticas de Python y Chuleta de Curso

Documento vivo para acumular principios, patrones, notas de curso y referencias técnicas para el desarrollo en Python.

---

## 1. Filosofía y Principios Fundamentales

- **Principios SOLID:** Aplicados a Python, guían el diseño de clases y módulos robustos.
  - **S - Responsabilidad Única:** Una clase o función debe hacer una sola cosa.
  - **O - Abierto/Cerrado:** Extiende el comportamiento con herencia o composición, no modificando el código existente.
  - **L - Sustitución de Liskov:** Los objetos de una clase hija deben poder sustituir a los de la clase padre sin romper la aplicación.
  - **I - Segregación de Interfaces:** Usa `typing.Protocol` o `abc.ABC` para crear interfaces pequeñas y específicas.
  - **D - Inversión de Dependencias:** Depende de abstracciones (`Protocol`), no de implementaciones concretas.

---

## 2. Calidad y Estilo de Código

### 2.1. PEP 8 y Formateo

- **PEP 8:** Es la guía de estilo oficial para el código Python. Síguela siempre.
- **Formateo Automático:** Usa `black .` para formatear todo el proyecto. Asegura un estilo consistente y elimina las discusiones sobre formato.

### 2.2. Tipado Estático (Type Hints)

- **Úsalo Siempre:** Añade `type hints` a las variables, argumentos de funciones y valores de retorno.
- **Beneficios:** Mejora la legibilidad, previene bugs y permite un mejor análisis estático por parte de editores y linters.
- **Ejemplo:** `def mi_funcion(nombre: str, edad: int) -> str:`

### 2.3. Docstrings y Comentarios

- **Docstrings:** Documenta todos los módulos, clases y funciones públicas. Sigue un formato estándar como Google, Sphinx o reStructuredText.
- **Comentarios:** Usa comentarios (`#`) para explicar el *porqué* de una línea de código compleja, no el *qué*. Si el código es tan complejo que necesita muchos comentarios, considera refactorizarlo.

### 2.4. Convenciones de Naming

| Tipo        | Convención         | Ejemplo              |
|-------------|--------------------|----------------------|
| Variables   | `snake_case`       | `nombre_usuario`     |
| Funciones   | `snake_case`       | `calcular_impuestos` |
| Clases      | `PascalCase`       | `FacturaDeVenta`     |
| Constantes  | `UPPER_SNAKE_CASE` | `TASA_DE_INTERES`    |
| Módulos     | `snake_case.py`    | `gestion_usuarios.py`|
| Campos bool | `es_` / `tiene_`   | `es_activo`, `tiene_permisos` |

### 2.5. Manejo de Errores y Excepciones

- **Sé Específico:** Captura excepciones concretas (`ValueError`, `KeyError`) en lugar de la genérica `Exception`.
- **Crea Excepciones Personalizadas:** Define tus propias excepciones para errores de dominio (ej. `UsuarioNoEncontradoError(Exception)`).
- **No Silencies Errores:** Evita bloques `except: pass`. Si es necesario, comenta por qué se está ignorando la excepción.
- **Usa `finally`:** Para código de limpieza que deba ejecutarse siempre (ej. cerrar un archivo o una conexión).

---

## 3. Herramientas del Ecosistema Python

### 3.1. Entornos Virtuales

- **Propósito:** Aislar las dependencias de diferentes proyectos.
- **Creación:** `python3 -m venv .venv`
- **Activación (Linux/macOS):** `source .venv/bin/activate`
- **Activación (Windows):** `.venv\Scripts\activate`

### 3.2. Gestión de Dependencias

- **`pip`:** El gestor de paquetes de Python.
- **`requirements.txt`:** El archivo estándar para listar las dependencias.
- **Instalar:** `pip install -r requirements.txt`
- **Guardar:** `pip freeze > requirements.txt`

### 3.3. Testing

- **`pytest`:** El framework de testing más popular. Es potente y fácil de usar.
  - **Ejecución:** `pytest`
- **`unittest`:** El framework de testing incluido en la librería estándar de Python.
  - **Ejecución:** `python -m unittest discover tests`

---

## 4. Estructura de Proyectos

### 4.1. Estructura Genérica Modular

```
mi_proyecto/
├── mi_paquete/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   └── routers/
├── tests/
└── requirements.txt
```

### 4.2. Estructura para FastAPI

Usa `APIRouter` para dividir la aplicación en módulos lógicos.

```
mi_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers/
│       ├── __init__.py
│       ├── usuarios.py
│       └── productos.py
├── models.py
└── db.py
```

### 4.3. Estructura para Django

Sigue la filosofía de "proyecto" y "apps".

```
mi_proyecto_django/
├── manage.py
├── proyecto_config/
│   ├── settings.py
│   └── urls.py
├── mi_app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
└── requirements.txt
```

---

## 5. Notas de Frameworks Web

### 5.1. FastAPI

- **Instalación:** `pip install "fastapi[standard]"`
- **Ejecución:** `uvicorn main:app --reload` o `fastapi dev main.py`
- **Modelos de Datos:** Usa Pydantic para definir los modelos de entrada y salida. La validación es automática.
- **Dependencias:** Usa el sistema de Inyección de Dependencias (`Depends`) para gestionar la lógica reutilizable (ej. `get_db`).

### 5.2. Django y Django REST Framework (DRF)

- **Serializers:** Son la clave para traducir los modelos de Django a JSON y viceversa. Centralizan la validación de datos.
- **ViewSets:** Agrupan la lógica para las operaciones CRUD de un recurso. `ModelViewSet` proporciona una implementación completa con muy poco código.
- **Routers:** Generan automáticamente las URLs para tus `ViewSets`.
- **Validación:**
  - **Nivel de Serializer:** Centraliza la validación aquí.
  - **Permisos:** Usa clases de permisos personalizadas para la autorización.
- **Throttling (Limitación de Peticiones):** Protege tu API contra el abuso. Configúralo globalmente en `settings.py` o por vista.

---

## 6. Ejemplos de Código y Patrones

### 6.1. Ejemplo de CRUD con DRF

```python
# models.py
from django.db import models
class Curso(models.Model):
    titulo = models.CharField(max_length=120)
    publicado = models.BooleanField(default=False)

# serializers.py
from rest_framework import serializers
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

# views.py
from rest_framework import viewsets
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# urls.py
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
urlpatterns = router.urls
```

### 6.2. Documentación de API con `drf-spectacular`

1.  `pip install drf-spectacular`
2.  Añadir `'drf_spectacular'` a `INSTALLED_APPS`.
3.  Configurar `REST_FRAMEWORK` en `settings.py`:
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }
    ```
4.  Añadir las rutas de la documentación en el `urls.py` principal.

---

## 7. Apéndice: Catálogo de Patrones de Diseño

(Esta sección se mantiene igual que en la versión anterior, ya que los patrones son conceptuales pero muy aplicables en Python)

### 7.1. Creacionales
*   **Singleton, Factory Method, Builder...**

### 7.2. Estructurales
*   **Adapter, Decorator, Facade, Proxy...**

### 7.3. Comportamiento
*   **Strategy, Observer, Command...**
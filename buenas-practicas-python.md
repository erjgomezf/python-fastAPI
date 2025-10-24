# 📘 Buenas Prácticas de Python y Chuleta de Curso

Documento vivo para acumular principios, patrones, notas de curso y referencias técnicas para el desarrollo en el ecosistema Python (Python puro, FastAPI, Django, DRF).

---

## 1. Filosofía y Principios Fundamentales

- **Principios SOLID:** Aplicados a Python, guían el diseño de clases y módulos robustos.
  - **S - Responsabilidad Única:** Una clase o función debe tener una sola razón para cambiar.
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
- **Abstracciones:** Usa `typing.Protocol` (preferido) o `abc.ABC` para definir contratos claros y aplicar los principios de Inversión de Dependencias y Sustitución de Liskov de forma pythónica.

### 2.3. Docstrings y Comentarios

- **Docstrings:** Documenta todos los módulos, clases y funciones públicas. Sigue un formato estándar como Google, Sphinx o reStructuredText.
- **Comentarios:** Usa comentarios (`#`) para explicar el _porqué_ de una línea de código compleja, no el _qué_. Si el código es tan complejo que necesita muchos comentarios, considera refactorizarlo.

- **Formato recomendado para Docstrings (estilo reStructuredText/Sphinx simplificado):**

  - Usar comillas triples `'''Docstring aquí'''`.
  - Una descripción breve en la primera línea.
  - Usar `*` para definir secciones claras como `* Atributos:`, `* Métodos:`, `* Parámetros:`.
  - Usar `-` para listar los elementos dentro de cada sección.

- **Ejemplo práctico:**
  ```python
  class MiVista(APIView):
      '''Vista para gestionar los perfiles de usuario.
      * Parámetros:
        - request: La petición HTTP.
      '''
  ```

### 2.4. Convenciones de Naming

| Tipo        | Convención                  | Ejemplo                       |
| ----------- | --------------------------- | ----------------------------- |
| Variables   | `snake_case`                | `nombre_usuario`              |
| Funciones   | `snake_case`                | `calcular_impuestos`          |
| Clases      | `PascalCase`                | `FacturaDeVenta`              |
| Constantes  | `UPPER_SNAKE_CASE`          | `TASA_DE_INTERES`             |
| Módulos     | `snake_case.py`             | `gestion_usuarios.py`         |
| Modelos     | `PascalCase`                | `Curso`, `UsuarioPerfil`      |
| Serializers | `PascalCase` + `Serializer` | `CursoSerializer`             |
| ViewSets    | `PascalCase` + `ViewSet`    | `CursoViewSet`                |
| Campos bool | `es_` / `tiene_`            | `es_activo`, `tiene_permisos` |

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

- **`pytest`:** El framework de testing más popular. Es potente y fácil de usar.
  - **Ejecución:** `pytest`
- **`unittest`:** El framework de testing incluido en la librería estándar de Python.
  - **Ejecución:** `python -m unittest discover tests`

---

## 4. Estructura de Proyectos

### 4.1. Estructura Genérica

```txt
mi_proyecto_python/
├── mi_paquete/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── services.py  # Lógica de negocio
│   └── routers/
├── tests/
└── requirements.txt
```

### 4.2. Estructura para FastAPI

Usa `APIRouter` para dividir la aplicación en módulos lógicos.

### 4.2.1. Árbol de Archivos Recomendado para FastAPI

```txt
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

### 4.2.2. Descripción de Componentes de FastAPI

- **`app/`**: Directorio principal que contiene la lógica de la aplicación.

  - **`main.py`**: Punto de entrada de la aplicación. Aquí se crea la instancia principal de `FastAPI` y se incluyen los routers de las diferentes áreas de la aplicación.
  - **`dependencies.py`**: Define dependencias comunes que se pueden inyectar en diferentes partes de la aplicación, como la obtención de la sesión de la base de datos o la autenticación de usuarios.
  - **`routers/`**: Directorio que agrupa los diferentes `APIRouter`. Cada archivo representa un conjunto de endpoints relacionados con una entidad de negocio.

    - **`customer.py` (ejemplo):**

      ```python
      # app/routers/customer.py
      from fastapi import APIRouter

      router = APIRouter(
          prefix="/customers",
          tags=["customers"],
      )

      @router.get("/")
      def read_customers():
          return [{"customer_id": 1, "name": "John Doe"}]
      ```

- **`models.py`**: Define los modelos de datos de la aplicación, generalmente utilizando Pydantic para la validación de datos o SQLModel/SQLAlchemy para la definición de tablas de la base de datos.
- **`db.py`**: Contiene la configuración y la lógica para la conexión a la base de datos.

```txt
mi_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers/
│       ├── __init__.py # Permite que Python trate el directorio como un paquete
│       ├── usuarios.py
│       └── productos.py
├── models.py
└── db.py
```

### 4.3. Estructura para Django

Sigue la filosofía de "proyecto" y "apps".

### 4.3.1. Árbol de Archivos Recomendado para Django

```txt
/
├── manage.py
├── requirements.txt
├── project_name/         # Directorio de configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── app_name/               # App de Django para una funcionalidad específica
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

### 4.3.2. Descripción de Componentes de Django

- **`manage.py`**: Utilidad de línea de comandos para interactuar con el proyecto Django (ej. `runserver`, `makemigrations`).
- **`project_name/`**: Directorio de configuración del proyecto que contiene `settings.py` y el `urls.py` principal.
- **`app_name/`**: Directorio que representa una aplicación de Django. Cada aplicación es un módulo de Python que se encarga de una funcionalidad específica (ej. `usuarios`, `productos`).
  - **`models.py`**: Define los modelos de la base de datos utilizando el ORM de Django.
  - **`serializers.py`**: Define los serializadores de DRF para convertir los modelos en JSON y viceversa.
  - **`views.py`**: Contiene la lógica de negocio (ViewSets o APIViews).
  - **`urls.py`**: Define las rutas específicas de la aplicación.

```txt
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
│   ├── permissions.py # Lógica de permisos personalizados
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
- **Comandos útiles:**
  - **Instalar:** `pip install fastapi`
  - **Instalar con extras (servidor, etc.):** `pip install "fastapi[standard]"`
  - **Ejecutar en desarrollo:** `uvicorn main:app --reload`
  - **Ejecutar con el CLI de FastAPI:** `fastapi dev main.py`
- **Configuración de Base de Datos (SQLModel con SQLite):**

  ```python
  # db.py (ejemplo para FastAPI con SQLModel)
  from typing import Annotated
  from fastapi import Depends, FastAPI
  from sqlmodel import Session, create_engine, SQLModel

  sqlite_name = "db.sqlite3" # Nombre del archivo de la base de datos SQLite
  sqlite_url = f"sqlite:///{sqlite_name}" # URL para la base de datos SQLite

  engine = create_engine(sqlite_url) # Crear el motor de la base de datos

  def create_all_tables(app: FastAPI):
      '''
      Crear todas las tablas en la base de datos.
      Parámetros:
      - app: La instancia de FastAPI.
      '''
      SQLModel.metadata.create_all(engine)
      yield

  def get_session():
      '''
      Obtener una sesión de base de datos.
      '''
      with Session(engine) as session:
          yield session
  SessionDep = Annotated[Session, Depends(get_session)] # Dependencia para obtener la sesión de base de datos
  ```

### 5.2. Django y Django REST Framework (DRF)

- **Serializers:** Son la clave para traducir los modelos de Django a JSON y viceversa. Centralizan la validación de datos.
- **ViewSets:** Agrupan la lógica para las operaciones CRUD de un recurso. `ModelViewSet` proporciona una implementación completa con muy poco código.
- **Routers:** Generan automáticamente las URLs para tus `ViewSets`.
- **Validación:**
  - **Nivel de Serializer:** Centraliza toda la validación de datos (nivel de campo, nivel de objeto) en los archivos `serializers.py`. Esto mantiene la lógica de validación contenida y reutilizable.
  - **Permisos:** Para lógicas de autorización complejas o reutilizables, crea un archivo `permissions.py` dentro de la app de Django. Define clases que hereden de `BasePermission`.
- **Throttling (Limitación de Peticiones):** Es una herramienta crucial para proteger tu API contra ataques de Denegación de Servicio (DoS) y abuso. DRF ofrece un sistema flexible.

  #### Configuración en Django REST Framework

  La forma más común de configurar el throttling es de manera global en tu archivo `settings.py`.

  1.  **Define las clases de throttling y los límites:**
      En `settings.py`, dentro del diccionario `REST_FRAMEWORK`, puedes establecer una política de throttling por defecto.
      ```python
      # settings.py
      REST_FRAMEWORK = {
          # ... otras configuraciones ...
          'DEFAULT_THROTTLE_CLASSES': [
              'rest_framework.throttling.AnonRateThrottle',  # Para usuarios anónimos (basado en IP)
              'rest_framework.throttling.UserRateThrottle'   # Para usuarios autenticados (basado en user ID)
          ],
          'DEFAULT_THROTTLE_RATES': {
              'anon': '100/day',  # Límite para usuarios anónimos
              'user': '1000/day'  # Límite para usuarios autenticados
          }
      }
      ```
  2.  **Personalización por Vista:**
      Si necesitas una política de throttling más específica para una vista en particular, puedes sobreescribir la configuración global directamente en la `APIView` o `ViewSet`.

      ```python
      # bookings/views.py
      from rest_framework.throttling import UserRateThrottle
      from rest_framework.views import APIView

      class VistaEspecial(APIView):
          throttle_classes = [UserRateThrottle]
          # Nota: DRF usará el 'DEFAULT_THROTTLE_RATES' para 'user'
          # a menos que definas una clase de throttle personalizada.
      ```

- **Migraciones:**
  - Crea migraciones atómicas y con nombres claros.
  - Nunca modifiques una migración que ya ha sido aplicada en entornos compartidos (como `main` o `develop`). En su lugar, crea una nueva migración para corregirla.
- **Archivos Estáticos:** Ejecuta `python manage.py collectstatic` antes de desplegar en producción para agrupar todos los archivos estáticos en el directorio definido en `STATIC_ROOT`.

---

## 6. Ejemplos de Código y Patrones

### 6.1. Ejemplo de CRUD con DRF

Este ejemplo muestra un CRUD completo para un modelo `Curso` siguiendo las mejores prácticas de DRF.

```python
# models.py
from django.db import models

class Curso(models.Model):
  titulo = models.CharField(max_length=120)
  publicado = models.BooleanField(default=False)
  creado_en = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:  # Representación útil en admin / shell
    return self.titulo

# serializers.py
from rest_framework import serializers
from .models import Curso

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = ["id", "titulo", "publicado", "creado_en"]
    read_only_fields = ["id", "creado_en"]

# views.py
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Curso
from .serializers import CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
  """
  API endpoint que permite ver, crear, editar y eliminar Cursos.
  Soporta filtrado por el campo `publicado`.
  """
  queryset = Curso.objects.all().order_by("-creado_en")
  serializer_class = CursoSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ["publicado"]  # Permite filtrar con ?publicado=true

# urls.py (de la app)
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet

router = DefaultRouter()
router.register(r"cursos", CursoViewSet, basename="curso")

urlpatterns = router.urls
```

**Puntos didácticos del ejemplo:**

- `ModelViewSet` reduce el código repetitivo (boilerplate) para un CRUD completo.
- `filterset_fields` habilita el filtrado a través de la URL sin código adicional.
- `read_only_fields` protege campos que no deben ser modificados por el cliente.
- El orden explícito del `queryset` (`order_by`) evita resultados no deterministas.

### 6.1.1. Guía pragmática de Métodos HTTP para el curso

- **POST** para crear nuevos recursos.
- **PATCH** para modificaciones parciales de recursos existentes.
- **PUT** solo si se gestiona un reemplazo completo y coherente del recurso.
- Evitar duplicar semántica (no tener a la vez PATCH y acciones POST que hagan el mismo ajuste).

### 6.2. Documentación de API con `drf-spectacular`

Herramienta que genera documentación OpenAPI 3.0 (Swagger UI / Redoc) de forma automática a partir de tus ViewSets, serializers y rutas.

1.  `pip install drf-spectacular`
2.  Añadir `'drf_spectacular'` a `INSTALLED_APPS`.
3.  Configurar `REST_FRAMEWORK` en `settings.py`:
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }
    SPECTACULAR_SETTINGS = {
        "TITLE": "API del Curso",
        "DESCRIPTION": "Documentación interactiva de la API",
        "VERSION": "1.0.0",
    }
    ```
4.  Añadir las rutas de la documentación en el `urls.py` del proyecto.

    ```python
    # urls.py (proyecto)
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

    urlpatterns = [
        # ... otras rutas ...
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        # UI Interactivas:
        path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
    ```

---

## 7. Glosario Rápido (DRF y Django)

- **Serializer:** Capa de transformación y validación. Convierte modelos de Django a JSON y viceversa.
- **ViewSet:** Agrupación de endpoints relacionados con un recurso (ej. CRUD de Cursos).
- **Router:** Generador automático de URLs para un ViewSet.
- **Servicio (Service):** Módulo o función que encapsula lógica de negocio compleja que no pertenece ni al modelo ni a la vista. Es un patrón para mantener el código limpio.
- **Permiso (Permission):** Clase que define si un usuario tiene autorización para realizar una acción.
- **Filtro (FilterSet):** Clase que define de forma declarativa cómo se pueden filtrar los querysets a través de parámetros en la URL.
- **Contrato:** Especificación de las entradas, salidas y errores esperados de una unidad de código (función, endpoint).

---

## 8. Apéndice: Chuleta de Comandos Específicos de Python

### Django y DRF

- **Crear proyecto:** `django-admin startproject <proyecto>`
- **Crear app:** `python manage.py startapp <app>`
- **Crear migraciones:** `python manage.py makemigrations`
- **Aplicar migraciones:** `python manage.py migrate`
- **Crear superusuario:** `python manage.py createsuperuser`
- **Recopilar estáticos para producción:** `python manage.py collectstatic`
- **Ocultar información sensible:** `pip install python-dotenv`
- **Nota de buenas prácticas:** Siempre encierra las variables de Django (`{{ ... }}`) dentro de etiquetas HTML como `<td>`, `<div>`, `<span>`, etc. Esto previene errores de formato y asegura que el formateador automático o el editor no mezclen bloques de plantilla con HTML, manteniendo la legibilidad y funcionalidad de tus archivos.

- **Shell de Django:** `python manage.py shell`

### 8.1.1. Comandos de Serializers (DRF)

Los **serializers** permiten transformar la data en JSON. En la shell de Django, se pueden usar estos comandos para probarlos:

```bash
from <nombre_de_tu_app>.serializers import <TuModelo>Serializer
data = {"campo1": "valor1", "campo2": "valor2"} # Datos de ejemplo
serializer = <TuModelo>Serializer(data=data)
serializer.is_valid() # Retorna True si los datos son válidos, False en caso contrario
```

Si `serializer.is_valid()` retorna `False`, puedes ver los errores con `serializer.errors`.

```bash
serializer.save() # Guarda el objeto si los datos son válidos
```

---

## 9. Arquitectura de Software en Python

Este apartado explora los modelos arquitectónicos comunes en el ecosistema Python, cuándo aplicarlos y cómo evolucionar la complejidad de un proyecto.

### 9.1. MVT (Modelo-Vista-Template) en Django

Es el patrón fundamental de Django:

- **Modelo (Model):** Define la estructura de los datos y la lógica de negocio mínima relacionada con la persistencia.
- **Vista (View):** Orquesta la lógica de la petición y la respuesta. En DRF, las vistas (o ViewSets) manejan las peticiones HTTP y utilizan serializers.
- **Template (Template):** Se encarga de la renderización de la interfaz de usuario. En APIs, esta capa es reemplazada en gran parte por los Serializers que transforman los datos a formatos como JSON.

### 9.2. MVT vs MVC (Modelo-Vista-Controlador)

- El **Controlador** en MVC es análogo a la **Vista** de Django.
- La **Vista** de MVC es análoga al **Template** en Django.
- Los **Serializers** en DRF añaden una capa adicional que no es estándar en el MVC tradicional, enfocada en la transformación y validación de datos para APIs.

### 9.3. Capa de Servicios

Una abstracción para encapsular lógica de negocio compleja que no encaja naturalmente en modelos o serializers sin sobrecargarlos.

- **Beneficios:** Facilita los tests unitarios aislados y simplifica la refactorización hacia arquitecturas más limpias.

### 9.4. Arquitectura Hexagonal (Ports & Adapters)

**Objetivo:** Desacoplar el dominio de la aplicación de la infraestructura.

- Se introducen **Puertos** (interfaces) que el dominio define, y **Adaptadores** (implementaciones) que la infraestructura provee (ej. bases de datos, APIs externas, colas de mensajes).
- **Cuándo usarla:** Cuando existen múltiples fuentes/destinos de datos, se necesita testear el dominio puro sin dependencias externas, o se prevé la sustitución de proveedores (ej. cambiar de motor de búsqueda o caché).

### 9.5. Clean Architecture

Un enfoque más estricto que la Hexagonal, con capas concéntricas (Entidades → Casos de Uso → Interfaces).

- **Propósito:** Similar a la Hexagonal, enfatiza la independencia de frameworks y bases de datos.
- **Consideración:** Puede ser una sobre-ingeniería para un CRUD educativo inicial.

### 9.6. Domain-Driven Design (DDD)

Un enfoque para software complejo que se centra en el dominio del negocio.

- **Conceptos clave:** Lenguaje ubicuo, agregados, value objects.
- **Beneficios:** Emergen cuando se gestionan invariantes no triviales y reglas transaccionales ricas.

### 9.7. CQRS (Command Query Responsibility Segregation)

Separa los modelos para leer datos (Queries) de los modelos para escribir datos (Commands).

- **Cuándo usarlo:** Aplazar hasta que el volumen de queries/commands lo justifique, ya que complica la sincronización.

### 9.8. Guía de Adopción Progresiva

1.  Comenzar con una arquitectura simple (ej. MVT + serializers limpios).
2.  Extraer lógica de negocio a una **Capa de Servicios** cuando las vistas o controladores crezcan demasiado.
3.  Introducir **Puertos y Adaptadores** (Hexagonal) si el sistema necesita interactuar con múltiples tecnologías externas (diferentes BDs, APIs, etc.).
4.  Considerar patrones **DDD** si aparecen invariantes complejas (consistencia agregada, reglas multi-entidad).

- **Regla general:** Diferir la complejidad arquitectónica hasta tener un caso real que la justifique. Documentar el motivo de cada salto de abstracción.

---

## 10. Apéndice: Catálogo de Patrones de Diseño

Para una descripción detallada de los patrones de diseño (Creacionales, Estructurales, Comportamiento), consulta la sección "5. Catálogo de Patrones de Diseño" en el archivo `buenas-practicas.md`.

---

## 11. Apéndice: Chuleta de Comandos Adicionales

(Esta sección se mantiene igual que en la versión anterior, ya que los patrones son conceptuales pero muy aplicables en Python)

### 7.1. Creacionales

### 11.1. Estructurales

### 11.2. Comportamiento

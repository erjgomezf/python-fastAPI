# 📘 Buenas Prácticas y Chuleta Evolutiva

Documento vivo para acumular principios, patrones, comandos y referencias técnicas mientras avanzo en el aprendizaje de programación (Python, Django, Django REST, fundamentos frontend y diseño de software). No contiene reglas de interacción; sólo conocimiento reutilizable.

---

## 1. Filosofía y Principios de Backend (Python)

Nuestra base es el código limpio y el diseño sólido. Estos son nuestros pilares innegociables.

### 1.1. Principios SOLID

- **S - Responsabilidad Única (SRP):** Cada componente (clase, función) tiene una sola razón para cambiar.
- **O - Abierto/Cerrado (OCP):** Abiertos a la extensión, pero cerrados a la modificación.
- **L - Sustitución de Liskov (LSP):** Las subclases deben ser sustituibles por sus superclases sin alterar la lógica.
- **I - Segregación de Interfaces (ISP):** Interfaces pequeñas y específicas. No obligar a los clientes a depender de métodos que no usan.
- **D - Inversión de Dependencias (DIP):** Los módulos de alto nivel dependen de abstracciones, no de módulos de bajo nivel.

### 1.2. Herramientas y Patrones Clave en Python3

- **Inyección de Dependencias (DI):** Aplicación práctica del DIP para lograr un código desacoplado, flexible y testeable.
- **Abstracciones con `typing.Protocol` (Preferencia) y `abc.ABC`:** Para definir contratos claros y aplicar DIP y LSP de forma pythónica.
- **Modelado y Validación con Pydantic:** Para crear modelos de datos seguros, auto-documentados y con validación en tiempo de ejecución.
- **Estilo y Legibilidad:** Adhesión estricta a **PEP 8** y uso intensivo de **Tipado Estático (`type hints`)** para claridad y detección temprana de errores.

---

## 2. Principios de Frontend (Visión a Futuro)

Aunque nuestro foco inicial es el backend, sentaremos las bases para un frontend de calidad con estos principios:

- **Separación de Responsabilidades:**
  - **HTML:** Para la estructura y el contenido semántico.
  - **CSS:** Para el estilo visual y la presentación.
  - **JavaScript:** Para la interactividad y el comportamiento dinámico.
- **Diseño Adaptable (Responsive Design):** Pensaremos en cómo se ven y funcionan nuestras aplicaciones en diferentes dispositivos, desde móviles hasta escritorios.
- **Accesibilidad (A11y):** construiremos aplicaciones que puedan ser utilizadas por el mayor número de personas posible, incluyendo aquellas con discapacidades.
- **Componentización:** Empezaremos a pensar en la interfaz de usuario como un conjunto de bloques reutilizables, una idea clave en los frameworks modernos.

---

## 3. Ciclo de Desarrollo Recomendado (Técnico)

1. Análisis del problema y criterios de aceptación claros.
2. Diseño ligero: modelos de datos + contratos (Protocols / Pydantic) antes de lógica compleja.
3. TDD/BDD básico: test que falla → implementación mínima → refactor.
4. Revisión técnica (legibilidad, acoplamiento, duplicación, naming).
5. Definition of Done: código funcionando + tests pasando + sin deuda evidente inmediata.

---

## 4. Calidad y Mantenimiento Técnico

- Revisar acoplamientos: priorizar composición sobre herencia innecesaria.
- Refactorizar duplicaciones (regla de 3 repeticiones).
- Nombrado: semántico, evitar abreviaturas opacas.
- Commits: un concepto por commit, mensaje imperativo claro.
- Evitar “comentarios de excusa”; si el código necesita explicación extensa, reconsiderar la implementación.

### 4.1. Comentarios y Docstrings Estructurados

- **Propósito:** Escribir docstrings que no solo sean legibles para humanos, sino también interpretables por herramientas automáticas (como asistentes de código o generadores de documentación).
- **Formato recomendado (estilo reStructuredText/Sphinx simplificado):**

  - Usar comillas triples `'''Docstring aquí'''`.
  - Una descripción breve en la primera línea.
  - Usar `*` para definir secciones claras como `* Atributos:`, `* Métodos:`, `* Parámetros:`.
  - Usar `-` para listar los elementos dentro de cada sección.

- **Ejemplo práctico:**

  ```python
  class MiVista(APIView):
      '''Vista para gestionar los perfiles de usuario.'''
  ```

## 5. Estrategia de Validación

- Tests de unidad para lógica pura y transformaciones (serializers, helpers, servicios).
- Tests de integración para endpoints (status + payload clave + permisos mínimos).
- Usar factories / fixtures simples (no sobre-ingeniería temprana).
- Prioridad a escenarios edge: campos obligatorios faltantes, tipos incorrectos, ausencia de permisos.
- **Validaciones a nivel de Serializer:** Centralizar todas las validaciones de datos (nivel de campo, nivel de objeto) en los archivos `serializers.py`. Esto mantiene la lógica de validación contenida y reutilizable, asegurando que ninguna data inválida llegue a los modelos o la lógica de negocio.
- **Permisos Personalizados en `permissions.py`:** Para lógicas de autorización complejas o reutilizables, crear un archivo `permissions.py` dentro de la app de Django. Definir clases de permisos personalizadas que hereden de `BasePermission` para verificar si un usuario tiene derecho a ejecutar una acción sobre una vista. Esto mantiene las vistas limpias y la lógica de permisos centralizada.

## 6. Evolución de Esquemas y Migraciones

- Crear migraciones atómicas y claramente nombradas.
- Nunca modificar una migración aplicada en remoto: generar nueva migración correctiva.
- Documentar en el PR si una migración puede afectar tiempo de bloqueo (índices grandes, operaciones de columna).

## 7. Observabilidad Básica (a futuro)

- Logging estructurado (INFO para flujo normal, WARNING para condiciones anómalas, ERROR para excepciones no recuperables).
- Evitar logs de datos sensibles (tokens, contraseñas, identificadores personales).

## 8. Checklist mental previa a abrir PR

1. ¿El nombre de la rama describe la intención? (ej: `feature/curso-endpoint`)
2. ¿Existe al menos 1 test por ruta/escenario principal?
3. ¿Pasó formateo y linter? (`black .`)
4. ¿No introduje dependencias sin justificar?
5. ¿El diff muestra sólo lo relacionado?

## 9. Glosario rápido

- Serializer: capa de validación + transformación entre modelo y representación externa.
- ViewSet: agrupación de endpoints CRUD de un recurso.
- FilterSet: definición declarativa de filtros reutilizables.
- Servicio (service): función/módulo aislado que encapsula lógica de negocio no trivial.
- Contrato: especificación breve de entradas/salidas/errores de una unidad.

## 10. Futuras secciones previstas (placeholders)

- Capa de caché y políticas de invalidación (pendiente necesidad real).
- Mejores prácticas de CI/CD (una vez se integre pipeline).
- Estrategias de versionado de API (cuando existan breaking changes).

  <!-- (Se reserva bloque para ejemplos futuros de código Python) -->

## 11. Ejemplo mínimo DRF (Serializer + ViewSet + Router)

```python
# models.py
from django.db import models

class Curso(models.Model):
  titulo = models.CharField(max_length=120)
  publicado = models.BooleanField(default=False)
  creado_en = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:  # representación útil en admin / shell
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

class CursoViewSet(viewsets.ModelViewSet):
  queryset = Curso.objects.all().order_by("-creado_en")
  serializer_class = CursoSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ["publicado"]  # filtros declarativos simples

# urls.py (de la app o central)
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet

router = DefaultRouter()
router.register(r"cursos", CursoViewSet, basename="curso")

urlpatterns = router.urls
```

Puntos didácticos del ejemplo:

- `ModelViewSet` reduce boilerplate para CRUD completo.
- `filterset_fields` habilita filtrado sin código adicional.
- `read_only_fields` protege campos inmutables en creación/actualización.
- Orden de queryset explícito evita resultados no deterministas en tests.

## 12. Errores HTTP típicos en la API

| Código | Uso en este curso                                      | Ejemplo de disparador      |
| ------ | ------------------------------------------------------ | -------------------------- |
| 200    | Lecturas exitosas (GET detail)                         | GET /cursos/1/             |
| 201    | Creación exitosa                                       | POST /cursos/              |
| 204    | Eliminación sin cuerpo                                 | DELETE /cursos/1/          |
| 400    | Validación de datos fallida                            | Campo obligatorio faltante |
| 401    | No autenticado (cuando se añada auth)                  | Token ausente              |
| 403    | Autenticado pero sin permiso                           | Rol sin acceso             |
| 404    | Recurso no encontrado                                  | ID inexistente             |
| 409    | Conflicto lógico (evitar duplicados o estado inválido) | Ej. publicar dos veces     |
| 500    | Error no controlado                                    | Excepción no capturada     |

Reglas: usar el código más específico; no envolver respuesta en claves arbitrarias tipo `{"success":true}` salvo estándar global.

## 13. Herramientas para la API

### 13.1. Pruebas manuales con Postman

- Postman permite probar endpoints REST, guardar colecciones y automatizar pruebas manuales.
- Útil para:
  - Probar rutas protegidas (añadir headers, tokens, etc.).
  - Inspeccionar respuestas y errores de validación.
  - Extraer código cURL: botón "Code" > copiar como cURL para reproducir peticiones en terminal o scripts.
  - Documentar ejemplos de requests para el equipo.
- Buenas prácticas:
  - Nombrar cada request con verbo y recurso (`GET cursos`, `POST reservas`).
  - Guardar variables de entorno (host, tokens) para evitar hardcodear.
  - Versionar la colección si evoluciona la API.

### 13.2. Documentación automática con drf-spectacular

- `drf-spectacular` genera documentación OpenAPI 3.0 interactiva (Swagger UI, Redoc) a partir de tus serializers y rutas DRF.
- Permite explorar y probar endpoints desde el navegador, útil para frontend y QA.

#### Instalación y setup básico

1. Añadir a `requirements.txt` y luego `pip install -r requirements.txt`: `drf-spectacular`
2. En `settings.py`:

   ```python
   INSTALLED_APPS += ["drf_spectacular"]

   REST_FRAMEWORK = {
      # ...otras settings...
      "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
   }
   SPECTACULAR_SETTINGS = {
      "TITLE": "API del Curso DRF",
      "DESCRIPTION": "Documentación interactiva de la API",
      "VERSION": "1.0.0",
   }
   ```

3. En `urls.py` del proyecto, añadir las rutas para la UI:

   ```python
   # urls.py (proyecto)
   from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

   urlpatterns = [
       # ... otras rutas ...
       path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
       path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
       path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
   ]
   ```

4. Acceder a la documentación en:
   - Swagger UI: `http://localhost:8000/api/docs/`
   - Redoc: `http://localhost:8000/api/redoc/`

## 14. Métodos HTTP (referencia para APIs REST)

Tabla de referencia centrada en semántica, idempotencia y uso esperado en el curso.

| Método  | Seguro (Safe) | Idempotente                                                  | Body habitual  | Semántica principal           | Ejemplo endpoint  | Notas                                                             |
| ------- | ------------- | ------------------------------------------------------------ | -------------- | ----------------------------- | ----------------- | ----------------------------------------------------------------- |
| GET     | Sí            | Sí                                                           | No (se ignora) | Lectura / listado             | GET /cursos/      | No modifica estado; cacheable.                                    |
| HEAD    | Sí            | Sí                                                           | No             | Metadatos                     | HEAD /cursos/1/   | Igual a GET sin cuerpo.                                           |
| OPTIONS | Sí            | Sí                                                           | No             | Capacidades                   | OPTIONS /cursos/  | DRF puede generarlo automáticamente.                              |
| POST    | No            | No                                                           | Sí             | Crear / acción no idempotente | POST /cursos/     | Repetir puede duplicar.                                           |
| PUT     | No            | Sí                                                           | Sí             | Reemplazo completo            | PUT /cursos/5/    | Enviar representación completa (estado final).                    |
| PATCH   | No            | No (a veces tratado como idempotente si parche determinista) | Sí             | Actualización parcial         | PATCH /cursos/5/  | Preferir para cambios puntuales.                                  |
| DELETE  | No            | Sí                                                           | No             | Eliminación                   | DELETE /cursos/5/ | Repetir DELETE sobre recurso inexistente típicamente retorna 404. |

Notas clave:

- Safe ≠ Idempotente: GET es ambos; POST no es ninguno.
- Idempotencia: PUT y DELETE deben producir el mismo resultado tras múltiples ejecuciones.
- Evitar usar GET para operaciones mutantes (violación de semántica y caching).
- Acciones custom: preferir POST a `/recurso/{id}/accion/` o usar `@action` de DRF con métodos adecuados.

Guía pragmática para el curso:

- POST para crear; PATCH para modificaciones parciales; PUT sólo si se gestiona un reemplazo completo coherente.
- Evitar duplicar semántica (no tener a la vez PATCH y acciones POST que hagan el mismo ajuste).

## 15. Convenciones de Naming

| Código | Uso en este curso                                      | Ejemplo de disparador      |
| ------ | ------------------------------------------------------ | -------------------------- |
| 200    | Lecturas exitosas (GET detail)                         | GET /cursos/1/             |
| 201    | Creación exitosa                                       | POST /cursos/              |
| 204    | Eliminación sin cuerpo                                 | DELETE /cursos/1/          |
| 400    | Validación de datos fallida                            | Campo obligatorio faltante |
| 401    | No autenticado (cuando se añada auth)                  | Token ausente              |
| 403    | Autenticado pero sin permiso                           | Rol sin acceso             |
| 404    | Recurso no encontrado                                  | ID inexistente             |
| 409    | Conflicto lógico (evitar duplicados o estado inválido) | Ej. publicar dos veces     |
| 500    | Error no controlado                                    | Excepción no capturada     |

Reglas: usar el código más específico; no envolver respuesta en claves arbitrarias tipo `{"success":true}` salvo estándar global.

| Tipo        | Convención                                  | Ejemplo                   |
| ----------- | ------------------------------------------- | ------------------------- |
| Modelos     | Singular PascalCase                         | Curso, UsuarioPerfil      |
| Serializers | PascalCase + Sufijo Serializer              | CursoSerializer           |
| ViewSets    | PascalCase + Sufijo ViewSet                 | CursoViewSet              |
| Campos bool | prefijo `es_` / `tiene_` / adjetivo directo | publicado, es_activo      |
| Rutas       | plural snake / kebab según contexto         | cursos, cursos-publicados |
| Funciones   | snake_case descriptivo                      | generar_token_reset       |
| Tests       | prefijo test\_ + verbo/condición            | test_crea_curso_ok        |

Principio: el nombre debe comunicar intención sin necesitar comentario adicional.

## 16. Modelos Arquitectónicos en el Ecosistema Python

Si el archivo crece demasiado:

- Mover comandos a `docs/comandos.md`.
- Mover patrones a `docs/patrones.md`.
- Mantener este archivo como índice curado.

Para modularizar: crear carpeta `docs/`, añadir índice al inicio aquí con enlaces relativos y anotar en cada subarchivo fecha de última revisión.

Panorama de modelos y cuándo importan. Mantener simplicidad mientras no haya complejidad real de dominio.

### 16.1. MVT (Django)

Modelo–Vista–Template. En Django:

- Model: persistencia y lógica mínima relacionada a datos.
- View: orquestación de request/response.
- Template: renderización (en APIs reemplazado en gran parte por Serializers + Response JSON).

### 16.2. MVT vs MVC

- Controller en MVC ≈ View de Django.
- View de MVC ≈ Template en Django.
- Serializers añaden una capa no estándar de MVC tradicional (transformación y validación específica de API).

### 16.3. Capa de Servicios

Abstracción fina para lógica de negocio que no encaja en serializer ni en modelo sin sobrecargar. Beneficios: test unitarios aislados y facilita refactor hacia arquitecturas más limpias.

### 16.4. Arquitectura Hexagonal (Ports & Adapters)

Objetivo: desacoplar dominio de infraestructura. Se introducen puertos (interfaces) y adaptadores (implementaciones: DB, APIs externas, colas). Útil cuando:

- Existen múltiples fuentes/destinos de datos.
- Necesidad de testear dominio puro sin DB.
- Sustitución de proveedor (ej. cambiar motor de búsqueda, cache) prevista.

### 16.5. Clean Architecture

Capas concéntricas (Entidades → Casos de Uso → Interfaces). Similar propósito a Hexagonal; énfasis en independencia de frameworks. Útil pero puede ser sobre-ing para un CRUD educativo inicial.

### 16.6. Domain-Driven Design (DDD)

Aplica cuando el dominio es complejo (ubiquitous language, agregados, value objects). Beneficios emergen cuando se gestionan invariantes no triviales y reglas transaccionales ricas.

### 16.7. CQRS (mención breve)

Separación de modelos de lectura y escritura. Aplazar hasta que el volumen de queries/commands lo justifique; complica sincronización.

### 16.8. Tabla comparativa (simplificada)

| Aspecto           | MVT (Django)                      | MVC Clásico             | Hexagonal / Clean                                       | Service Layer Simple              |
| ----------------- | --------------------------------- | ----------------------- | ------------------------------------------------------- | --------------------------------- |
| Enfoque principal | Productividad + convención        | Separación presentación | Aislar dominio de infraestructura                       | Extraer lógica reusable           |
| Serializers       | Capa añadida (API)                | No explícito            | En adaptadores / DTO                                    | Sí (interfaz entrada)             |
| Tests dominio     | Menos aislado si lógica en modelo | Medio                   | Muy aislado (puro)                                      | Fácil si servicios puros          |
| Curva complejidad | Baja                              | Media                   | Alta inicial                                            | Baja                              |
| Cuándo aplicar    | Inicio / CRUD educativo           | Apps web tradicionales  | Sistemas con reglas complejas / múltiples integraciones | Cuando modelos/serializers crecen |

### 16.9. Guía de adopción progresiva

1. Comenzar con MVT + serializers limpios.
2. Extraer servicios al crecer validaciones transversales.
3. Introducir puertos/adaptadores sólo ante dependencias externas múltiples.
4. Considerar patrones DDD si aparecen invariantes complejas (consistencia agregada, reglas multi-entidad).

Regla general: diferir complejidad arquitectónica hasta tener un caso real; documentar el motivo de cada salto de abstracción.

---

## 17. Modularización de Apéndices (futuro)

Si el archivo crece demasiado:

- Mover comandos a `docs/comandos.md`.
- Mover patrones a `docs/patrones.md`.
- Mantener este archivo como índice curado.

Para modularizar: crear carpeta `docs/`, añadir índice al inicio aquí con enlaces relativos y anotar en cada subarchivo fecha de última revisión

## Apéndice A: Guía Rápida de Comandos

### Despliegue de archivos estáticos en producción

- **Antes de subir a producción, ejecuta:**

```bash
  python manage.py collectstatic
```

Esto recopila todos los archivos estáticos (CSS, JS, imágenes) en una sola carpeta lista para servir desde el servidor web.

- **En `settings.py`, asegúrate de tener:**

```python
STATIC_ROOT = "static"
```

Así evitarás perder los estilos y archivos estáticos al desplegar tu proyecto en el servidor.

### Formateo de Código Python

- **Formatear todo el código automáticamente con Black (recomendado antes de pasar a producción):**

```bash
black .
```

_Esto asegura un estilo uniforme y elimina errores de formato en todos los archivos Python del proyecto._

_Esta sección es tu "chuleta" personal para memorizar y acceder rápidamente a los comandos más comunes._

### Entorno Virtual y Dependencias

- **Crear entorno virtual:** `python3 -m venv ~/.env/<nombre_entorno>`
- **Activar (Linux/macOS):** `source ~/.env/<nombre_entorno>/bin/activate`
- **Activar (Windows):** `.\env\Scripts\activate`
- **Desactivar entorno:** `deactivate`
- **Instalar dependencias de un archivo:** `pip install -r requirements.txt`
- **Guardar dependencias actuales en un archivo:** `pip freeze > requirements.txt`
- **Buscar paquetes instalados:** `pip list | grep <nombre_paquete>`

### Control de Versiones (Git)

- **Inicializar repositorio:** `git init`
- **Ver estado:** `git status`
- **Añadir todos los cambios:** `git add .`
- **Confirmar cambios:** `git commit -m "Mensaje descriptivo"`
- **Ver log compacto:** `git log --oneline --graph --decorate --all`
- **Crear y cambiar a una nueva rama:** `git checkout -b <nombre-rama>`

### Django

> **Nota de buenas prácticas:**
> Siempre encierra las variables de Django (`{{ ... }}`) dentro de etiquetas HTML como `<td>`, `<div>`, `<span>`, etc. Esto previene errores de formato y asegura que el formateador automático o el editor no mezclen bloques de plantilla con HTML, manteniendo la legibilidad y funcionalidad de tus archivos.

- **Crear un proyecto:** `django-admin startproject <proyecto>`
- **Iniciar el servidor:** `python3 manage.py runserver`
- **Crear una aplicación:** `python3 manage.py startapp <nombre_de_la_app>`
- **Crear migraciones:** `python3 manage.py makemigrations`
- **Aplicar migraciones:** `python3 manage.py migrate`
- **Crear un superusuario:** `python3 manage.py createsuperuser`
- **Shell de Django:** `python3 manage.py shell`
- **Libreria que actua como conectos de Django con el entorno virual de PostgreSQL:** `pip install psycopg2-binary`
- **Libreria que se utiliza para ocultar la informancion sensible del proyecto:** `pip install python-dotenv`

### APIRest

> Los **serializers** permiten transformar la data en json, en la shell se pueden usar estos comandos;

```bash
from modelo.serializers import ModeloSerializer
data = {"clave":"valor"}
serializer = ModeloSerializer(data=data)
serializer.is_valid()
```

> Si serializer.is_valid() = TRUE -> data esta bien definida / de lo contrario, ejecutar -> serializer.errors (para ver errores).

```bash
serializer.save()
```

### fastAPI

- **Para instalar:** `pip install fastapi`
- **Para instalar la version estandar de fastAPI:** `pip install "fastapi[standard]"`
- **Para ejecutar:** `uvicorn main:app --reload`
- **Para ejecutar modo dev:** `fastapi dev`

### Postman

> Se puede utilizar postman para verificar la funcionadidad de la Api\'s, ademas de que puede generar un codigo culs para ejecutar el comando por consola

### Testing

- **Ejecutar todas las pruebas con pytest:** `python3 -m pytest`
- **Descubrir y correr pruebas con unittest:** `python3 -m unittest discover tests`

### Docker y Docker Compose

- **Construir imágenes:** `docker-compose build`
- **Iniciar servicios (en segundo plano):** `docker-compose up -d`
- **Detener y eliminar contenedores:** `docker-compose down`
- **Ver logs:** `docker-compose logs`
- **Entrar a un contenedor:** `docker-compose exec <nombre-servicio> bash`

---

## Apéndice B: Catálogo de Patrones de Diseño

_Referencia rápida para identificar y aplicar soluciones probadas a problemas comunes._

### Patrones Creacionales

| Patrón               | Propósito Principal                                                | Cuándo Usarlo (Casos de Uso)                                                            |
| :------------------- | :----------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **Singleton**        | Garantizar una única instancia de una clase.                       | Controlar el acceso a un recurso único (ej. conexión a BD, gestor de configuración).    |
| **Factory Method**   | Delegar la creación de objetos a subclases.                        | Crear un objeto sin especificar la clase exacta.                                        |
| **Abstract Factory** | Crear familias de objetos relacionados.                            | Producir conjuntos de objetos que deben funcionar juntos (ej. UI para Windows y macOS). |
| **Builder**          | Construir un objeto complejo paso a paso.                          | Separar la construcción de la representación final.                                     |
| **Prototype**        | Clonar un objeto pre-configurado para evitar una creación costosa. | Copiar un objeto existente.                                                             |

### Patrones Estructurales

| Patrón        | Intención Principal                                | Foco                                                         |
| :------------ | :------------------------------------------------- | :----------------------------------------------------------- |
| **Adapter**   | Convertir una interfaz en otra.                    | Hacer que dos cosas incompatibles funcionen juntas.          |
| **Bridge**    | Desacoplar abstracción de implementación.          | Dividir una jerarquía en dos independientes.                 |
| **Composite** | Tratar a un grupo de objetos como a uno solo.      | Construir jerarquías de parte-todo.                          |
| **Decorator** | Añadir comportamiento a un objeto dinámicamente.   | Envolver un objeto para darle nuevas funcionalidades.        |
| **Facade**    | Simplificar la interfaz de un subsistema complejo. | Ocultar la complejidad interna.                              |
| **Flyweight** | Ahorrar memoria compartiendo estado.               | Optimizar el uso de recursos para un gran número de objetos. |
| **Proxy**     | Controlar el acceso a un objeto.                   | Actuar como un intermediario.                                |

### Patrones de Comportamiento

| Patrón                      | Intención Principal                                     | Foco                                           |
| :-------------------------- | :------------------------------------------------------ | :--------------------------------------------- |
| **Strategy**                | Encapsular algoritmos intercambiables.                  | Cómo un objeto realiza una tarea.              |
| **State**                   | Cambiar el comportamiento de un objeto según su estado. | Qué puede hacer un objeto en su estado actual. |
| **Mediator**                | Centralizar la comunicación entre objetos.              | Cómo colabora un grupo de objetos.             |
| **Command**                 | Encapsular una acción en un objeto.                     | Convertir una operación en un objeto portable. |
| **Observer**                | Notificar a múltiples objetos sobre un cambio.          | Mantener a los objetos sincronizados.          |
| **Chain of Responsibility** | Pasar una solicitud por una cadena de manejadores.      | Desacoplar quién envía de quién recibe.        |

## 18. Seguridad y Rendimiento

### 18.1. Limitar Peticiones con Throttling

El "throttling" (o limitación de velocidad) es una herramienta crucial para proteger tu API contra ataques de Denegación de Servicio (DoS) y abuso por parte de usuarios que realizan demasiadas peticiones en un corto período de tiempo. Django REST Framework ofrece un sistema de throttling flexible y fácil de configurar.

#### ¿Por qué usar Throttling?

- **Prevenir Abuso:** Evita que un solo usuario (o una IP) sature el servidor con peticiones, ya sea de forma malintencionada o por un error en un script.
- **Garantizar Disponibilidad:** Asegura que la API siga siendo accesible para todos los usuarios al evitar que un pico de tráfico la sobrecargue.
- **Controlar el Consumo de Recursos:** Limita el uso de CPU, memoria y ancho de banda.

#### Configuración en Django REST Framework

La forma más común de configurar el throttling es de manera global en tu archivo `settings.py`.

1. **Define las clases de throttling y los límites:**

   En `settings.py`, dentro del diccionario `REST_FRAMEWORK`, puedes establecer una política de throttling por defecto.

   ```python
   # doctorapp/settings.py

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

2. **Personalización por Vista:**

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

#### Tipos de `Throttle`

- **`AnonRateThrottle`**: Limita las peticiones de usuarios no autenticados. Usa la dirección IP para identificar al cliente.
- **`UserRateThrottle`**: Limita las peticiones de usuarios autenticados. Usa el `user.id` para identificar al cliente.
- **`ScopedRateThrottle`**: Permite definir límites específicos para ciertas vistas. Requiere que asignes un `throttle_scope` en la vista.

**Ejemplo con `ScopedRateThrottle`:**

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'contact': '5/hour', # Límite para el scope 'contact'
        'upload': '10/day',  # Límite para el scope 'upload'
    }
}

# views.py
class ContactoView(APIView):
    throttle_scope = 'contact'
    # ...

class SubirArchivoView(APIView):
    throttle_scope = 'upload'
    # ...
```

Al aplicar estas políticas, si un usuario excede el límite de peticiones, recibirá una respuesta `HTTP 429 Too Many Requests` con un mensaje indicando cuándo podrá volver a realizar una petición.

---

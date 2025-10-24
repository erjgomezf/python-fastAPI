# 📘 Buenas Prácticas de Ingeniería de Software y Chuleta General

Documento vivo para acumular principios, patrones, comandos y referencias técnicas multilinguaje para el desarrollo de software.

---

## 1. Principios Fundamentales de Diseño (SOLID)

Estos principios son la base para construir software robusto, mantenible y escalable, independientemente del lenguaje.

- **S - Responsabilidad Única (SRP):** Cada componente (clase, función, módulo) debe tener una sola razón para cambiar.
- **O - Abierto/Cerrado (OCP):** El software debe estar abierto a la extensión, pero cerrado a la modificación.
- **L - Sustitución de Liskov (LSP):** Las subclases deben ser sustituibles por sus superclases sin alterar la lógica del programa.
- **I - Segregación de Interfaces (ISP):** Es preferible tener muchas interfaces pequeñas y específicas que una grande y monolítica.
- **D - Inversión de Dependencias (DIP):** Los módulos de alto nivel no deben depender de los de bajo nivel. Ambos deben depender de abstracciones.

---

## 2. Principios de Desarrollo por Capa

### 2.1. Backend

- **Diseño de APIs:** Prefiere APIs RESTful o GraphQL consistentes. Usa los códigos de estado HTTP y los métodos (verbos) correctamente.
- **Stateless:** Las APIs deben ser sin estado siempre que sea posible. Cada petición debe contener toda la información necesaria para ser procesada.
- **Seguridad:** Valida y sanea toda la entrada del usuario. Usa mecanismos de autenticación y autorización robustos. No expongas información sensible en los logs o mensajes de error.
- **Observabilidad:** Implementa logging estructurado, métricas y tracing para entender el comportamiento de la aplicación en producción.

### 2.2. Frontend

- **Separación de Responsabilidades:**
  - **HTML:** Para la estructura y el contenido semántico.
  - **CSS:** Para el estilo visual y la presentación.
  - **JavaScript:** Para la interactividad y el comportamiento dinámico.
- **Diseño Adaptable (Responsive Design):** Asegura que la aplicación se vea y funcione bien en todos los dispositivos.
- **Accesibilidad (A11y):** Construye aplicaciones que puedan ser utilizadas por el mayor número de personas posible.
- **Componentización:** Piensa en la UI como un conjunto de bloques reutilizables e independientes.
- **Observabilidad:** Implementa logging estructurado (INFO para flujo normal, WARNING para condiciones anómalas, ERROR para excepciones no recuperables). Evita logs de datos sensibles (tokens, contraseñas, identificadores personales).

### 2.3. Base de Datos

- **Migraciones Atómicas:** Cada migración debe representar un cambio de esquema pequeño y reversible. Nómbralas de forma clara.
- **Nunca modifiques migraciones aplicadas:** Si una migración ya está en producción o en ramas compartidas, crea una nueva migración para corregirla o revertirla.
- **Índices:** Añade índices a las columnas que se usan frecuentemente en filtros (`WHERE`), uniones (`JOIN`) y ordenamiento (`ORDER BY`) para optimizar el rendimiento de las consultas.
- **Evita N+1:** Utiliza técnicas como `JOIN` (o `select_related` / `prefetch_related` en ORMs como Django) para cargar datos relacionados en una sola consulta en lugar de N consultas adicionales dentro de un bucle.

---

## 3. Calidad, Mantenimiento y Ciclo de Vida

- **Composición sobre Herencia:** Prefiere componer objetos a partir de otros más simples en lugar de crear complejas jerarquías de herencia.
- **No te repitas (DRY - Don't Repeat Yourself):** Evita la duplicación de código. Abstrae y reutiliza la lógica común.
- **Nombrado Semántico:** Usa nombres de variables, funciones y clases que sean descriptivos y revelen su intención.
- **Commits Atómicos:** Cada commit en el control de versiones debe representar un cambio lógico y completo. Escribe mensajes de commit claros.
- **Evita comentarios de excusa:** Si el código necesita una explicación extensa, considera refactorizarlo para que sea más claro.
- **Checklist Pre-PR (Pull Request):**
  - ¿El nombre de la rama describe la intención? (ej. `feature/user-authentication`)
  - ¿El código nuevo tiene tests que cubren el "happy path" y al menos un caso de error?
  - ¿Se ha ejecutado el formateador de código y el linter?
  - ¿El `diff` muestra solo los cambios relacionados con la tarea?
  - ¿Se ha actualizado la documentación si es necesario?

### 3.1. Ciclo de Desarrollo Recomendado

1.  **Análisis:** Criterios de aceptación claros.
2.  **Diseño Ligero:** Definir modelos de datos y contratos (interfaces) antes de la lógica compleja.
3.  **Implementación Guiada por Pruebas (TDD/BDD):** Escribir un test que falle -> implementar el código mínimo para que pase -> refactorizar.
4.  **Revisión Técnica:** Evaluar legibilidad, acoplamiento, duplicación y nombrado.

---

## 4. Arquitectura de Software

Patrones para organizar la estructura de una aplicación a gran escala.

- **Arquitectura en Capas:** Separa la aplicación en capas horizontales (Presentación, Lógica de Negocio, Acceso a Datos).
- **Arquitectura Hexagonal (Puertos y Adaptadores):** Desacopla el núcleo de la aplicación (dominio) de la infraestructura (frameworks, BDs). El dominio define "puertos" (interfaces) y la infraestructura provee "adaptadores" (implementaciones).
- **Clean Architecture:** Un enfoque más estricto que la Hexagonal, con capas concéntricas (Entidades -> Casos de Uso -> Adaptadores de Interfaz -> Frameworks). La regla principal es que las dependencias solo apuntan hacia adentro.
- **Microservicios:** Descompone una aplicación grande en un conjunto de servicios pequeños, independientes y débilmente acoplados que se comunican a través de APIs.
- **Domain-Driven Design (DDD):** Un enfoque para software complejo que se centra en el dominio del negocio, usando un lenguaje ubicuo compartido entre desarrolladores y expertos del dominio.
- **CQRS (Command Query Responsibility Segregation):** Separa los modelos para leer datos (Queries) de los modelos para escribir datos (Commands). Útil para sistemas con altos volúmenes de lectura o escritura.

### 4.1. Estrategia de Adopción Progresiva

1.  Comenzar con una arquitectura simple (ej. Capas o MVT en Django).
2.  Extraer lógica de negocio a una **Capa de Servicios** cuando las vistas o controladores crezcan demasiado.
3.  Introducir **Puertos y Adaptadores** (Hexagonal) si el sistema necesita interactuar con múltiples tecnologías externas (diferentes BDs, APIs, etc.).

### 4.1. Métodos HTTP (Referencia para APIs REST)

| Método  | Seguro (Safe) | Idempotente                                                  | Body habitual  | Semántica principal           |
| ------- | ------------- | ------------------------------------------------------------ | -------------- | ----------------------------- |
| GET     | Sí            | Sí                                                           | No (se ignora) | Lectura / listado             |
| POST    | No            | No                                                           | Sí             | Crear / acción no idempotente |
| PUT     | No            | Sí                                                           | Sí             | Reemplazo completo            |
| PATCH   | No            | No (a veces tratado como idempotente si parche determinista) | Sí             | Actualización parcial         |
| DELETE  | No            | Sí                                                           | No             | Eliminación                   |
| HEAD    | Sí            | Sí                                                           | No             | Metadatos (GET sin cuerpo)    |
| OPTIONS | Sí            | Sí                                                           | No             | Capacidades del servidor      |

**Notas clave:**

- **Idempotencia:** Una operación es idempotente si realizarla una o N veces produce el mismo resultado (ej. `DELETE /users/1`). `POST` no es idempotente, ya que llamarlo N veces crearía N recursos.
- **Seguridad (Safe):** Un método es seguro si no modifica el estado del servidor. `GET` y `HEAD` son seguros.

### 4.2. Códigos de Estado HTTP Comunes en APIs

| Código | Significado       | Cuándo usarlo                                                     |
| ------ | ----------------- | ----------------------------------------------------------------- |
| 200    | OK                | Peticiones `GET` exitosas.                                        |
| 201    | Created           | Creación de un recurso exitosa (`POST`).                          |
| 204    | No Content        | Petición exitosa sin contenido que devolver (`DELETE`).           |
| 400    | Bad Request       | Error del cliente (ej. JSON malformado, datos inválidos).         |
| 401    | Unauthorized      | El cliente no está autenticado.                                   |
| 403    | Forbidden         | El cliente está autenticado pero no tiene permisos.               |
| 404    | Not Found         | El recurso solicitado no existe.                                  |
| 409    | Conflict          | Conflicto con el estado actual del recurso (ej. email duplicado). |
| 429    | Too Many Requests | El cliente ha excedido el límite de peticiones (throttling).      |

- **Reglas:** Usa el código más específico. No envuelvas la respuesta en claves arbitrarias tipo `{"success":true}` salvo que el proyecto defina un estándar global.

---

## 5. Catálogo de Patrones de Diseño

Soluciones probadas a problemas comunes de diseño de software.

### 5.1. Creacionales

- **Singleton:** Garantiza una única instancia de una clase.
- **Factory Method:** Delega la creación de objetos a subclases.
- **Builder:** Construye un objeto complejo paso a paso.

### 5.2. Estructurales

- **Adapter:** Convierte una interfaz en otra para que clases incompatibles puedan trabajar juntas.
- **Decorator:** Añade funcionalidades a un objeto dinámicamente.
- **Facade:** Proporciona una interfaz simplificada a un subsistema complejo.
- **Proxy:** Proporciona un sustituto o intermediario para otro objeto para controlar el acceso a él.

### 5.3. Comportamiento

- **Strategy:** Permite definir una familia de algoritmos, poner cada uno de ellos en una clase separada y hacer sus objetos intercambiables.
- **Observer:** Permite definir un mecanismo de suscripción para notificar a múltiples objetos sobre cualquier evento que le suceda al objeto que están observando.
- **Command:** Convierte una solicitud en un objeto independiente que contiene toda la información sobre la solicitud.

---

## 6. Apéndice: Chuleta de Comandos

### 6.1. Control de Versiones (Git)

- **Inicializar repositorio:** `git init`
- **Ver estado:** `git status`
- **Añadir todos los cambios:** `git add .`
- **Confirmar cambios:** `git commit -m "feat: Mensaje descriptivo"`
- **Ver log compacto:** `git log --oneline --graph --decorate --all`
- **Crear y cambiar a una nueva rama:** `git checkout -b <nombre-rama>`
- **Cambiar de rama:** `git checkout <nombre-rama>`
- **Fusionar rama actual con otra:** `git merge <otra-rama>`

### 6.2. Contenedores (Docker & Docker Compose)

- **Construir imágenes:** `docker-compose build`
- **Iniciar servicios (en segundo plano):** `docker-compose up -d`
- **Detener servicios:** `docker-compose stop`
- **Detener y eliminar contenedores:** `docker-compose down`
- **Ver logs de un servicio:** `docker-compose logs -f <nombre-servicio>`
- **Entrar a un contenedor:** `docker-compose exec <nombre-servicio> bash`
- **Listar contenedores en ejecución:** `docker ps`

### 6.3. Herramientas de API

- **cURL:**
  - **Petición GET:** `curl https://api.example.com/resource`
  - **Petición POST con JSON:** `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com/resource`
  - **Con Header de Autorización:** `curl -H "Authorization: Bearer <token>" https://api.example.com/resource`
- **Postman:** Herramienta gráfica para probar y documentar APIs. Permite guardar colecciones de peticiones y generar código en diferentes lenguajes.

### 6.4. Testing

- **Ejecutar todas las pruebas con pytest:** `pytest`
- **Descubrir y correr pruebas con unittest:** `python -m unittest discover tests`

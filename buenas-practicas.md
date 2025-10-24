# 📘 Buenas Prácticas de Programación y Chuleta General

Documento vivo para acumular principios, patrones, comandos y referencias técnicas multilinguaje para el desarrollo de software.

---

## 1. Principios Fundamentales de Diseño

Estos principios son la base para construir software robusto, mantenible y escalable, independientemente del lenguaje.

- **S - Responsabilidad Única (SRP):** Cada componente (clase, función, módulo) debe tener una sola razón para cambiar.
- **O - Abierto/Cerrado (OCP):** El software debe estar abierto a la extensión, pero cerrado a la modificación.
- **L - Sustitución de Liskov (LSP):** Las subclases deben ser sustituibles por sus superclases sin alterar la lógica del programa.
- **I - Segregación de Interfaces (ISP):** Es preferible tener muchas interfaces pequeñas y específicas que una grande y monolítica.
- **D - Inversión de Dependencias (DIP):** Los módulos de alto nivel no deben depender de los de bajo nivel. Ambos deben depender de abstracciones.

---

## 2. Principios de Desarrollo General

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

---

## 3. Calidad y Mantenimiento

- **Composición sobre Herencia:** Prefiere componer objetos a partir de otros más simples en lugar de crear complejas jerarquías de herencia.
- **No te repitas (DRY - Don't Repeat Yourself):** Evita la duplicación de código. Abstrae y reutiliza la lógica común.
- **Nombrado Semántico:** Usa nombres de variables, funciones y clases que sean descriptivos y revelen su intención.
- **Commits Atómicos:** Cada commit en el control de versiones debe representar un cambio lógico y completo. Escribe mensajes de commit claros.

---

## 4. Arquitectura de Software

Patrones para organizar la estructura de una aplicación a gran escala.

- **Arquitectura en Capas:** Separa la aplicación en capas horizontales (Presentación, Lógica de Negocio, Acceso a Datos).
- **Arquitectura Hexagonal (Puertos y Adaptadores):** Desacopla el núcleo de la aplicación (dominio) de la infraestructura (frameworks, BDs). El dominio define "puertos" (interfaces) y la infraestructura provee "adaptadores" (implementaciones).
- **Clean Architecture:** Un enfoque más estricto que la Hexagonal, con capas concéntricas (Entidades -> Casos de Uso -> Adaptadores de Interfaz -> Frameworks). La regla principal es que las dependencias solo apuntan hacia adentro.
- **Microservicios:** Descompone una aplicación grande en un conjunto de servicios pequeños, independientes y débilmente acoplados que se comunican a través de APIs.

---

## 5. Catálogo de Patrones de Diseño

Soluciones probadas a problemas comunes de diseño de software.

### 5.1. Creacionales
*   **Singleton:** Garantiza una única instancia de una clase.
*   **Factory Method:** Delega la creación de objetos a subclases.
*   **Builder:** Construye un objeto complejo paso a paso.

### 5.2. Estructurales
*   **Adapter:** Convierte una interfaz en otra para que clases incompatibles puedan trabajar juntas.
*   **Decorator:** Añade funcionalidades a un objeto dinámicamente.
*   **Facade:** Proporciona una interfaz simplificada a un subsistema complejo.
*   **Proxy:** Proporciona un sustituto o intermediario para otro objeto para controlar el acceso a él.

### 5.3. Comportamiento
*   **Strategy:** Permite definir una familia de algoritmos, poner cada uno de ellos en una clase separada y hacer sus objetos intercambiables.
*   **Observer:** Permite definir un mecanismo de suscripción para notificar a múltiples objetos sobre cualquier evento que le suceda al objeto que están observando.
*   **Command:** Convierte una solicitud en un objeto independiente que contiene toda la información sobre la solicitud.

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
# .github/copilot-instructions.md — Guía Evolutiva para Agentes (Curso Django REST Framework)

Estado: vivo / incremental. Este documento instruye a cualquier agente de IA sobre CÓMO interactuar productivamente en este repositorio orientado al aprendizaje práctico de Django REST Framework (DRF). Mantenerlo concreto, accionable y sin “ruido de plantilla genérica”.

## 1. Propósito y Alcance

Este repo sirve como sandbox educativo para construir APIs REST con Django + DRF aplicando principios de diseño limpio (SOLID, separación de capas y contratos explícitos). Toda contribución del agente debe:

- Acelerar el aprendizaje (explicar decisiones brevemente cuando introduzca algo nuevo).
- Mantener coherencia arquitectónica y consistencia de estilos.
- Evitar introducir complejidad sin un caso de uso actual o inminente.

## 2. Panorama Arquitectónico (esperado)

- Núcleo: Django (configuración en `settings.py`), DRF para la capa de presentación API.
- Dominio típico por app: `models.py` (persistencia), `serializers.py` (transformación / validación), `views.py` o `viewsets.py` (endpoints), `urls.py` (enrutado local), registro global en `project/urls.py` vía `routers.DefaultRouter`.
- Filtros: usar `django-filter` integrándolo en ViewSets (atributo `filterset_fields` o clases `FilterSet`).
- Paginación: central en `REST_FRAMEWORK` de `settings.py` (no redefinir por endpoint salvo justificación).
- Autenticación/Permisos: usar clases DRF estándar (por ejemplo `IsAuthenticated`) antes de crear permisos custom.

## 3. Patrones y Decisiones Clave

- Preferir ViewSets + Routers sobre funciones o APIViews manuales para CRUD estándar.
- Añadir lógica de negocio fuera de los serializers cuando exceda validación (crear un servicio/helper antes de inflar un serializer).
- Evitar lógica de dominio en señales si puede expresarse de forma explícita en servicios transaccionales.
- Orden sugerido al crear una nueva funcionalidad:
  1.  Definir modelo (si falta)
  2.  Serializer mínimo
  3.  ViewSet + ruta
  4.  Pruebas (lista + creación + detalle + error)
  5.  Refinar (filtros, paginación, permisos, documentación breve)

## 4. Estándares de Código y Estilo

- Idioma: español en comentarios / docstrings; inglés permitido sólo para nombres técnicos ampliamente aceptados.
- Formato: `black .` antes de finalizar cambios sustanciales.
- Tipado: añadir `type hints` (mínimo en firmas públicas). No forzar tipado redundante obvio (`def save(self) -> None:` es aceptable; no tipar atributos triviales duplicados).
- Imports: agrupar (stdlib / terceros / locales). Evitar comodines.
- Plantillas: envolver expresiones `{{ ... }}` dentro de etiquetas HTML para mitigar conflictos de formateo.

## 5. Flujo de Trabajo Operativo (para el agente)

1. Lectura contextual: revisar `requirements.txt`, `settings.py`, `urls.py` y archivos de la app objetivo antes de proponer cambios.
2. Contrato: en tareas no triviales, anotar mini-contrato (entradas, salidas, éxito, errores esperados) + 1–3 TODOs secuenciales.
3. Batches: agrupar hasta 3–5 acciones (lecturas/ediciones); antes de cada batch declarar propósito y resultado esperado.
4. Validación mínima tras editar código ejecutable: formateo, (cuando existan) tests base y arranque rápido de servidor si procede.
5. Iterar: máximo 3 intentos de corrección antes de solicitar aclaración.

## 6. Respuestas del Agente (estructura recomendada)

Preambulo | Acciones | Archivos cambiados | Cómo probar | Verificaciones (Build/Lint/Tests/Smoke) | Requisitos (Done/Deferred) | Notas/Futuros.
Mantener cada bloque conciso (ideal: ≤4 bullets). Explicar razonamientos sólo cuando añaden claridad o introducen un nuevo patrón.

## 7. Pruebas (Enfoque Pedagógico)

- Añadir pruebas mínimas representativas (happy path + 1 error). Evitar suites masivas si aún no se justifica.
- Prioridad inicial: endpoints CRUD (status codes, estructura de respuesta, validaciones básicas).
- Si no existen tests todavía, sugerir carpeta `tests/` y crear un primer archivo `tests/test_<recurso>.py` con un ejemplo.

## 8. Manejo de Datos y Validación

- Validaciones simples: en serializers (`validate_<field>` o `validate`).
- Validaciones cruzadas / composición: método de servicio separado (`services/<nombre>.py`).
- Evitar crear un “God Serializer”: cuando la validación se infle, extraer reglas a funciones puras testeables.

## 9. Errores y Respuestas API

- Usar códigos HTTP semánticos (`400` validación, `404` inexistente, `403` permiso, `409` conflicto lógico, `500` inesperado no atrapado).
- No crear envoltorios JSON arbitrarios (“success”, “data”) salvo que el proyecto defina un estándar global.

## 10. Filtros, Orden y Paginación

- Filtros declarativos vía `filterset_fields = ["campo"]` o `FilterSet` dedicado si la lógica escala.
- Ordenación: permitir `ordering` param si aporta valor; documentar campos seguros.
- Paginación: centralizada; cambiar a nivel de vista sólo con justificación explícita (p.ej. feed público vs. panel interno).

## 11. Seguridad y Buenas Prácticas

- No exponer datos sensibles (tokens, contraseñas) en logs / respuestas.
- Antes de introducir dependencias nuevas: justificar (beneficio > coste cognitivo).
- Nada de credenciales hardcodeadas; usar `.env` (si se agrega, documentar claves mínimas requeridas).

## 12. Rendimiento (Umbral Inicial)

- Optimización mayor sólo tras detectar necesidad real (consultas repetitivas, N+1 evidente). Sugerir `select_related` / `prefetch_related` cuando corresponda.
- Evitar premature caching; si se menciona, proponerlo como “próximo paso opcional”.

## 13. Comunicación y Clarificaciones

- Si falta contexto esencial (archivo crítico inexistente, ambigüedad de dominio), inferir 1 supuesto razonable y continuar; si el riesgo > beneficio, preguntar.
- Evitar preguntas retóricas; cada pregunta debe desbloquear una decisión clara.

## 14. DO / DON'T del Agente

DO:

- Explicar sucintamente cuando introduces una abstracción nueva.
- Mantener cambios acotados al objetivo declarado.
- Sugerir micro-mejoras seguras (añadir type hints, docstring breve, test mínimo) tras cumplir el requerimiento principal.
  DON'T:
- Reescribir archivos completos sin necesidad.
- Introducir frameworks externos para tareas triviales.
- Fabricar endpoints no solicitados.

## 15. Evolución de Este Documento

- Añadir nuevas secciones sólo cuando emerja un patrón repetido o fricción recurrente.
- Registrar cambios significativos al inicio (Changelog breve). Ej.: `2025-09-25: +Secciones rendimiento y validación cruzada.`
- Mantener enfoque: guía de interacción + decisiones arquitectónicas actuales; no convertirlo en manual teórico extenso.

## 16. Plantilla Rápida para Creación de Nuevo Recurso (ejemplo abstracto)

1. Modelo (si procede).
2. Serializer mínimo (campos explícitos).
3. ViewSet (`ModelViewSet` si CRUD completo).
4. Router (`router.register("recurso", RecursoViewSet)`).
5. Test básico (listar + crear + validación errónea).
6. Añadir filtros y permisos si aplica.
7. Revisión/refactor.

## 17. Estructura de Commit Sugerida

Mensaje en español, modo imperativo: `Añade ViewSet de Curso con filtros básicos`.
Si incluye breaking change educativo, añadir nota: `BREAKING: cambia nombre de campo '...'`.

## 18. Herramientas Mentales para el Curso

- “Menos es más”: implementar lo mínimo demostrable primero.
- “Extraer antes que duplicar grande”: si repites un bloque ≥3 veces, factoriza.
- “Errores hablan”: usa el primer test que falla como brújula antes de refactorizar más.

## 19. Formato de Respuesta del Agente (Ejemplo literal)

```
Preambulo: Implementaré el ViewSet de Cursos; primero crearé serializer y registraré en router.
Acciones: creado serializer, viewset, registro en urls, test inicial.
Archivos: app/cursos/serializers.py (nuevo) — define CursoSerializer; app/cursos/views.py — añade CursoViewSet; project/urls.py — registra ruta.
Cómo probar: (pytest) ; listar endpoint /api/cursos/.
Verificaciones: Build PASS / Lint PASS / Tests PASS / Smoke PASS.
Requisitos: CRUD básico Done; filtros Deferred (no requeridos aún).
Notas: sugerido añadir permisos IsAuthenticated en próxima iteración.
Cierre: recurso expuesto y probado mínimamente.
```

## 20. Referencias Locales

- `requirements.txt`: dependencias base (Django 5, djangorestframework, django-filter, Markdown).
- `copilot-instructions.md` (raíz): documento extenso con filosofía y apéndices (consultar para profundidad conceptual).

— Fin versión 2025-09-25 —

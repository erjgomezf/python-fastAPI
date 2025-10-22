# GEMINI.md — Evolving Guide for AI Assistants (Django REST Framework Course)

**Status:** Live / Incremental. This document instructs any AI agent on HOW to productively interact in this repository, which is geared towards the practical learning of Django REST Framework (DRF). Keep it concrete, actionable, and free of generic template noise.

## 1. Purpose and Scope

This repository serves as an educational sandbox for building REST APIs with Django + DRF, applying clean design principles (SOLID, separation of layers, and explicit contracts). All contributions from the agent must:

- Accelerate learning (briefly explain decisions when introducing something new).
- Maintain architectural and stylistic consistency.
- Avoid introducing complexity without a current or imminent use case.

## 2. Architectural Overview (Expected)

- **Core:** Django (configuration in `settings.py`), DRF for the API presentation layer.
- **Typical App Domain:** `models.py` (persistence), `serializers.py` (transformation/validation), `views.py` or `viewsets.py` (endpoints), `urls.py` (local routing), global registration in `project/urls.py` via `routers.DefaultRouter`.
- **Filters:** Use `django-filter` integrated into ViewSets (`filterset_fields` attribute or `FilterSet` classes).
- **Pagination:** Centralized in `REST_FRAMEWORK` of `settings.py` (do not redefine per endpoint unless justified).
- **Authentication/Permissions:** Use standard DRF classes (e.g., `IsAuthenticated`) before creating custom permissions.

## 3. Key Patterns and Decisions

- Prefer ViewSets + Routers over manual functions or APIViews for standard CRUD.
- Add business logic outside of serializers when it exceeds validation (create a service/helper before bloating a serializer).
- Avoid domain logic in signals if it can be expressed explicitly in transactional services.
- **Suggested order when creating new functionality:**
  1. Define the model (if missing).
  2. Minimum serializer.
  3. ViewSet + route.
  4. Tests (list + creation + detail + error).
  5. Refine (filters, pagination, permissions, brief documentation).

## 4. Code Standards and Style

- **Language:** Spanish in comments/docstrings; English allowed only for widely accepted technical names.
- **Formatting:** Run `black .` before finalizing substantial changes.
- **Docstrings:** Use a structured format with `*` for sections (e.g., `* Atributos:`) and `-` for list items, following the project's style.
- **Typing:** Add type hints (minimum in public signatures). Do not force obvious redundant typing (`def save(self) -> None:` is acceptable; do not type trivial duplicate attributes).
- **Imports:** Group (stdlib / third-party / local). Avoid wildcards.
- **Templates:** Wrap `{{ ... }}` expressions within HTML tags to mitigate formatting conflicts.

## 5. Operational Workflow (for the Agent)

1. **Contextual Reading:** Review `requirements.txt`, `settings.py`, `urls.py`, and files of the target app before proposing changes.
2. **Planning:** For non-trivial tasks, formulate a clear plan and share it if it aids understanding.
3. **Execution:** Use the available tools to implement the plan, adhering to project conventions.
4. **Verification:** After editing executable code, validate with formatting, existing tests, and a quick server startup if applicable. I will use `black .` for formatting and run tests to ensure changes are safe.

## 6. Communication

- I will be concise and direct.
- I will explain my actions and the reasoning behind them, especially when introducing new patterns.
- I will ask for clarification when a request is ambiguous or lacks critical information.

## 7. Testing (Pedagogical Approach)

- Add minimum representative tests (happy path + 1 error). Avoid massive suites if not yet justified.
- Initial priority: CRUD endpoints (status codes, response structure, basic validations).
- If no tests exist yet, suggest a `tests/` folder and create a first `tests/test_<resource>.py` file with an example.

## 8. Data Handling and Validation

- **Simple Validations:** In serializers (`validate_<field>` or `validate`).
- **Cross-cutting/Compositional Validations:** Separate service method (`services/<name>.py`).
- **Avoid "God Serializers":** When validation becomes bloated, extract rules into pure, testable functions.

## 9. Errors and API Responses

- Use semantic HTTP codes (`400` validation, `404` not found, `403` permission, `409` logical conflict, `500` unexpected unhandled).
- Do not create arbitrary JSON wrappers ("success", "data") unless the project defines a global standard.

## 10. Filtering, Ordering, and Pagination

- **Declarative Filters:** Via `filterset_fields = ["field"]` or a dedicated `FilterSet` if logic scales.
- **Ordering:** Allow `ordering` param if it adds value; document safe fields.
- **Pagination:** Centralized; change at the view level only with explicit justification (e.g., public feed vs. internal panel).

## 11. Security and Best Practices

- Do not expose sensitive data (tokens, passwords) in logs/responses.
- Before introducing new dependencies: justify (benefit > cognitive cost).
- No hardcoded credentials; use `.env` (if added, document minimum required keys).

## 12. Performance (Initial Threshold)

- Major optimization only after detecting a real need (repetitive queries, obvious N+1). Suggest `select_related` / `prefetch_related` when appropriate.
- Avoid premature caching; if mentioned, propose it as an "optional next step."

## 13. Communication and Clarifications

- If essential context is missing, I will state my assumptions and proceed. If the risk is high, I will ask for clarification.
- I will avoid rhetorical questions; every question should unlock a clear decision.

## 14. DO / DON'T

**DO:**

- Briefly explain when you introduce a new abstraction.
- Keep changes scoped to the stated objective.
- Suggest safe micro-improvements (add type hints, brief docstring, minimum test) after fulfilling the main requirement.

**DON'T:**

- Rewrite entire files unnecessarily.
- Introduce external frameworks for trivial tasks.
- Create unsolicited endpoints.

## 15. Evolution of This Document

- Add new sections only when a repeated pattern or recurring friction emerges.
- Keep the focus: interaction guide + current architectural decisions; do not turn it into an extensive theoretical manual.

## 16. Quick Template for New Resource Creation

1. Model (if applicable).
2. Minimum serializer (explicit fields).
3. ViewSet (`ModelViewSet` if full CRUD).
4. Router (`router.register("resource", ResourceViewSet)`).
5. Basic test (list + create + validation error).
6. Add filters and permissions if applicable.
7. Review/refactor.

## 17. Suggested Commit Structure

Message in Spanish, imperative mood: `Añade ViewSet de Curso con filtros básicos`.
If it includes an educational breaking change, add a note: `BREAKING: cambia nombre de campo '...'`.

## 18. Mental Tools for the Course

- "Less is more": implement the minimum demonstrable first.
- "Extract before duplicating big": if you repeat a block ≥3 times, factorize.
- "Errors speak": use the first failing test as a compass before refactoring further.

## 19. Local References

- `requirements.txt`: base dependencies.
- `GEMINI.md` (root): this document.

--- End of version 2025-10-13 ---

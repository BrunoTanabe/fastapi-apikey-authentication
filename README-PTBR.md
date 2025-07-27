
**FastAPI API Key Blueprint**

### Short summary (Markdown supported)

Example FastAPI app showing **API Key** auth via `Header`, `Query`, or `Cookie`, using dependency injection, optional scopes, and reusable OpenAPI security components.

### Detailed application description (Markdown)

```markdown
## Overview

This example demonstrates **API Key authentication** in a FastAPI application. It focuses on practical patterns you can reuse in real projects:
- Keys passed via **HTTP header** (`X-API-Key`), **query** (`api_key`), or **cookie** (`api_key`)
- Centralized, dependency-based auth with clear error handling
- Optional **scopes** for coarse-grained authorization
- Reusable OpenAPI `securitySchemes` and operation-level security
- Simple tests and structure you can extend

## How it works

1. Clients send an API key using one of the supported transports:
   - Header: `X-API-Key: <key>`
   - Query: `GET /resource?api_key=<key>`
   - Cookie: `api_key=<key>`

2. A security dependency extracts the key, validates it (e.g., against env/config or a store), and optionally checks scopes.

3. Protected routes declare the dependency and (optionally) their required scopes.

## Endpoints

- `GET /health` — public health check  
- `GET /secure` — requires a valid API key  
- `GET /secure/{item_id}` — secure route example with path params

## Configuration

- Default header name: `X-API-Key`  
- Default query param: `api_key`  
- Default cookie name: `api_key`  
- Expected environment variable(s): `API_KEY` (and optionally `API_KEY_SCOPES`)

You can adapt names and validation logic to your environment (files, DB, secrets manager).

## Error responses

- `401 Unauthorized` — missing or invalid API key  
- `403 Forbidden` — key is valid but lacks required scopes (if enabled)

## Testing & local run

- **Run**: `uvicorn app.main:app --reload`  
- **Tests**: `pytest`  
- The OpenAPI UI is available at `/docs` and `/redoc`.

## Notes

This example is intentionally minimal and aims to teach patterns for real-world use. For production, consider rotation, hashing, rate limiting, logging, and storage in a secure secrets backend.
```

---

## Application Metadata

### `pyproject.toml` description

A minimal, well-documented FastAPI application that demonstrates API Key authentication via header, query, and cookie, with dependency-based validation, optional scopes, reusable OpenAPI security components, and tests for easy reuse in real projects.

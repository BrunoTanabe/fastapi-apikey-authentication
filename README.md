# FastAPI API Key Authentication

[![Python](https://img.shields.io/badge/python-3.13-blue.svg?logo=python\&logoColor=white)](#-requirements)
[![FastAPI](https://img.shields.io/badge/fastapi-0.115.13-green.svg?logo=fastapi\&logoColor=white)](#-key-technologies-used)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg?logo=docker\&logoColor=white)](https://www.docker.com/)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg?logo=github\&logoColor=white)](#-how-to-run-the-project-locally)
[![Docs](https://img.shields.io/badge/docs-Swagger-informational.svg?logo=swagger\&logoColor=white)](#-available-endpoints)

> **FastAPI application example with API Key authentication – Python Backend Template**

**FastAPI API Key Authentication** is a **100% Python** backend *template* project that demonstrates how to implement simple **API Key** authentication in a REST API built with FastAPI. Following **Clean Architecture** and **Domain-Driven Design (DDD)** principles, the project provides a modern structural foundation for secure and scalable applications.

Aimed at **beginner to advanced** developers, the template offers:

* **Security out of the box**: API Key authentication (via customizable header) already integrated into protected routes.
* **Organized architecture**: clear separation between *core* (infrastructure) and *domain modules*, making maintenance and growth easier.
* **Automatic documentation**: Swagger (OpenAPI) interface available to quickly test and integrate endpoints.
* **Built-in best practices**: Pydantic v2 validation, structured logging (Loguru), standardized responses, and pre-configuration for Docker and tests.

Below you’ll find a complete guide to installation, usage, and contribution. Enjoy!

---

## 📑 Table of Contents

* [1. General Description](#-general-description)

  * [1.1 What it does 🚀](#what-it-does-)
  * [1.2 Problem it solves 💡](#problem-it-solves)
  * [1.3 Target Audience 🎯](#target-audience-)
  * [1.4 Highlights 🔥](#highlights)
* [2. Main Features](#-main-features)
* [3. Key Technologies Used](#-key-technologies-used)
* [4. Project Structure](#-project-structure)
* [5. Dependency Structure](#-dependency-structure)
* [6. Requirements](#-requirements)

  * [6.1 Software & Tools](#-software--tools)
  * [6.2 Project Dependencies](#-project-dependencies)
* [7. How to run the project locally](#-how-to-run-the-project-locally)

  * [7.1 Path A — Local environment with uv (recommended)](#path-a--local-environment-with-uv-recommended)
  * [7.2 Path B — Docker / Docker Compose](#path-b--docker--docker-compose)
* [8. Available Endpoints](#-available-endpoints)

  * [8.1 Authentication](#-authentication)
  * [8.2 Overview](#-overview)
  * [8.3 POST /api/v1/example/ — Operation Example](#1-post-apiv1example--operation-example)
  * [8.4 GET /healthz — Health Check](#2-get-healthz--health-check)
  * [8.5 GET / — Redirect to /docs](#3-get--redirect-to-docs)
  * [8.6 GET /docs & /redoc — Documentation](#4-get-docs--redoc--documentation)
* [9. Frequently Asked Questions (FAQ)](#-frequently-asked-questions-faq)
* [10. How to contribute](#-how-to-contribute)

  * [10.1 Contribution flow](#-contribution-flow)
  * [10.2 Branch & Commit Conventions](#-branch--commit-conventions)
  * [10.3 Code Quality & Style](#-code-quality--style)
  * [10.4 Environment Variables & Secrets](#-environment-variables--secrets)
  * [10.5 Pull Requests (PRs)](#-pull-requests-prs)
  * [10.6 Pre-PR Checklist](#-pre-pr-checklist)
* [11. License](#-license)
* [12. Authors](#-authors)

---

## 📝 General Description

**FastAPI API Key Authentication** is a sample application created to show, in practice, how to protect **FastAPI** API endpoints using an **API Key**. It serves as a starting point for building **microservices** or **internal APIs** that need a simple authentication layer without implementing full OAuth2 or JWT flows.

### What it does 🚀

1. **Validates** all requests hitting protected endpoints, ensuring they include a valid **API Key** header before running business logic.
2. **Demonstrates** a layered project structure (Clean Architecture), serving as a model for creating new endpoints and modules in a decoupled manner.
3. **Provides** standardized JSON responses, including metadata (HTTP code, path, timestamp) for both success and error cases, simplifying consumption and debugging.
4. **Documents** the API automatically using FastAPI’s **Swagger UI** (interactive interface available at `/docs`) for quick route testing.
5. **Includes** production-ready utilities like a *health check* endpoint (`/healthz`) for monitoring and easy environment configuration via a `.env` file.

### Problem it solves 💡

Many web applications must expose APIs quickly and securely, either for internal microservice consumption or for offering services to external clients. Implementing a simple authentication scheme from scratch can lead to security pitfalls (e.g., checks vulnerable to *timing attacks*) or to an unstructured architecture as the project grows.

This template addresses these challenges by:

* **Providing a minimalist, ready-to-use authentication solution** (API Key), avoiding the setup of OAuth2 or other methods when not needed.
* **Establishing an organized codebase**, enabling project evolution with well-defined modules without mixing business rules with infrastructure details.
* **Ensuring basic security** by using secure string comparison (`secrets.compare_digest`) and consistent error returns (401 with appropriate headers), aligned with HTTP best practices.

### Target Audience 🎯

| User Profile                         | What they gain from this project                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Backend Developers**               | A cohesive starting point to create structured, secure APIs with API Key.                                               |
| **Internal API Teams**               | A consistent model to standardize authentication between microservices and ensure only authorized services access data. |
| **FastAPI Beginners**                | A practical example of organizing a complex FastAPI project (multiple layers) cleanly, with integrated auth and docs.   |
| **Tech Leads / Software Architects** | A reference blueprint to spread best practices for structuring Python projects and deploying simple security measures.  |

### Highlights 🔥

* **Easy to Customize**: API Key header name and the key value itself are defined via `.env`, enabling quick adaptation to environments or security policies.
* **Global Auth via Dependency/Middleware**: All routes (except explicitly public ones) can be protected at once using global dependencies or middleware—making it easy to extend security to new endpoints.
* **Unified Standard Response**: A consistent response model (`StandardResponse`) wraps user data and metadata (status, method, etc.), simplifying logs and monitoring.
* **Docker-ready**: *Dockerfile* and *docker-compose* provided for containerized execution, speeding up local testing and deployments in standardized environments.
* **Fast Development Loop**: Hot-reload in development (Uvicorn or FastAPI CLI) and preconfigured lint/format (Ruff) for quick feedback and consistent code.
* **Test-ready**: Automated testing structure (Pytest) to make unit and integration testing straightforward as the project grows.

## ⚙️ Main Features

| #     | Feature                    | What it does                                                                                                   | Technical/Usability Differentials                                                                                                                |
|-------|----------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **1** | **API Key Authentication** | Restricts API access to requests presenting the correct key in the header.                                     | 🔐 Secure verification using `secrets.compare_digest` to prevent timing attacks. Customizable header (default: **X-API-Key**).                   |
| **2** | **Example Endpoint**       | Provides an illustrative route (e.g., `/api/v1/example/`) that can serve as a model for implementing features. | 🛠️ Practical application of **Clean Architecture** (layers for *domain*, *use case*, *presentation*) and **Pydantic** for data validation.      |
| **3** | **Health Check**           | Exposes a public `/healthz` endpoint for quick service checks (used by orchestrators, Kubernetes, etc.).       | ❤️ Follows the 12‑Factor App style; easily integrates with load balancers or uptime monitoring systems.                                          |
| **4** | **Interactive Docs**       | Offers Swagger/OpenAPI via `/docs` (Swagger UI) and `/redoc` (ReDoc).                                          | 📖 Test API calls directly in the browser, including providing the API Key through Swagger’s **Authorize** button.                               |
| **5** | **Standardized Responses** | All success/error responses follow a unified schema (`code`, `method`, `path`, `timestamp`, `details{...}`).   | 📊 Makes logging and auditing easier; clients and developers always handle a consistent response format.                                         |
| **6** | **Structured Logging**     | Logs each request with important info (execution time, status, origin) and `X-Request-ID` identification.      | 📑 Based on **Loguru** for JSON output; easy integration with observability tools (ELK, Graylog, etc.) and readable stack traces (Stackprinter). |

---

## 🧰 Key Technologies Used

| Technology              | Version         | Role in the Project                                                        | Why it was chosen                                                                                                     |
|-------------------------|-----------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Python**              | 3.13            | Main language; native async support.                                       | Vast ecosystem and simple syntax, plus performance improvements with each version.                                    |
| **FastAPI**             | 0.115.13        | ASGI web framework for building REST APIs.                                 | Excellent performance (comparable to Node.js and Go) and automatic documentation generation (Swagger UI).             |
| **Pydantic v2**         | 2.11.7          | Data modeling and validation (request/response models, configs).           | Declarative and fast validations (Rust core), ensuring reliable data in the API.                                      |
| **Uvicorn & Hypercorn** | 0.34.x / 0.17.3 | ASGI servers to run the app (Uvicorn in dev, Hypercorn optional for prod). | Modern features (HTTP/2, WebSockets); hot reload in dev and high performance in production.                           |
| **Orjson**              | 3.11.0          | Ultra-fast JSON serialization for HTTP responses.                          | Up to 3x faster than Python’s stdlib JSON, improving API latency.                                                     |
| **Loguru**              | 0.7.3           | Simple, structured logging.                                                | Friendly API, per-request formatting, flexible sinks (console, file, etc.).                                           |
| **Pydantic Settings**   | 2.10.1          | Read configs and secrets from `.env` or environment variables.             | Embraces *12-Factor* principles: configuration outside code with automatic type parsing.                              |
| **Pytest**              | 8.4.1 (dev)     | Testing framework.                                                         | Concise tests with fixtures; asyncio support makes testing FastAPI functions easy.                                    |
| **Ruff**                | 0.12.0 (dev)    | Python linter and formatter.                                               | Bundles dozens of checks (Flake8, Black-style formatting, etc.) in one ultra-fast tool for consistent code standards. |

> 🔒 **Dependency Security:** All versions are pinned in `requirements.txt` and `uv.lock` for reproducible builds. Only essential libraries are included to minimize attack surface and performance overhead.

## 🗂️ Project Structure

<details>
<summary><strong>🌳 Directory tree (simplified)</strong></summary>

```text
fastapi-apikey-authentication/
├── app/
│   ├── app.py               # Initializes the FastAPI instance and includes routes
│   ├── core/                # "Core" features (infrastructure & cross-cutting)
│   │   ├── security.py      # API Key auth logic (Dependency)
│   │   ├── middleware.py    # Response formatting and logging middleware
│   │   ├── exception_handler.py  # Global HTTP exception handling
│   │   ├── settings.py      # App configuration (Pydantic BaseSettings)
│   │   ├── schemas.py       # Reusable generic schemas (e.g., StandardResponse)
│   │   ├── exceptions.py    # Custom exceptions
│   │   ├── logging.py       # Loguru logger configuration
│   │   ├── resources.py     # Misc resources (e.g., error texts or constants)
│   │   └── utils.py         # General utilities
│   └── modules/             # Business modules (each folder is an isolated context)
│       ├── example/         # Example module (demonstration feature)
│       │   ├── domain/      # Business rules, entities, mappers (if applicable)
│       │   ├── application/ # Use cases (orchestration between domain and presentation)
│       │   └── presentation/ # Interface (FastAPI routers, request/response schemas, docs)
│       │       ├── routers.py       # Example endpoints/routes definition
│       │       ├── schemas.py       # Pydantic schemas for the example’s request/response
│       │       ├── dependencies.py  # Example-specific dependencies (injections)
│       │       ├── docs.py          # Descriptions & examples (used in OpenAPI) for the module
│       │       └── exceptions.py    # Example domain-specific exceptions
│       └── health/          # Health check module (system domain)
│           ├── application/ # (Could include subsystem checks if needed)
│           └── presentation/
│               ├── routers.py       # Health route (`/healthz`)
│               ├── schemas.py       # Health response schema (e.g., status)
│               ├── docs.py          # Health endpoint documentation
│               └── exceptions.py    # (n/a — health rarely needs custom exceptions)
├── .env.example            # Environment config example (copy to .env)
├── Dockerfile              # Build recipe for the app’s Docker image
├── docker-compose.yaml     # Defines service for local run (includes the app)
├── pyproject.toml          # Project metadata and dependencies (PEP 621)
├── requirements.txt        # Pinned (frozen) dependency list
├── uv.lock                 # Dependency lockfile (generated by uv)
├── scripts/
│   └── directory_tree.py   # Utility script to generate the directory tree
├── test/                   # Tests (unit/integration)
│   ├── core/               # (e.g., tests for core utilities)
│   └── modules/            # (e.g., tests for each business module)
└── README.md               # Main repository documentation
```

</details>

| Layer/Folder            | Responsibility/Role                                                                         | Details                                                                                                                                                                                                                      |
|-------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`app/app.py`**        | Initializes the FastAPI app, sets global definitions, and includes routes from all modules. | The application “entry point”. Imports each module’s routers and adds middlewares (such as global authentication, if configured).                                                                                            |
| **`app/core/`**         | Core module with reusable components and configurations spanning the whole project.         | Contains auth logic, response formatting, error capture, *12‑Factor* settings, and other utilities independent of business rules.                                                                                            |
| **`app/modules/`**      | Each subfolder represents an isolated **business context** (DDD).                           | Enables adding new domains/features without conflicting with existing ones. E.g., **example** (didactic) and **health** (systemic) modules.                                                                                  |
| **`.../presentation/`** | **Presentation** layer: where Clean Architecture controllers live (here, FastAPI routers).  | Defines endpoints, performs initial validation via Pydantic schemas, and returns responses using model classes. Also includes descriptions (docs.py) shown in Swagger UI.                                                    |
| **`.../application/`**  | **Application** layer: implements use cases or interactors.                                 | Orchestrates calls between presentation and domain layers. In the example module, it could process input data, call domain services, and shape the final response.                                                           |
| **`.../domain/`**       | **Domain** layer: business rules, entities, and repository contracts.                       | Ideally infrastructure-agnostic. In the example module, it holds classes/functions representing the core business logic. In larger templates, this is where repository interfaces and external service contracts would live. |
| **Config files**        | (root) `Dockerfile`, `docker-compose.yaml`, etc.                                            | Enable containerization and consistent execution across environments.                                                                                                                                                        |
| **`test/`**             | Automated test suite (initially illustrative).                                              | Makes it easy to expand coverage as features grow (e.g., authentication tests and example endpoint tests).                                                                                                                   |

> 🧩 **Note:** The layered structure (presentation, application, domain) doesn’t prevent an endpoint from calling logic directly, but it encourages separation of concerns. For simple features, the application layer can be minimal; for complex cases, this pattern helps keep code organized.

---

## 🧬 Dependency Structure

Project dependencies are managed via **pyproject.toml** (PEP 621) and a lockfile (`uv.lock`) for consistency. Below is an overview of key libraries and subcomponents:

```text
fastapi-apikey-authentication (template) v1.0.0
├─ fastapi[standard] v0.115.13
│   ├─ pydantic v2.11.7
│   ├─ starlette v0.46.2
│   ├─ email-validator, python-multipart, httpx, jinja2... (FastAPI extras)
│   └─ uvicorn[standard] v0.34.3 (web server + reload)
├─ hypercorn v0.17.3          (alternative ASGI server, e.g., for HTTP/2)
├─ loguru v0.7.3             (structured logging)
├─ orjson v3.11.0            (high‑performance JSON serialization)
├─ pydantic-settings v2.10.1 (BaseSettings-based configuration management)
├─ stackprinter v0.2.12      (readable traceback formatting)
├─ pytest v8.4.1 [dev]       (testing framework)
└─ ruff v0.12.0 [dev]        (all-in-one linter/formatter)
```

**Notes:**

* Packages marked `[dev]` are for development only, not required in production.
* FastAPI is installed with the `[standard]` extra, bundling useful tooling like uvicorn (server) and utilities (email-validator, jinja2, etc.) for faster prototyping.
* `requirements.txt` is generated from the lockfile and pins exact versions (ensuring all developers/environments use the same versions).
* There are no external DB or third-party auth dependencies—the goal is to keep it simple. If your use case requires integrations, add them as needed while keeping the modular organization.

---

## 🧾 Requirements

### 📦 Software & Tools

To run and develop this project, ensure you have:

| Item                     | Version / Notes                       |          Required?           | Description / Use                                                                                                                               |
|--------------------------|---------------------------------------|:----------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Python**               | >= 3.13 (compatible with 3.13+)       |              ✅               | Python interpreter to run the app. Newer versions ensure better performance and compatibility with Pydantic v2.                                 |
| **uv** (deps CLI)        | Latest stable (optional)              |              ⚠️              | Recommended dependency/venv manager. Eases venv creation and `uv.lock` sync. ([install](https://astral.sh/uv/))                                 |
| **Git**                  | Any recent version                    |              ✅               | Version control to clone the repo and manage source code.                                                                                       |
| **Docker** + **Compose** | Docker Engine 20+ / Docker Compose 2+ | ✔️ (for deploy) ⚠️ (for dev) | To run in containers (optional for dev but recommended to ensure environment parity).                                                           |
| **Editor/IDE**           | VSCode, PyCharm, etc. (suggested)     |              ✅               | A good editor boosts productivity. This project includes ready-to-use lint config (Ruff) that integrates with your editor for instant feedback. |

*Note:* Using **uv** (by Astral) is encouraged to simplify environment and dependency management (similar to `pipenv` or `poetry`). You can also use traditional *pip/venv*—just follow `requirements.txt`.

### 🔧 Project Dependencies

* **Main Libraries:** Already listed above (FastAPI, Pydantic, etc.). All installed via `pip` or `uv` from `pyproject.toml`.
* **Development Libraries:** Include `pytest` (to run tests) and `ruff` (lint/format). Not required in production but recommended during development to keep code quality high.
* **External Services:** None consumed in this app. Authentication is performed locally by comparing the provided key with the one configured in environment variables. If needed, integrate DBs or external APIs in new modules, following the template’s pattern.

### 🖥️ Environment Configuration

* **Environment Variables:** Rename `.env.example` to `.env` and set values as needed. Main parameters include:

  * `SECURITY_API_KEY_HEADER` – Header name that carries the API Key (default: `X-API-Key`).
  * `SECURITY_API_KEY` – The secret API Key value to accept. (Set a strong value in production; the example file contains a placeholder for development.)
  * Other parameters: (e.g., `LOG_LEVEL`, `APP_ENV`) as defined in `core/settings.py`, which may change logging behavior or environment-specific settings.
* **Application Port:** By default, the app runs on **8000** (see `docker-compose.yaml` and instructions below). You can change it with the `--port` flag or by adjusting the Docker Compose port mapping.
* **Debug Mode:** In development, **auto-reload** is enabled (when using uvicorn via `uv run` or `fastapi dev`). In production, disable debug and reload for better performance.

---

## ▶️ How to run the project locally

You can run the application locally in two ways: directly in a Python environment (ideal for development) or using Docker (useful to test in an isolated environment or produce a deployable image).

### Path A — **Local environment with uv (recommended)**

1. **Install `uv` (Astral’s env & deps manager):**

   * **Linux/macOS (via cURL):**

     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```
   * **Windows (PowerShell):**

     ```powershell
     iwr https://astral.sh/uv/install.ps1 -UseBasicParsing | iex
     ```

   *If you prefer, check the [official uv docs](https://github.com/astral-sh/uv) for alternative installation methods.*

2. **Clone this repository and move into the project folder:**

   ```bash
   git clone https://github.com/BrunoTanabe/fastapi-apikey-authentication.git
   cd fastapi-apikey-authentication
   ```

3. **Create a Python virtual environment:**

   ```bash
   uv venv .venv
   ```

   This creates a `.venv` at the project root. (Optionally, use `python -m venv .venv` and `source .venv/bin/activate` instead.)

4. **Install production dependencies:**

   ```bash
   uv sync
   ```

   This reads `pyproject.toml` and installs all specified dependencies, honoring versions pinned in `uv.lock`. You’ll get FastAPI, Uvicorn, and the rest.

5. **(Optional) Also install development dependencies:**

   ```bash
   uv sync --group dev
   ```

   This includes `pytest` and `ruff`. Not required to run the app, but useful for testing and maintaining code quality.

6. **Set environment variables:**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` with appropriate values. Set `SECURITY_API_KEY` to a secret token required to access protected endpoints. Keep `SECURITY_API_KEY_HEADER` as `X-API-Key` (or change if needed).

7. **Run the API in development (with hot-reload):**

   ```bash
   uv run uvicorn app.app:app --reload --port 8000 --host 0.0.0.0
   ```

   This starts Uvicorn with the FastAPI app (`app.app:app`, i.e., `app` object in `app/app.py`), enables auto-reload on file changes, and binds to port 8000 on all interfaces.

   Alternatively, use **FastAPI CLI** (installed via the `[standard]` extra):

   ```bash
   uv run fastapi dev app/app.py --port 8000
   ```

   Either way, your API will listen at `http://localhost:8000`.

8. **Open the interactive docs** to test:
   Go to [http://localhost:8000/docs](http://localhost:8000/docs). You’ll see Swagger UI to try endpoints. Click **Authorize** and supply the API Key from your `.env` to call protected routes.

> 💡 **Tip:** `uv run ...` ensures the lockfile is synced before execution, avoiding version drift. If you don’t use `uv`, you can run `uvicorn app.app:app --reload --port 8000` after installing dependencies with `pip install -r requirements.txt`.

---

### Path B — **Docker / Docker Compose**

If you prefer, or for production purposes, run the app in a Docker container:

1. **Ensure Docker is installed** and the daemon is running.

2. **Build the Docker image:**
   From the project root:

   ```bash
   docker build -t fastapi-apikey-auth .
   ```

   Uses the provided `Dockerfile` to package the app. The image is named `fastapi-apikey-auth`.

3. **Run the container:**

   ```bash
   docker run --rm -p 8000:8000 --env-file .env fastapi-apikey-auth
   ```

   This:

   * Publishes container port 8000 to host 8000.
   * Loads environment variables from your local `.env` (ensuring the API Key and other configs are available inside the container).
   * Uses the image you built above.
   * `--rm` removes the container after exit.

4. **(Optional) Use Docker Compose for development:**
   A `docker-compose.yaml` is provided. It builds the image and exposes port 8000. Just run:

   ```bash
   docker-compose up --build
   ```

   The `api` service maps `8000:8000` and mounts the project directory for live reload. Feel free to tweak `docker-compose.yaml` (e.g., volumes or commands).

5. **Open Swagger and test:**
   With the container running, go to [http://localhost:8000/docs](http://localhost:8000/docs) to confirm everything works inside the container. Routes and authentication should behave the same as locally.

> 🐳 **Tip:** The image is based on slim Python, containing only project deps (thanks to `requirements.txt`). For a smaller image, consider multi-stage builds or Alpine/Python base. Also, configure secrets via CI/CD or orchestrators instead of hardcoding in the Dockerfile.

---

## 🔌 Available Endpoints

> Generally, all API responses (success and error) follow the **`StandardResponse`** schema. It includes fields like `code`, `method`, `path`, and `timestamp`, plus a `details` object containing actual results or error messages—providing uniform info for logging and client handling.

### 🔐 Authentication

API Key authentication works as follows in this project:

* All “protected” routes require a specific HTTP header, whose default name is defined in `SECURITY_API_KEY_HEADER` (in `.env`). By default, we use **`X-API-Key`**.
* The header value must match the key set in the `SECURITY_API_KEY` environment variable.
* If the key is missing or incorrect:

  * The API returns **HTTP 401 Unauthorized**, with an error JSON indicating invalid credentials.
  * The `WWW-Authenticate` header is included in the response, as recommended by HTTP for API credentials (though not Basic/Bearer, it indicates authentication is required).
* Certain endpoints remain open by design: typically Swagger `/docs`, `/openapi.json`, and health check `/healthz`. This allows checking status or documentation without a key.

### 📋 Overview

Main endpoints provided by this project:

| Method   | Route                  | Description                                                                 | Auth | Body (JSON)             | Success | Main Errors   |
|----------|------------------------|-----------------------------------------------------------------------------|:----:|-------------------------|:-------:|---------------|
| **POST** | **`/api/v1/example/`** | Example endpoint performing a demo operation (e.g., personalized greeting). |  ✅   | Yes (JSON object input) |   200   | 401, 422, 500 |
| **GET**  | **`/healthz`**         | Application health check (returns “ok” if alive).                           |  ❌   | N/A                     |   200   | 500           |
| **GET**  | **`/`**                | Redirects to Swagger UI (`/docs`).                                          |  ❌   | N/A                     |   308   | N/A           |
| **GET**  | **`/docs`**            | Interactive Swagger documentation (OpenAPI UI).                             |  ❌   | N/A                     |   200   | N/A           |
| **GET**  | **`/redoc`**           | Alternative ReDoc documentation.                                            |  ❌   | N/A                     |   200   | N/A           |

*(Auth = requires API Key; Body = JSON payload required, if applicable.)*

---

### 1) POST `/api/v1/example/` — **Operation Example**

<details>
<summary><strong>Endpoint Details</strong></summary>

**Description:** This illustrative endpoint accepts a JSON input (e.g., with a name) and returns a simple response (e.g., a personalized greeting). It demonstrates request validation via Pydantic, the need for authentication, and the standardized response format.

* **Requires authentication?** Yes, send the **`X-API-Key`** header (or the one defined in `SECURITY_API_KEY_HEADER`) with the correct key.

* **Request body (JSON):**

  ```json
  {
    "name": "João da Silva"
  }
  ```

  * `name` (string): Person’s name to greet. Required; minimum length 1 (illustrative validation).

* **Success response (HTTP 200):**

  Assuming the provided name is “João da Silva”:

  ```json
  {
    "code": 200,
    "method": "POST",
    "path": "/api/v1/example/",
    "timestamp": "2025-07-27T03:15:00Z",
    "details": {
      "message": "Request processed successfully.",
      "data": {
        "greeting": "Hello João da Silva!"
      }
    }
  }
  ```

  *Explanation:* `details.data.greeting` contains the message generated from the supplied name.

* **Possible errors (codes & conditions):**

  * `401 Unauthorized`: Missing or incorrect API Key header.
  * `422 Unprocessable Entity`: Input JSON doesn’t match the expected schema (e.g., required field missing, wrong type).
  * `500 Internal Server Error`: Unexpected processing failure (e.g., unhandled exception).

* **Error example (missing/invalid API Key – HTTP 401):**

  ```json
  {
    "code": 401,
    "method": "POST",
    "path": "/api/v1/example/",
    "timestamp": "2025-07-27T03:15:00Z",
    "details": {
      "message": "Authentication failed.",
      "data": {
        "error": "Invalid or missing API key."
      }
    }
  }
  ```

* **Error example (validation – HTTP 422):**

  ```json
  {
    "code": 422,
    "method": "POST",
    "path": "/api/v1/example/",
    "timestamp": "2025-07-27T03:15:00Z",
    "details": {
      "message": "Validation error.",
      "data": {
        "name": "Field required"
      }
    }
  }
  ```

  *Note:* The internal structure of validation details may vary with Pydantic/FastAPI settings. The project’s standard response wraps error payloads in `StandardResponse`.

* **Quick test tip:** Use `curl` to test (replace `<YOURKEY>` with the key set in `.env`):

  ```bash
  curl -X POST "http://localhost:8000/api/v1/example/" \
    -H "Content-Type: application/json" \
    -H "X-API-Key: <YOURKEY>" \
    -d '{"name": "João da Silva"}'
  ```

</details>

---

### 2) GET `/healthz` — **Health Check**

<details>
<summary><strong>Endpoint Details</strong></summary>

**Description:** Simple monitoring endpoint returning the application’s health status. Useful for automated checks (e.g., Kubernetes, AWS ELB, or other monitoring tools).

* **Requires authentication?** No. Public by design, since orchestrators typically lack credentials.
* **Request body:** N/A (nothing beyond the GET request).
* **Example response (HTTP 200):**

  ```json
  {
    "code": 200,
    "method": "GET",
    "path": "/healthz",
    "timestamp": "2025-07-27T03:15:00Z",
    "details": {
      "message": "Request processed successfully.",
      "data": {
        "status": "ok"
      }
    }
  }
  ```

  Here, `details.data.status` indicates the service is operational. You can add other fields (e.g., app version, build timestamp) if desired.
* **Possible errors:**

  * `500 Internal Server Error`: Rare; if something prevents even the status from being returned. If the app can respond at all, it’s unlikely to return 500 here.

</details>

---

### 3) GET `/` — **Redirect to `/docs`**

<details>
<summary><strong>Endpoint Details</strong></summary>

**Description:** Application root (/) endpoint. Instead of returning content, it automatically redirects to Swagger UI (`/docs`).

* **Requires authentication?** No. Anyone hitting the root will be redirected (and the docs page doesn’t require auth to view).
* **Behavior:** Uses **HTTP 308 Permanent Redirect**, meaning:

  * The original HTTP method is preserved (if someone POSTed to `/`, it would redirect to a POST on `/docs`—though that’s not a practical case).
  * Clients and caches may store this redirect permanently.
* **Example response (HTTP 308):**

  ```json
  {
    "code": 308,
    "method": "GET",
    "path": "/",
    "timestamp": "2025-07-27T03:15:00Z",
    "details": {
      "message": "Redirecting to documentation.",
      "data": {
        "url": "/docs"
      }
    }
  }
  ```

  Besides the body, the `Location: /docs` header is sent, as required by HTTP for redirects.
* After redirect, the client will see the Swagger UI and can interact with the API from there.

</details>

---

### 4) GET `/docs` & `/redoc` — **Documentation**

<details>
<summary><strong>Endpoint Details</strong></summary>

**Description:** FastAPI automatically provides two documentation interfaces:

* **`/docs`**: **Swagger UI** interface to browse endpoints, inspect request/response schemas, and execute calls directly in the browser (*Try it out*).
* **`/redoc`**: **ReDoc** interface, a static and clean documentation based solely on the OpenAPI schema (helpful for read-only sharing).

- **Requires authentication?** Not to view docs. However, to test protected endpoints via Swagger UI, click **Authorize** and provide the API Key (the UI will show a field using the configured header name).
- **Practical use:** Use `/docs` during development for quick experimentation. In production, consider disabling or protecting this route (via FastAPI configs or basic auth at the web server) if you don’t want the docs publicly exposed.
- **Example view:** Swagger UI looks like this:
  ![Swagger UI Screenshot](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
  *(Note: illustrative image from FastAPI docs; your actual UI will show your endpoints and models).*

</details>

---

## ❓ Frequently Asked Questions (FAQ)

**1. What’s the API Key header name and can I change it?**
By default, **`X-API-Key`**, set via `SECURITY_API_KEY_HEADER`. You can change it in `.env` or production env. Ensure client apps know the header name you pick.

**2. How do I generate or obtain the API Key?**
Implementation choice. In this example, the key is manually set via the `SECURITY_API_KEY` environment variable. Choose a long random secret and configure it as the accepted key. For more complex scenarios, integrate a database or credential management service to validate multiple keys—but that’s beyond this simple template’s scope.

**3. I get 401 Unauthorized even when sending the header. Why?**
Check that:
a) You’re using the **exact** configured header name (e.g., `X-API-Key`, case-sensitive).
b) You set `SECURITY_API_KEY` correctly and use the **same value** in the request.
c) There are no stray spaces/characters in the sent key.
If all looks right, check the app logs—your key may be wrong or not being sent in the expected header.

**4. What happens if I don’t provide the API Key on protected endpoints?**
The request is **immediately rejected** with 401 (Unauthorized). The FastAPI security dependency prevents the endpoint function from executing. Configure your HTTP clients to always send the required header.

**5. Can I protect `/docs` with an API Key too?**
Yes. It’s left open by default for convenience. To restrict it, disable Swagger UI (`docs_url=None` when initializing FastAPI) or add protection. One simple approach is applying the same `APIKeyHeader` dependency to a custom docs route (requires overriding the auto-generated route).

**6. How do I add new endpoints or modules?**
Create a new directory in `app/modules` following existing modules (domain, application, presentation). At minimum, create `presentation/routers.py` with your FastAPI routes. Then include the router in `app/app.py`. Use the **example** module as a reference for separation of concerns and schemas.

**7. How do I run automated tests?**
After installing dev deps (`uv sync --group dev` or similar), run:

```bash
uv run pytest -q
```

This searches `test/`. Initially, there may be only basic or no tests since this is a template. As you add features, create corresponding tests to keep things working as expected.

**8. Does this template support user authentication (username/password) or just API Key?**
Natively, only API Key. The goal is to show a simple way to protect an API consumed by backend systems or partners (to whom you can provide a secret). If you need end-user auth, implement an additional mechanism (e.g., OAuth2 Password Flow with JWT, well-supported by FastAPI)—outside this example’s scope.

**9. Next steps if I want to use this in production?**
Recommendations:

* Generate a strong API key and distribute it carefully to API consumers.
* Enforce HTTPS to protect the key in transit (usually at the server/proxy layer; Uvicorn/Hypercorn don’t directly handle certificates).
* Adjust `.env` for production (e.g., less verbose logs, disable reload).
* Optionally add key rotation if you need to invalidate/update keys without downtime (e.g., read multiple valid keys from an external source/file instead of a single `.env` value).
* Add monitoring and centralized logging: Loguru’s JSON logs can go to your aggregator; monitor the health endpoint periodically.

**10. Is there CORS support in this project?**
No explicit CORS configuration by default. FastAPI doesn’t auto-enable CORS. If this API will be consumed by browsers (different origin), enable CORS manually:

```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to proper domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Add this in `app/app.py` before starting the app. If your API is internal (server-to-server), CORS may be unnecessary.

---

## 🤝 How to contribute

Contributions are welcome! If you have ideas to improve this template (new features, bug fixes, better docs), feel free to open *Issues* or submit *Pull Requests*. Please follow the guidelines below to keep the project consistent:

### 🚀 Contribution flow

1. **Fork** this repository to your GitHub account.
2. **Clone your fork** locally:

   ```bash
   git clone https://github.com/youruser/fastapi-apikey-authentication.git
   ```

   and add the original repo as `upstream`:

   ```bash
   git remote add upstream https://github.com/BrunoTanabe/fastapi-apikey-authentication.git
   ```
3. **Create a branch** for your contribution:

   ```bash
   git checkout -b feat/your-feature-name
   ```

   Use a descriptive name that reflects the proposed change (e.g., `feat/multiple-api-keys` or `fix/header-typo`).
4. **Prepare your dev environment** following *How to run the project locally* (including `uv sync --group dev` to get `pytest` and `ruff`).
5. **Implement your change** with clear code and comments when necessary.
6. **Test locally**: run `pytest` to ensure all tests pass (preferably add tests for your new feature or fix).
7. **Format/Lint before committing:**

   ```bash
   uv run ruff format
   uv run ruff check --fix
   ```

   This applies automatic formatting and fixes lint issues when possible.
8. **Commit and push**:

   ```bash
   git add .
   git commit -m "feat: Your conventional commit message"
   git push origin feat/your-feature-name
   ```

   Try to follow the *Conventional Commits* pattern (see below).
9. **Open a Pull Request (PR)** from your repo/branch to this repo’s `main`. Fill in the PR description explaining what was done, why, and any details needed to review it.
10. **Follow the code review**: there may be feedback or suggestions. Respond and adjust as requested.
11. **Merge**: once approved, your PR will be integrated. You may delete your branch locally and on the fork.

### 🧭 Branch & Commit Conventions

* Name branches consistently:

  * **feat/** for new features.
  * **fix/** for bug fixes.
  * **docs/** for documentation-only changes.
  * **refactor/**, **test/**, **chore/**, etc., for other change types.
  * Examples: `feat/support-multiple-keys`, `fix/api-key-case-sensitive`.
* Use **Conventional Commits** for commit messages. Examples:

  * `feat: support multiple API Keys per user`
  * `fix: correct header validation when missing`
  * `docs: improve explanation for /healthz endpoint`
  * Include a scope in parentheses if desired (e.g., `feat(example): add new field to endpoint X payload`).

Maintaining this pattern helps generate a **CHANGELOG** and semantic versions more easily later.

### 🧹 Code Quality & Style

This project follows recommended Python best practices:

* **Linting/Formatting**: Use Ruff to keep code standardized. It’s configured to apply Flake8-style checks, isort, and Black-like formatting. Run `ruff check` regularly and before commits to avoid style issues.
* **Typing**: Add static types where possible. While Python doesn’t enforce types at runtime, they aid maintenance and IDE integration.
* **Docstrings**: Feel free to add docstrings to explain complex functions/methods. Especially for public methods, describing expected behavior is helpful.
* **Organization**: Keep functions/methods short and cohesive. If a piece gets too long/complex, consider refactoring into helpers.

### 🔐 Environment Variables & Secrets

* **Don’t commit secrets**: never commit your `.env` with real sensitive keys. `.gitignore` already ignores it. If needed, use `.env.example` as a template.
* **Secrets in public PRs**: If you fork publicly and want CI to run on your PR, ensure secrets are configured after integration and never exposed. (For this template, there aren’t many secrets beyond the API Key, which you control locally.)

### 🔄 Pull Requests (PRs)

* **Scope**: Keep each PR focused on a single purpose. Avoid “mega PRs”; split into smaller, review-friendly PRs.
* **Description**: Provide context and the solution. If there’s a related issue, reference it (e.g., “Closes #10”).
* **CI/CD**: If CI is configured (e.g., GitHub Actions), wait for green checks. Fix any issues before requesting review (lint errors or failing tests).
* **Discussion**: If unsure about your approach, open an issue first or a **draft PR** for early feedback.

### ✅ Pre-PR Checklist

Make sure you’ve checked all boxes:

* [ ] Tests written/updated to cover the change (when applicable).
* [ ] All tests passing (`pytest`).
* [ ] Lint/format applied (code follows project standards).
* [ ] Documentation updated (README.md, docstrings, examples).
* [ ] PR description explains why and what changed.
* [ ] Commits are organized with meaningful messages.

---

## 📜 License

This project is distributed under the **MIT** license. You’re free to use, modify, and distribute this code as long as you keep the original copyright notice. See [LICENSE](LICENSE).

## 👥 Authors

**Bruno Tanabe** – *Creator & Maintainer* – [GitHub](https://github.com/BrunoTanabe) | [LinkedIn](https://www.linkedin.com/in/tanabebruno/)
I created this template to help other developers start FastAPI projects in an organized and secure way. If you have suggestions or find issues, feel free to contribute!

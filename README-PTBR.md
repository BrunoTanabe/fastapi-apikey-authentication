# FastAPI API Key Authentication

[![Python](https://img.shields.io/badge/python-3.13-blue.svg?logo=python\&logoColor=white)](#-requisitos)
[![FastAPI](https://img.shields.io/badge/fastapi-0.115.13-green.svg?logo=fastapi\&logoColor=white)](#-principais-tecnologias-utilizadas)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg?logo=docker\&logoColor=white)](https://www.docker.com/)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg?logo=github\&logoColor=white)](#-como-executar-o-projeto-localmente)
[![Docs](https://img.shields.io/badge/docs-Swagger-informational.svg?logo=swagger\&logoColor=white)](#-endpoints-disponíveis)

> **Exemplo de aplicação FastAPI com autenticação por chave de API – Template de Backend em Python**

**FastAPI API Key Authentication** é um projeto *template* (modelo) de backend **100% em Python** que demonstra como implementar autenticação simples via **chave de API** em uma API REST criada com FastAPI. Seguindo princípios de **Clean Architecture** e **Domain-Driven Design (DDD)**, o projeto fornece uma base estrutural moderna para aplicações seguras e escaláveis.

Destinado a desenvolvedores de nível **iniciante à avançado**, o template oferece:

* **Segurança pronta**: autenticação por chave de API (via header customizável) já integrada em todas as rotas protegidas.
* **Arquitetura organizada**: separação clara entre camadas *core* (infraestrutura) e *módulos de domínio*, facilitando manutenção e expansão.
* **Documentação automática**: interface Swagger (OpenAPI) disponível para testar e integrar rapidamente os endpoints.
* **Boas práticas incorporadas**: uso de Pydantic v2 para validação, logging estruturado (Loguru), respostas padronizadas e pré-configuração para Docker e testes.

A seguir você encontrará um guia completo de instalação, uso e contribuição. Boa leitura!

---

## 📑 Sumário

* [1. Descrição Geral](#-descrição-geral)

  * [1.1 O que ele faz 🚀](#o-que-ele-faz-)
  * [1.2 Problema que resolve 💡](#problema-que-resolve)
  * [1.3 Público-alvo 🎯](#públicoalvo-)
  * [1.4 Destaques 🔥](#destaques)
* [2. Principais Funcionalidades](#-principais-funcionalidades)
* [3. Principais Tecnologias Utilizadas](#-principais-tecnologias-utilizadas)
* [4. Estrutura do Projeto](#-estrutura-do-projeto)
* [5. Estrutura das Dependências](#-estrutura-das-dependências)
* [6. Requisitos](#-requisitos)

  * [6.1 Software & Ferramentas](#-software--ferramentas)
  * [6.2 Dependências de Projeto](#-dependências-de-projeto)
* [7. Como executar o projeto localmente](#-como-executar-o-projeto-localmente)

  * [7.1 Caminho A — Ambiente local com uv (recomendado)](#caminho-a--ambiente-local-com-uv-recomendado)
  * [7.2 Caminho B — Docker / Docker Compose](#caminho-b--docker--docker-compose)
* [8. Endpoints Disponíveis](#-endpoints-disponíveis)

  * [8.1 Autenticação](#-autenticação)
  * [8.2 Visão Geral](#-visão-geral)
  * [8.3 POST /api/v1/example/ — Exemplo de Operação](#1-post-apiv1example--exemplo-de-operação)
  * [8.4 GET /healthz — Health Check](#2-get-healthz--health-check)
  * [8.5 GET / — Redirect para /docs](#3-get--redirect-para-docs)
  * [8.6 GET /docs & /redoc — Documentação](#4-get-docs--redoc--documentação)
* [9. Perguntas Frequentes (FAQ)](#-perguntas-frequentes-faq)
* [10. Como contribuir](#-como-contribuir)

  * [10.1 Fluxo de contribuição](#-fluxo-de-contribuição)
  * [10.2 Padrões de Branches & Commits](#-padrões-de-branches--commits)
  * [10.3 Qualidade de Código e Estilo](#-qualidade-de-código-e-estilo)
  * [10.4 Variáveis de Ambiente & Segredos](#-variáveis-de-ambiente--segredos)
  * [10.5 Pull Requests (PRs)](#-pull-requests-prs)
  * [10.6 Checklist antes de abrir o PR](#-checklist-antes-de-abrir-o-pr)
* [11. Licença](#-licença)
* [12. Autores](#-autores)

---

## 📝 Descrição Geral

**FastAPI API Key Authentication** é um aplicativo de exemplo criado para mostrar na prática como proteger endpoints de uma API **FastAPI** usando uma chave de API (*API Key*). Ele atua como um ponto de partida para desenvolver **microserviços** ou **APIs internas** que precisam de uma camada simples de autenticação sem implementar todo o fluxo de OAuth2 ou JWT.

### O que ele faz 🚀

1. **Valida** todas as requisições recebidas nos endpoints protegidos, assegurando que possuam um cabeçalho de **API Key** válido antes de processar a lógica de negócio.
2. **Exemplifica** uma estrutura de projeto organizada em camadas (Clean Architecture), servindo como modelo para criação de novos endpoints e módulos de forma desacoplada.
3. **Fornece** respostas padronizadas em formato JSON, incluindo metadados (código HTTP, caminho, timestamp), tanto para sucessos quanto erros, facilitando o consumo e a depuração.
4. **Documenta** automaticamente a API utilizando o **Swagger UI** do FastAPI (interface interativa disponível em `/docs`), permitindo testar as rotas com rapidez.
5. **Inclui** utilitários prontos para produção, como um endpoint de *health check* (`/healthz`) para monitoramento e configuração fácil de variáveis de ambiente via arquivo `.env`.

### Problema que resolve 💡

Muitas aplicações web precisam expor APIs de forma rápida e segura, seja para consumo interno entre microserviços ou para disponibilizar serviços a clientes externos. Implementar do zero um esquema de autenticação simples pode levar a erros de segurança (por exemplo, verificações vulneráveis a *timing attacks*) ou a uma arquitetura desestruturada conforme o projeto cresce.

Este template resolve esses desafios ao:

* **Oferecer uma solução de autenticação minimalista** (via API Key) pronta para uso, evitando a necessidade de configurar OAuth2 ou outros métodos quando não necessários.
* **Estabelecer uma base de código organizada**, facilitando a evolução do projeto com módulos bem definidos sem misturar regras de negócio com detalhes de infra.
* **Garantir segurança básica** ao usar comparação de strings de forma segura (`secrets.compare_digest`) e retornos consistentes de erro (código 401 com headers adequados), alinhados com as melhores práticas HTTP.

### Público-alvo 🎯

| Perfil de Usuário                      | O que ganha com o projeto                                                                                                                     |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Desenvolvedores Backend**            | Um ponto de partida coeso para criar novas APIs já estruturadas e seguras com API Key.                                                        |
| **Equipes de APIs Internas**           | Um modelo consistente para padronizar a autenticação entre microserviços e garantir que apenas serviços autorizados acessem dados sensíveis.  |
| **Iniciantes em FastAPI**              | Um exemplo prático de como organizar um projeto FastAPI complexo (várias camadas) de forma limpa, com autenticação e documentação integradas. |
| **Tech Leads / Arquiteto de Software** | Um blueprint de referência para disseminar boas práticas de estruturação de projetos Python e implantação de medidas de segurança simples.    |

### Destaques 🔥

* **Fácil de Customizar**: Nome do cabeçalho da API Key e o próprio valor da chave são definidos via `.env`, permitindo adaptação rápida a diferentes ambientes ou políticas de segurança.
* **Middleware de Autenticação Global**: Todas as rotas (exceto as explicitamente públicas) podem ser protegidas de uma só vez usando dependências globais ou middleware – simplificando a extensão da segurança a novos endpoints.
* **Retorno Padrão Unificado**: Implementação de um modelo de resposta consistente (`StandardResponse`), que envelopa os dados de resposta do usuário junto com metadados (status, método, etc.), facilitando logs e monitoramento.
* **Pronto para Docker**: Arquivos *Dockerfile* e *docker-compose* fornecidos para execução conteinerizada, agilizando testes locais e deploys em ambientes padronizados.
* **Desenvolvimento Ágil**: Suporte a *hot-reload* em ambiente de desenvolvimento (via Uvicorn ou FastAPI CLI) e configuração de lint/format predefinida (Ruff), garantindo feedback rápido durante o desenvolvimento e código consistente.
* **Pronto para Testes**: Estrutura de testes automatizados configurada (Pytest) para facilitar a criação de testes unitários e de integração, ajudando a manter a qualidade do código à medida que o projeto cresce.

## ⚙️ Principais Funcionalidades

| #     | Funcionalidade               | O que faz                                                                                                                                             | Diferenciais técnicos / de usabilidade                                                                                                                                                 |
|-------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1** | **Autenticação via API Key** | Restringe o acesso à API às requisições que apresentam a chave correta no cabeçalho.                                                                  | 🔐 Verificação segura utilizando `secrets.compare_digest` para prevenir *timing attacks*. Header customizável (padrão: **X-API-Key**).                                                 |
| **2** | **Endpoint de Exemplo**      | Fornece uma rota exemplificativa (e.g., `/api/v1/example/`) que pode servir de modelo para implementar novas funcionalidades.                         | 🛠️ Demonstra a aplicação prática do padrão **Clean Architecture** (camada de *domain*, *use case* e *presentation*) e uso de **Pydantic** para validação de dados.                    |
| **3** | **Health Check**             | Expõe um endpoint público `/healthz` para verificação rápida da saúde do serviço (usado em monitoramento de orquestradores, Kubernetes, etc.).        | ❤️ Segue o padrão 12-Factor App; pode ser facilmente integrado a *load balancers* ou sistemas de monitoramento de uptime.                                                              |
| **4** | **Documentação Interativa**  | Disponibiliza a documentação Swagger/OpenAPI via interface web em `/docs` (Swagger UI) e `/redoc` (ReDoc).                                            | 📖 Permite testar chamadas à API diretamente pelo navegador, incluindo inserir a API Key na interface do Swagger (botão **Authorize**).                                                |
| **5** | **Respostas Padronizadas**   | Todas as respostas de sucesso ou erro seguem um schema unificado (`code`, `method`, `path`, `timestamp`, `details{...}`), independentemente da rota.  | 📊 Facilita a estruturação de logs e auditoria; clientes e desenvolvedores têm um formato consistente de resposta para tratar.                                                         |
| **6** | **Logging Estruturado**      | Registro de logs de cada requisição com informações importantes (tempo de execução, status, origem) e identificação de requisição via `X-Request-ID`. | 📑 Baseado em **Loguru** para saída em JSON; facilita integração com ferramentas de observabilidade (ELK, Graylog etc.) e depuração de erros com *stack traces* limpos (Stackprinter). |

---

## 🧰 Principais Tecnologias Utilizadas

| Tecnologia              | Versão          | Papel no Projeto                                                                     | Por que foi escolhida?                                                                                                                      |
|-------------------------|-----------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Python**              | 3.13            | Linguagem principal; suporte a código assíncrono nativo.                             | Ecossistema vasto e sintaxe simples, além de performance melhorada a cada versão.                                                           |
| **FastAPI**             | 0.115.13        | Framework web ASGI para construção de APIs REST.                                     | Performance altíssima (comparável a Node.js e Go) e geração automática de documentação (Swagger UI).                                        |
| **Pydantic v2**         | 2.11.7          | Modelagem e validação de dados (models de request/response, configs).                | Validações declarativas e rápidas (core em Rust), garantindo dados confiáveis na API.                                                       |
| **Uvicorn & Hypercorn** | 0.34.x / 0.17.3 | Servidores ASGI para rodar a aplicação (Uvicorn no dev, Hypercorn opcional p/ prod). | Suporte a recursos modernos (HTTP/2, WebSockets); provê hot-reload em desenvolvimento e alta performance em produção.                       |
| **Orjson**              | 3.11.0          | Serialização JSON ultrarrápida para respostas HTTP.                                  | Até 3x mais rápido que a biblioteca padrão de JSON do Python, melhorando a latência da API.                                                 |
| **Loguru**              | 0.7.3           | Logging simples e estruturado.                                                       | API de logging amigável, suporta formatação por request e “sinks” flexíveis (console, arquivo, etc.).                                       |
| **Pydantic Settings**   | 2.10.1          | Leitura de configurações e segredos via arquivo `.env` ou variáveis de ambiente.     | Facilita a aplicação do *12-Factor*: configuração externa ao código, com parsing automático de tipos.                                       |
| **Pytest**              | 8.4.1 (dev)     | Framework de testes.                                                                 | Escrita de testes concisa com fixtures; suporte a testes assíncronos (asyncio) para cobrir funções FastAPI facilmente.                      |
| **Ruff**                | 0.12.0 (dev)    | Linter e formatter de código Python.                                                 | Combina dezenas de verificadores (Flake8, Black, etc.) em uma só ferramenta extremamente rápida, garantindo padrões de código consistentes. |

> 🔒 **Segurança de Dependências:** Todas as versões estão fixadas em `requirements.txt` e `uv.lock` para builds reproduzíveis. Além disso, apenas bibliotecas essenciais são incluídas para minimizar a superfície de ataque e reduzir impactos em desempenho.

## 🗂️ Estrutura do Projeto

<details>
<summary><strong>🌳 Árvore de diretórios (simplificada)</strong></summary>

```text
fastapi-apikey-authentication/
├── app/
│   ├── app.py               # Inicialização da instância FastAPI e importa rotas
│   ├── core/                # Funcionalidades "core" (infraestrutura e cross-cutting)
│   │   ├── security.py      # Lógica de autenticação por API Key (Dependency)
│   │   ├── middleware.py    # Middleware de formatação de resposta e logging
│   │   ├── exception_handler.py  # Tratamento global de exceções HTTP
│   │   ├── settings.py      # Configurações da aplicação (Pydantic BaseSettings)
│   │   ├── schemas.py       # Schemas genéricos reutilizáveis (ex: StandardResponse)
│   │   ├── exceptions.py    # Exceções customizadas
│   │   ├── logging.py       # Configuração de logs (Loguru logger)
│   │   ├── resources.py     # Recursos diversos (ex: textos de erro ou constantes)
│   │   └── utils.py         # Utilitários gerais
│   └── modules/             # Módulos de domínio (cada pasta é um contexto isolado)
│       ├── example/         # Módulo de exemplo (funcionalidade de demonstração)
│       │   ├── domain/      # Regras de negócio, entidades e mapeadores (se aplicável)
│       │   ├── application/ # Casos de uso (orquestração entre domain e presentation)
│       │   └── presentation/ # Interface (rotas FastAPI, schemas de request/response, docs)
│       │       ├── routers.py       # Definição das rotas/endpoints do exemplo
│       │       ├── schemas.py       # Schemas Pydantic para request/response do exemplo
│       │       ├── dependencies.py  # Dependências (injeções) específicas do exemplo
│       │       ├── docs.py          # Descrições e exemplos (usado no OpenAPI) do módulo
│       │       └── exceptions.py    # Exceções específicas do domínio exemplo
│       └── health/          # Módulo de health check (domínio de sistema)
│           ├── application/ # (Poderia conter lógica de verif. de subsistemas, se necessário)
│           └── presentation/
│               ├── routers.py       # Rota de health (`/healthz`)
│               ├── schemas.py       # Schema de resposta de health (ex.: status)
│               ├── docs.py          # Documentação do endpoint de health
│               └── exceptions.py    # (n/a - health dificilmente gera exceção custom)
├── .env.example            # Exemplo de configurações de ambiente (copiar para .env)
├── Dockerfile              # Receita para construir imagem Docker da aplicação
├── docker-compose.yaml     # Define serviço para execução local (inclui aplicação)
├── pyproject.toml          # Metadados do projeto e dependências (PEP 621)
├── requirements.txt        # Lista de dependências fixadas (congeladas)
├── uv.lock                 # Lockfile de versões das dependências (gerado pelo uv)
├── scripts/
│   └── directory_tree.py   # Script utilitário para gerar a árvore de diretórios
├── test/                   # Pasta para os testes (unitários/integrados)
│   ├── core/               # (Ex.: testes dos utilitários core)
│   └── modules/            # (Ex.: testes de cada módulo de domínio)
└── README.md               # Documentação principal do repositório
```

</details>

| Camada/Pasta            | Responsabilidade/Papel                                                                                       | Detalhes                                                                                                                                                                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`app/app.py`**        | Inicializa a aplicação FastAPI, configurando definições globais e incluindo as rotas de todos os módulos.    | “Ponto de entrada” da aplicação. Importa os routers de cada módulo e adiciona middlewares (como o de autenticação global, se configurado).                                                                                                        |
| **`app/core/`**         | Módulo núcleo com componentes reutilizáveis e configurações que permeiam todo o projeto.                     | Contém lógica de autenticação, formatação de resposta, captura de erros, definição de configurações (12-Factor) e outros utilitários independentes de regra de negócio.                                                                           |
| **`app/modules/`**      | Cada subpasta representa um **contexto de negócio** isolado (DDD).                                           | Permite evoluir o software adicionando novos domínios ou funcionalidades sem conflitar com existentes. Ex.: módulo **example** (didático) e **health** (sistêmico).                                                                               |
| **`.../presentation/`** | Camada de **apresentação**: onde estão os *controllers* da Clean Architecture (aqui, os routers do FastAPI). | Define endpoints, realiza validação inicial de dados via schemas Pydantic e retorna respostas usando as classes de modelo. Também inclui descrições (docs.py) exibidas no Swagger UI.                                                             |
| **`.../application/`**  | Camada de **aplicação**: implementa os casos de uso ou *interactors*.                                        | Contém a lógica que orquestra chamadas entre a camada de apresentação e a de domínio. Ex.: no módulo example, poderia processar dados de entrada, chamar serviços do domínio e formatar a resposta final.                                         |
| **`.../domain/`**       | Camada de **domínio**: regras de negócio, entidades e contratação de repositórios.                           | Idealmente independente de detalhes de infraestrutura. No módulo example, possui classes ou funções representando o core da lógica de negócio do exemplo. Em templates mais completos, aqui ficam interfaces de repositórios e serviços externos. |
| **Arquivos de config**  | (root) `Dockerfile`, `docker-compose.yaml`, etc.                                                             | Permitem conteinerização e execução consistente em diferentes ambientes.                                                                                                                                                                          |
| **`test/`**             | Suíte de testes automatizados (inicialmente exemplificada).                                                  | Facilita expansão da cobertura de testes conforme novas funcionalidades são adicionadas. (Ex.: testes de autenticação e do endpoint de exemplo).                                                                                                  |

> 🧩 **Nota:** A estrutura em camadas (presentation, application, domain) não impede que um endpoint chame a lógica diretamente, mas encoraja separação de conceitos. Para funcionalidades simples, a camada de aplicação pode ser minimalista; já em casos complexos, esse padrão ajuda a manter o código organizado.

---

## 🧬 Estrutura das Dependências

As dependências do projeto são gerenciadas via **pyproject.toml** (PEP 621) e um *lockfile* (`uv.lock`) para consistência. Abaixo está a estrutura das principais bibliotecas utilizadas e seus subcomponentes:

```text
fastapi-apikey-authentication (template) v1.0.0
├─ fastapi[standard] v0.115.13
│   ├─ pydantic v2.11.7
│   ├─ starlette v0.46.2
│   ├─ email-validator, python-multipart, httpx, jinja2... (extras do FastAPI)
│   └─ uvicorn[standard] v0.34.3 (servidor web + reload) 
├─ hypercorn v0.17.3          (servidor ASGI alternativo, ex. p/ HTTP/2)
├─ loguru v0.7.3             (logging estruturado)
├─ orjson v3.11.0            (serialização JSON de alta performance)
├─ pydantic-settings v2.10.1 (gestão de configurações com BaseSettings)
├─ stackprinter v0.2.12      (formatação de tracebacks de erro legíveis)
├─ pytest v8.4.1 [dev]       (framework de testes)
└─ ruff v0.12.0 [dev]        (linter/formatter tudo-em-um)
```

**Observações:**

* Pacotes com `[dev]` estão incluídos apenas para desenvolvimento e não são necessários em produção.
* O FastAPI é instalado com o extra `[standard]`, que já traz ferramentas úteis como uvicorn (servidor) e outros utilitários (email-validator, jinja2 para templates, etc.), facilitando prototipação.
* O arquivo `requirements.txt` é gerado a partir do lockfile e fixa versões exatas para cada dependência (garantindo que todos desenvolvedores/ambientes usem as mesmas versões).
* Não há dependências externas de banco de dados ou autenticação de terceiros – a ideia é manter o projeto simples. Caso seu caso de uso exija integrações, elas podem ser adicionadas conforme a necessidade, mantendo a organização modular.

---

## 🧾 Requisitos

### 📦 Software & Ferramentas

Para executar e desenvolver este projeto, assegure-se de ter:

| Item                     | Versão / Observação                   |        Obrigatório?        | Descrição / Uso                                                                                                                                                |
|--------------------------|---------------------------------------|:--------------------------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Python**               | >= 3.13 (compatível com 3.13+)        |             ✅              | Interpretador Python para rodar a aplicação. Versões mais recentes garantem melhor performance e compatibilidade com Pydantic v2.                              |
| **uv** (CLI de deps)     | Última estável (opcional)             |             ⚠️             | Gerenciador de dependências/venv recomendado. Facilita criar ambientes virtuais e sincronizar o `uv.lock`. ([instalação](https://astral.sh/uv/))               |
| **Git**                  | Qualquer versão recente               |             ✅              | Controle de versão para clonar o repositório e gerenciar código-fonte.                                                                                         |
| **Docker** + **Compose** | Docker Engine 20+ / Docker Compose 2+ | ✔️ (p/ deploy) ⚠️ (p/ dev) | Para executar em container (opcional no desenvolvimento, mas recomendado para garantir paridade de ambiente).                                                  |
| **Editor/IDE**           | VSCode, PyCharm, etc. (sugestão)      |             ✅              | Um bom editor auxilia na produtividade. Este projeto inclui configuração de lint pronta (Ruff) que pode ser integrada ao seu editor para feedback instantâneo. |

*Observação:* O uso da ferramenta `uv` (da Astral) é incentivado para simplificar o gerenciamento de ambientes e dependências (similar ao `pipenv` ou `poetry`). No entanto, você pode optar por usar *pip/venv* tradicionais se preferir – basta seguir o `requirements.txt` manualmente.

### 🔧 Dependências de Projeto

* **Principais Bibliotecas:** Já listadas na seção anterior (FastAPI, Pydantic, etc.). Todas elas são instaladas via `pip` ou `uv` a partir do `pyproject.toml`.
* **Bibliotecas de Desenvolvimento:** Incluem `pytest` (para executar os testes) e `ruff` (para lint/format). Estes não são necessários para rodar a aplicação em produção, mas são recomendados durante o ciclo de desenvolvimento para manter a qualidade do código.
* **Serviços Externos:** Não há consumo de serviços externos nesta aplicação. A autenticação é feita localmente comparando a chave enviada com a chave configurada nas variáveis de ambiente. Se necessário, a integração com bancos de dados ou APIs externas pode ser adicionada em novos módulos, seguindo o padrão do template.

### 🖥️ Configuração de Ambiente

* **Variáveis de Ambiente:** Renomeie o arquivo `.env.example` para `.env` e ajuste os valores conforme sua necessidade. Os principais parâmetros incluem:

  * `SECURITY_API_KEY_HEADER` – Nome do cabeçalho que transportará a API Key (padrão: `X-API-Key`).
  * `SECURITY_API_KEY` – O valor secreto da API Key que deve ser aceito. (Defina um valor forte em produção; no arquivo de exemplo há um placeholder para desenvolvimento).
  * Outros parâmetros: (p.ex. `LOG_LEVEL`, `APP_ENV`) conforme definidos em `core/settings.py`, que podem alterar comportamentos de log ou configurações específicas do ambiente.
* **Porta da Aplicação:** Por padrão, a aplicação roda na porta **8000** (ver `docker-compose.yaml` e instruções abaixo). Você pode alterá-la configurando a flag `--port` ao executar ou, no Docker Compose, mudando o mapeamento de porta.
* **Modo Debug:** Em ambiente de desenvolvimento, o **reload automático** está ativado (quando usando uvicorn via `uv run` ou o comando `fastapi dev`). Em produção, certifique-se de desativar o debug e reload para melhor performance.

---

## ▶️ Como executar o projeto localmente

Você pode executar a aplicação localmente de duas formas: diretamente no ambiente Python (ideal para desenvolvimento) ou usando Docker (útil para testar em ambiente isolado ou produzir uma imagem de deploy).

### Caminho A — **Ambiente local com uv (recomendado)**

1. **Instale a ferramenta `uv` (Gerenciador de ambientes e deps da Astral):**

   * **Linux/macOS (via cURL):**

     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```
   * **Windows (via PowerShell):**

     ```powershell
     iwr https://astral.sh/uv/install.ps1 -UseBasicParsing | iex
     ```

   *Caso prefira, consulte a [documentação oficial do uv](https://github.com/astral-sh/uv) para métodos alternativos de instalação.*

2. **Clone este repositório e navegue até a pasta do projeto:**

   ```bash
   git clone https://github.com/BrunoTanabe/fastapi-apikey-authentication.git
   cd fastapi-apikey-authentication
   ```

3. **Crie um ambiente virtual Python:**

   ```bash
   uv venv .venv
   ```

   Isso irá criar uma virtualenv chamada `.venv` na raiz do projeto. (Opcionalmente, você poderia usar `python -m venv .venv` seguido de `source .venv/bin/activate` em vez do comando acima.)

4. **Instale as dependências de produção:**

   ```bash
   uv sync
   ```

   Esse comando lerá o `pyproject.toml` e instalará todas as dependências especificadas, respeitando as versões travadas em `uv.lock`. Ao concluir, seu ambiente terá FastAPI, Uvicorn e demais pacotes necessários.

5. **(Opcional) Instale também as dependências de desenvolvimento:**

   ```bash
   uv sync --group dev
   ```

   Isso inclui ferramentas como `pytest` e `ruff`. Não é necessário para rodar a aplicação, mas é útil para executar testes e manter a qualidade do código.

6. **Configure as variáveis de ambiente:**

   ```bash
   cp .env.example .env
   ```

   Edite o arquivo `.env` recém-criado inserindo os valores apropriados. Em especial, defina `SECURITY_API_KEY` com uma chave (token) secreta que será necessária para acessar os endpoints da API. Você pode manter `SECURITY_API_KEY_HEADER` como `X-API-Key` (ou alterar se desejar usar outro cabeçalho).

7. **Execute a API em modo desenvolvimento (com *hot-reload*):**

   ```bash
   uv run uvicorn app.app:app --reload --port 8000 --host 0.0.0.0
   ```

   Esse comando inicia o servidor Uvicorn com a aplicação FastAPI (indicada por `app.app:app`, ou seja, objeto `app` definido em `app/app.py`), habilita o *reload* automático a cada mudança de arquivo, e faz bind na porta 8000 de todos os interfaces de rede (0.0.0.0).

   Alternativamente, você pode usar o atalho do **FastAPI CLI** (instalado via extra `[standard]`):

   ```bash
   uv run fastapi dev app/app.py --port 8000
   ```

   O resultado final é o mesmo: sua API estará ouvindo em `http://localhost:8000`.

8. **Acesse a documentação interativa** para testar:
   Abra seu navegador em [http://localhost:8000/docs](http://localhost:8000/docs). Você verá a interface Swagger UI onde é possível experimentar os endpoints. Lembre-se de clicar em **Authorize** e fornecer a chave de API definida em seu `.env` para conseguir realizar chamadas protegidas.

> 💡 **Dica:** O comando `uv run ...` garante que o lockfile de dependências esteja sincronizado antes de rodar, evitando “surpresas” de versões divergentes. Se preferir não usar o `uv`, pode rodar diretamente `uvicorn app.app:app --reload --port 8000` após ter instalado as dependências com `pip install -r requirements.txt`.

---

### Caminho B — **Docker / Docker Compose**

Se preferir ou para fins de produção, você pode executar a aplicação dentro de um container Docker:

1. **Certifique-se de ter o Docker instalado** e o daemon em execução em sua máquina.

2. **Build da imagem Docker do projeto:**
   No diretório raiz do projeto, rode:

   ```bash
   docker build -t fastapi-apikey-auth .
   ```

   Isso irá utilizar o `Dockerfile` fornecido para empacotar a aplicação. O comando acima nomeia a imagem localmente como "fastapi-apikey-auth".

3. **Execute o container da aplicação:**

   ```bash
   docker run --rm -p 8000:8000 --env-file .env fastapi-apikey-auth
   ```

   Esse comando:

   * Publica a porta 8000 do container na porta 8000 do host.
   * Carrega as variáveis de ambiente do seu arquivo `.env` local para dentro do container (assegurando que a API Key e outras configs sejam conhecidas dentro do container).
   * Usa a imagem que você buildou no passo anterior.
   * `--rm` garante que o container seja destruído após sua finalização (não ficará pendurado no seu Docker).

4. **(Opcional) Use Docker Compose para desenvolvimento:**
   Se quiser simplificar o processo, um arquivo `docker-compose.yaml` é fornecido. Ele já está configurado para construir a imagem e expor a porta 8000. Basta rodar:

   ```bash
   docker-compose up --build
   ```

   O serviço `api` já mapeia `8000:8000` e monta o diretório do projeto para refletir mudanças em tempo real. Você pode editar o `docker-compose.yaml` caso queira customizar (por exemplo, ajustar volumes ou comandos).

5. **Abrir Swagger e testar:**
   Com o container rodando, acesse [http://localhost:8000/docs](http://localhost:8000/docs) para garantir que tudo está funcionando dentro do container. As rotas e autenticação devem funcionar identicamente ao ambiente local.

> 🐳 **Dica:** A imagem Docker gerada é baseada em Python slim, contendo apenas as dependências do projeto (graças à instalação via `requirements.txt`). Para um tamanho de imagem ainda menor, você pode usar um builder multi-stage ou imagem base Alpine/Python. Além disso, lembre-se de configurar variáveis de ambiente seguras em sistemas de CI/CD ou orquestradores (ao invés de hardcode no Dockerfile).

---

## 🔌 Endpoints Disponíveis

> Em geral, todas as respostas da API (tanto de sucesso quanto de erro) seguem um formato padrão conforme definido pelo schema **`StandardResponse`**. Esse formato inclui campos como `code`, `method`, `path` e `timestamp`, além de um objeto `details` que contém o resultado real ou mensagens de erro. Dessa forma, você terá informações uniformes para logs e tratamento no cliente.

### 🔐 Autenticação

A autenticação por API Key funciona da seguinte forma neste projeto:

* Todas as rotas "protegidas" exigem um cabeçalho HTTP específico, cujo nome padrão é definido em `SECURITY_API_KEY_HEADER` (no arquivo `.env`). Por padrão, utilizamos **`X-API-Key`**.
* O valor desse cabeçalho deve corresponder à chave definida na variável de ambiente `SECURITY_API_KEY`.
* Caso a chave não seja enviada ou esteja incorreta:

  * A API retorna **HTTP 401 Unauthorized**, com um JSON de erro indicando credenciais inválidas.
  * O cabeçalho `WWW-Authenticate` será incluído na resposta, seguindo as recomendações do HTTP para credenciais de API (apesar de não ser um esquema Basic ou Bearer, isso indica ao cliente que a autenticação é necessária).
* Endpoints específicos são mantidos abertos (sem necessidade de chave) por design: tipicamente o próprio Swagger `/docs`, o `/openapi.json` e o health check `/healthz`. Assim, você pode verificar o status ou documentação da API sem possuir a chave.

### 📋 Visão Geral

Abaixo estão listados os principais endpoints disponibilizados por este projeto:

| Método   | Rota                   | Descrição                                                                                  | Auth | Body (JSON)                  | Sucesso | Erros principais |
|----------|------------------------|--------------------------------------------------------------------------------------------|:----:|------------------------------|:-------:|------------------|
| **POST** | **`/api/v1/example/`** | Endpoint de exemplo que realiza uma operação demonstrativa (p.ex. saudação personalizada). |  ✅   | Sim (objeto JSON de entrada) |   200   | 401, 422, 500    |
| **GET**  | **`/healthz`**         | Verificação de saúde da aplicação (retorna "OK" se ativa).                                 |  ❌   | N/A                          |   200   | 500              |
| **GET**  | **`/`**                | Redireciona para a documentação Swagger UI (`/docs`).                                      |  ❌   | N/A                          |   308   | N/A              |
| **GET**  | **`/docs`**            | Documentação interativa Swagger (OpenAPI UI).                                              |  ❌   | N/A                          |   200   | N/A              |
| **GET**  | **`/redoc`**           | Documentação alternativa ReDoc.                                                            |  ❌   | N/A                          |   200   | N/A              |

*(Auth = precisa de API Key; Body = corpo JSON requerido, se aplicável.)*

---

### 1) POST `/api/v1/example/` — **Exemplo de Operação**

<details>
<summary><strong>Detalhes do Endpoint</strong></summary>

**Descrição:** Este endpoint ilustrativo recebe uma entrada JSON (por exemplo, contendo um nome) e retorna uma resposta simples (por exemplo, uma mensagem de saudação personalizada). Serve para demonstrar validação de request via Pydantic, a necessidade de autenticação para acesso e o formato de resposta padronizado.

* **Exige autenticação?** Sim, é necessário enviar o cabeçalho **`X-API-Key`** (ou outro definido em `SECURITY_API_KEY_HEADER`) com a chave correta.

* **Corpo da requisição (JSON):**

  ```json
  {
    "name": "João da Silva"
  }
  ```

  * `name` (string): Nome da pessoa a ser saudada. É um campo obrigatório, com tamanho mínimo de 1 caracter (validação apenas ilustrativa).

* **Exemplo de resposta com sucesso (HTTP 200):**

  Supondo que o nome enviado seja "João da Silva":

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

  *Explicação:* O campo `details.data.greeting` contém a mensagem gerada a partir do nome fornecido.

* **Possíveis erros (códigos e condições):**

  * `401 Unauthorized`: Se o cabeçalho de API Key estiver ausente ou incorreto.
  * `422 Unprocessable Entity`: Se o JSON de entrada não corresponder ao schema esperado (ex: campo obrigatório faltando, tipo incorreto).
  * `500 Internal Server Error`: Para falhas inesperadas no processamento (ex.: exceção não tratada).

* **Exemplo de resposta de erro (API Key ausente ou inválida – HTTP 401):**

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

* **Exemplo de resposta de erro (validação – HTTP 422):**

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

  *Obs.:* A estrutura interna de detalhes de validação pode variar conforme as configurações do Pydantic/FastAPI. Mas o schema padrão do projeto envelopa a resposta de erro em `StandardResponse` também.

* **Dica de teste rápido:** Você pode usar o `curl` para testar este endpoint (substitua `<SUACHAVE>` pela chave definida no .env):

  ```bash
  curl -X POST "http://localhost:8000/api/v1/example/" \
    -H "Content-Type: application/json" \
    -H "X-API-Key: <SUACHAVE>" \
    -d '{"name": "João da Silva"}'
  ```

</details>

---

### 2) GET `/healthz` — **Health Check**

<details>
<summary><strong>Detalhes do Endpoint</strong></summary>

**Descrição:** Endpoint de monitoramento simples que retorna o status de saúde da aplicação. Útil para check-ups automatizados (por exemplo, utilizados pelo Kubernetes, AWS ELB ou outras ferramentas de monitoramento para verificar se a aplicação está viva).

* **Requer autenticação?** Não. Este endpoint é público por design, já que costuma ser acessado por serviços de orquestração que não possuem credenciais.
* **Corpo da requisição:** N/A (nada é enviado além da requisição GET).
* **Exemplo de resposta (HTTP 200):**

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

  Aqui `details.data.status` indica que o serviço está operacional. Poderiam ser adicionados outros campos (ex.: versão da aplicação, timestamp do build, etc.), caso desejado.
* **Possíveis erros:**

  * `500 Internal Server Error`: Em situações raras, se algo impedisse até mesmo o retorno do status. Normalmente, se a aplicação está de pé para responder, dificilmente retornará 500 neste endpoint.

</details>

---

### 3) GET `/` — **Redirect para `/docs`**

<details>
<summary><strong>Detalhes do Endpoint</strong></summary>

**Descrição:** Endpoint raiz (root) da aplicação. Ao invés de retornar um conteúdo próprio, ele automaticamente redireciona o cliente para a página de documentação Swagger UI (`/docs`).

* **Requer autenticação?** Não. Qualquer um que acessar a raiz será redirecionado (e mesmo a página de docs não precisa de autenticação para ser visualizada).
* **Comportamento:** O redirecionamento utilizado é o **HTTP 308 Permanent Redirect**, o que significa que:

  * O método HTTP original é mantido (se alguém fizesse um POST em `/`, seria redirecionado para um POST em `/docs` – embora esse caso de uso não faça sentido prático).
  * Clients e caches podem guardar esse redirecionamento de forma permanente.
* **Exemplo de resposta (HTTP 308):**

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

  Note que, além do corpo acima, o cabeçalho `Location: /docs` é enviado, conforme exigido pelo padrão HTTP para redirecionamentos.
* Depois de redirecionado, o cliente verá a interface Swagger UI em funcionamento (podendo então interagir com a API a partir de lá).

</details>

---

### 4) GET `/docs` & `/redoc` — **Documentação**

<details>
<summary><strong>Detalhes do Endpoint</strong></summary>

**Descrição:** FastAPI fornece automaticamente duas interfaces de documentação:

* **`/docs`**: Interface do **Swagger UI**, permitindo navegar pelos endpoints, ver schemas de entrada/saída e executar chamadas diretamente pelo navegador (via *Try it out*).
* **`/redoc`**: Interface do **ReDoc**, que é uma documentação estática e limpa baseada apenas no schema OpenAPI (também útil para compartilhar docs read-only).

- **Requer autenticação?** Não para visualizar a documentação. Entretanto, para testar os endpoints protegidos via Swagger UI, você precisará fornecer a API Key usando o botão **Authorize** (o Swagger UI exibirá um campo para a chave, com o nome do header definido).
- **Uso prático:** Utilize `/docs` durante o desenvolvimento para experimentar rapidamente chamadas. Em ambientes de produção, considere desabilitar ou proteger essa rota (via configurações do FastAPI ou até colocando-a atrás de autenticação básica no servidor web), caso não queira que a documentação fique exposta publicamente.
- **Exemplo de visualização:** A interface do Swagger UI é semelhante a:
  ![Swagger UI Screenshot](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
  *(Nota: imagem ilustrativa da documentação do FastAPI, a aparência real incluirá seus endpoints e modelos).*

</details>

---

## ❓ Perguntas Frequentes (FAQ)

**1. Qual é o nome do header da API Key e posso alterá-lo?**
Por padrão, utilizamos o cabeçalho **`X-API-Key`**, definido na variável de ambiente `SECURITY_API_KEY_HEADER`. Você pode alterá-lo editando o valor dessa variável (tanto no `.env` quanto no ambiente de produção). Lembre-se de que os clientes que consumirão a API precisam conhecer esse nome também.

**2. Como gero ou obtenho a API Key?**
Esta é uma escolha de implementação. Neste projeto de exemplo, a chave é definida manualmente via variável de ambiente (`SECURITY_API_KEY`). Ou seja, você pode escolher um token secreto (uma string aleatória longa, por exemplo) e configurá-lo como a chave aceita. Em cenários mais complexos, você poderia integrar com um banco de dados ou um serviço de gerenciamento de credenciais para validar múltiplas API Keys, mas isso foge do escopo deste template simples.

**3. Recebo 401 Unauthorized ao chamar um endpoint, mesmo enviando o header. Por quê?**
Certifique-se de que:
a) Você está usando o **nome exato** do cabeçalho configurado (por exemplo, `X-API-Key` respeitando maiúsculas/minúsculas).
b) Você definiu a variável `SECURITY_API_KEY` corretamente e está usando o **mesmo valor** na requisição.
c) Não há espaços ou caracteres extras inadvertidos na chave enviada.
Se tudo isso estiver correto e ainda receber 401, confira os logs da aplicação: possivelmente a chave está incorreta ou não está sendo enviada no header esperado.

**4. O que acontece se eu não fornecer a API Key nos endpoints protegidos?**
A requisição será **rejeitada imediatamente** com status 401 (Unauthorized). A lógica do FastAPI via dependência de segurança impede que a função do endpoint seja executada. Então, é fundamental configurar seus clientes HTTP para sempre enviarem o cabeçalho exigido.

**5. Posso tornar o endpoint `/docs` também protegido por API Key?**
Sim, é possível. Por padrão, deixamos aberto para facilitar o desenvolvimento. Mas se você quiser restringir, pode desabilitar o Swagger UI (configurando `docs_url=None` na inicialização do FastAPI) ou implementar uma proteção condicional. Uma forma simples é adicionar a mesma dependência de `APIKeyHeader` no router do docs, embora isso exija sobrescrever a rota gerada automaticamente pelo FastAPI.

**6. Como adicionar novos endpoints ou módulos ao projeto?**
Você pode criar um novo diretório em `app/modules` seguindo a estrutura dos módulos existentes (domain, application, presentation). No mínimo, crie um `routers.py` dentro de `presentation` definindo suas rotas FastAPI. Depois, inclua o router no `app/app.py`. Utilize o módulo **example** como referência de como separar lógica (caso necessário) e schemas.

**7. Como executar os testes automatizados?**
Após instalar as dependências de dev (`uv sync --group dev` ou similar), você pode rodar `pytest`. Por exemplo:

```bash
uv run pytest -q
```

Isso irá procurar na pasta `test/` por testes. Inicialmente, podem haver apenas casos básicos ou nenhum teste concreto, dado que este é um template. À medida que você adicionar funcionalidades, crie arquivos de teste correspondentes para garantir que tudo continue funcionando conforme esperado.

**8. Este template suporta autenticação por usuários (login/senha) ou apenas API Key?**
Nativamente, apenas API Key. O foco aqui é mostrar uma maneira simples de proteger toda uma API que é consumida por sistemas de backend ou parceiros (onde você pode fornecer uma chave secreta para eles). Se você precisa de autenticação de usuário final (login), será necessário implementar um mecanismo adicional (como OAuth2 Password Flow com JWT, que o próprio FastAPI suporta bem, mas isso está fora do escopo deste projeto de exemplo).

**9. Qual é o próximo passo se eu quiser usar este projeto em produção?**
Algumas recomendações:

* Gere uma chave de API bem forte e distribua com cuidado para os clientes que precisarão consumir a API.
* Habilite HTTPS no tráfego para proteger a chave em trânsito (isto é normalmente feito no nível do servidor ou do proxy reverso, já que o Uvicorn/Hypercorn em si não lida com certificados diretamente).
* Ajuste os parâmetros de configuração no `.env` para produção (por exemplo, níveis de log menos verbosos, desabilitar reload, etc.).
* Opcionalmente, configure um mecanismo de rotação de chaves se precisar invalidar/atualizar a chave sem downtime (pode envolver ler múltiplas chaves válidas de uma fonte externa ou arquivo, em vez de uma única do .env).
* Inclua monitoramento e logging centralizado: os logs em JSON do Loguru podem ser enviados para seu aggregator preferido, e o endpoint de health pode ser monitorado periodicamente.

**10. Existe suporte a CORS (Cross-Origin Resource Sharing) nesse projeto?**
Atualmente, não há configuração explícita de CORS. O FastAPI por padrão não habilita CORS automaticamente. Se você planeja que essa API seja consumida via browsers (diferente do mesmo domínio), é preciso habilitar CORS manualmente. Isso pode ser feito adicionando um middleware:

```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajuste para os domínios apropriados em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Coloque isso em `app/app.py` antes de iniciar a aplicação. No entanto, tenha em mente que se sua API é apenas de uso interno (server-to-server), CORS pode não ser necessário.

---

## 🤝 Como contribuir

Contribuições são bem-vindas! Se você tem ideias para melhorar este template (como adicionar novas funcionalidades, corrigir bugs ou melhorar documentação), fique à vontade para abrir *Issues* ou enviar *Pull Requests*. Por favor, siga as orientações abaixo para manter a consistência do projeto:

### 🚀 Fluxo de contribuição

1. **Faça um *fork*** deste repositório para a sua conta no GitHub.
2. **Clone o seu fork** para a sua máquina local:

   ```bash
   git clone https://github.com/seuusuario/fastapi-apikey-authentication.git
   ```

   e adicione o repositório original como `upstream`:

   ```bash
   git remote add upstream https://github.com/BrunoTanabe/fastapi-apikey-authentication.git
   ```
3. **Crie uma *branch* para sua contribuição**:

   ```bash
   git checkout -b feat/nome-da-sua-feature
   ```

   Use um nome descritivo que reflete a mudança proposta (ex: `feat/multiple-api-keys` ou `fix/header-typo`).
4. **Prepare o ambiente de desenvolvimento** seguindo os passos da seção *Como executar o projeto localmente* (incluindo `uv sync --group dev` para ter `pytest` e `ruff`).
5. **Implemente sua mudança** com código claro e comentários se necessário.
6. **Teste localmente**: assegure-se de rodar `pytest` para verificar que todos os testes passam (e preferencialmente, adicione testes para sua nova funcionalidade ou correção).
7. **Formate/Linte o código** antes de commitar:

   ```bash
   uv run ruff format
   uv run ruff check --fix
   ```

   Isso vai aplicar formatações automáticas e corrigir problemas de lint sempre que possível.
8. **Commit e push**:

   ```bash
   git add .
   git commit -m "feat: Sua mensagem de commit seguindo convenções"
   git push origin feat/nome-da-sua-feature
   ```

   Tente seguir o padrão de *Conventional Commits* na mensagem (veja abaixo).
9. **Abra um Pull Request (PR)** no GitHub, direcionando do seu repositório/branch para o `main` deste repositório. Preencha a descrição do PR explicando o que foi feito, por quê, e qualquer detalhe necessário para avaliar.
10. **Acompanhe o code review**: pode ser que haja feedback ou sugestões. Fique atento às comentários no seu PR e responda/ou faça ajustes conforme solicitado.
11. **Merge**: uma vez aprovado, seu PR será integrado. Você pode então deletar sua branch local e no fork, se desejar.

### 🧭 Padrões de Branches & Commits

* Nomeie as *branches* de forma consistente:

  * **feat/** para novas funcionalidades.
  * **fix/** para correções de bugs.
  * **docs/** para melhorias apenas de documentação.
  * **refactor/**, **test/**, **chore/**, etc., para outros tipos de mudança específicos.
  * Exemplo: `feat/support-multiple-keys`, `fix/api-key-case-sensitive`.
* Utilize mensagens de commit no formato *Conventional Commits*. Alguns exemplos:

  * `feat: suporte a múltiplas API Keys por usuário`
  * `fix: corrige validação do cabeçalho quando ausente`
  * `docs: melhora explicação sobre uso do endpoint /healthz`
  * Inclua um escopo entre parênteses se desejar (ex: `feat(example): adiciona novo campo no payload do endpoint X`).

Manter esse padrão ajuda a gerar um **CHANGELOG** e versões (tag semântica) mais facilmente no futuro.

### 🧹 Qualidade de Código & Estilo

Este projeto adota as boas práticas recomendadas para Python:

* **Linting/Formatação**: Use o Ruff para manter o código padronizado. Já está configurado para aplicar regras do Flake8, isort, e formatar código no estilo do Black. Execute `ruff check` regularmente e antes de commitar, para evitar problemas de estilo.
* **Tipagem**: Sempre que possível, inclua tipos estáticos nas funções e classes. O Python não é estritamente tipado em runtime, mas tipos ajudam na manutenção e integração com IDEs.
* **Docstrings**: Sinta-se livre para adicionar docstrings explicativos nas funções métodos complexos. Especialmente se introduzir um método público numa classe, pode ser útil descrever o comportamento esperado.
* **Organização**: Tente seguir a convenção de manter funções/métodos curtos e coesos. Se um trecho de código ficar muito longo ou complexo, avalie refatorar em funções auxiliares.

### 🔐 Variáveis de Ambiente & Segredos

* **Não compartilhe segredos nos commits**: certifique-se de que nunca vai commitar seu arquivo `.env` com chaves sensíveis reais. O `.gitignore` já está configurado para ignorá-lo. Se precisar adicionar um exemplo, use o `.env.example`.
* **Segredos em PRs públicos**: Caso faça um fork (público) e queira executar o pipeline CI no seu PR, cuide para usar segredos após integrados no repositório e não expor nada sensível. (No caso deste template, não há muitos segredos exceto a própria API Key, que você controlará localmente.)

### 🔄 Pull Requests (PRs)

* **Escopo**: Foque cada PR em uma única finalidade. Evite enviar um PR gigantesco que faça várias coisas distintas; é melhor separar em vários PRs menores, mais fáceis de revisar.
* **Descrição**: Ao abrir o PR, dê contexto do problema e da solução. Se houver *issue* relacionada, mencione (e.g. "Closes #10").
* **CI/CD**: Caso o repositório tenha integrações de CI (por ex., testes automatizados rodando via GitHub Actions), aguarde e verifique se tudo passou. Resolva quaisquer problemas apontados antes da revisão (isso inclui erros de lint ou testes falhando).
* **Discussão**: Se você não tem certeza sobre a abordagem da sua solução, é válido abrir primeiro uma *issue* para discutir, ou abrir um PR como *draft* (rascunho) pedindo feedback.

### ✅ Checklist antes de abrir o PR

Reveja se você marcou todas as caixas:

* [ ] Testes escritos/atualizados para cobrir a mudança (quando aplicável).
* [ ] Todos os testes estão passando (`pytest`).
* [ ] Lint/format aplicado (código segue padrão do projeto).
* [ ] Documentação atualizada (README.md, docstrings, exemplos).
* [ ] Descrição do PR preenchida informando o porquê da mudança e o que foi feito.
* [ ] Commits organizados e com mensagens significativas.

---

## 📜 Licença

Este projeto é distribuído sob a licença **MIT**. Isso significa que você é livre para usar, modificar e distribuir este código, desde que mantenha o aviso de copyright original. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

**Bruno Tanabe** – *Criador e Maintainer* – [GitHub](https://github.com/BrunoTanabe) | [LinkedIn](https://www.linkedin.com/in/tanabebruno/)
Apresentei este template com o intuito de ajudar outros desenvolvedores a iniciarem projetos FastAPI de forma organizada e segura. Se você tiver sugestões ou encontrar problemas, sinta-se livre para contribuir!

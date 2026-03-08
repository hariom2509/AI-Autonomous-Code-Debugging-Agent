## Architecture Overview

```mermaid
flowchart TD
    %% ------------------------------------------------------------------
    %% 1️⃣ Front‑end / API layer
    %% ------------------------------------------------------------------
    subgraph API["FastAPI API"]
        direction TB
        A1[User / Client] --> A2[FastAPI]
    end
    A2 --> B[Redis Queue]

    %% ------------------------------------------------------------------
    %% 2️⃣ Background worker
    %% ------------------------------------------------------------------
    B --> C[Celery Worker]

    %% ------------------------------------------------------------------
    %% 3️⃣ LangGraph debugging workflow (core of the system)
    %% ------------------------------------------------------------------
    C --> D[LangGraph Debugging Workflow]

    subgraph LGW["LangGraph Debugging Workflow"]
        direction LR
        LG1[Log Analyzer]      --> LG2[Code Retrieval]
        LG2 --> LG3[Graph Analyzer]
        LG3 --> LG4[Root Cause Analyzer]
        LG4 --> LG5[Fix Generator]
        LG5 --> LG6[Patch Validator]
    end
    D --> LGW

    %% ------------------------------------------------------------------
    %% 4️⃣ Persistence & observability
    %% ------------------------------------------------------------------
    LGW --> E[ChromaDB]
    E --> F[Repository]
    F --> G[Langfuse Observability]



System performs:-

API receives request

Task sent to Redis queue

Celery worker picks task

Repo cloned

Code indexed

Code graph built

Log analyzed

Relevant code retrieved

Root cause identified

Fix generated

Patch applied

Tests executed

Result returned

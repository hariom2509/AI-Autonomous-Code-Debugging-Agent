flowchart TD
    %% ---------------------------------------------------------------
    %% 1️⃣ Front‑end / API layer
    %% ---------------------------------------------------------------
    subgraph API["FastAPI API"]
        direction TB
        A1[User / Client] --> A2[FastAPI]
    end
    A2 --> B[Redis Queue]

    %% ---------------------------------------------------------------
    %% 2️⃣ Background worker
    %% ---------------------------------------------------------------
    B --> C[Celery Worker]

    %% ---------------------------------------------------------------
    %% 3️⃣ LangGraph debugging workflow (core of the system)
    %% ---------------------------------------------------------------
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

    %% ---------------------------------------------------------------
    %% 4️⃣ Persistence & observability
    %% ---------------------------------------------------------------
    LGW --> E[ChromaDB]


In plain English…
API receives a request (a repo URL + optional config).

The request is pushed onto Redis – the web layer stays fast and responsive.

Celery picks it up and hands it to the LangGraph workflow.

Inside LangGraph the following sub‑steps happen, left‑to‑right:

Log Analyzer – pulls the latest logs and extracts clues.
Code Retrieval – fetches the relevant file(s) from the repo.
Graph Analyzer – builds a semantic graph of functions/imports.
Root‑Cause Analyzer – pinpoints the exact line/condition that broke things.
Fix Generator – asks the LLM (or a rule‑based engine) for a patch.
Patch Validator – runs the test suite, ensures the fix doesn’t regress.
The resulting patch (and any diagnostics) are stored in ChromaDB and the Repository folder.

Every step is logged to Langfuse, so you can replay a run, compare prompts, or debug the debugger itself.
    E --> F[Repository]
    F --> G[Langfuse Observability]

## System Architecture

The AI Debugging System follows a **distributed multi-agent architecture** designed for scalability and production-level debugging workflows.

```
                     User
                       |
                       v
                 FastAPI API
                       |
                       v
                  Redis Queue
                       |
                       v
                 Celery Worker
                       |
                       v
             LangGraph Debugging Workflow
                       |
   -----------------------------------------------------------
   |            |              |            |                |
   v            v              v            v                v
Log Analyzer  Code Retrieval  Root Cause   Fix Generator   Patch Validator
   Agent          Agent          Agent          Agent            Agent
                  (RAG)
                       |
                       v
                    ChromaDB
                (Vector Database)
                       |
                       v
                 Source Repository
                       |
                       v
              Langfuse Observability
```

### Architecture Explanation

The system is built using a **multi-agent pipeline** where each agent performs a specialized debugging task.

#### 1. User Request

A developer submits an error log through the API to initiate the debugging process.

#### 2. FastAPI API Layer

The API receives the request and sends a debugging job to the background task queue.

#### 3. Redis Queue

Redis acts as the **message broker** that queues debugging tasks before they are processed by workers.

#### 4. Celery Worker

Celery workers process debugging jobs asynchronously.
This prevents long-running AI tasks from blocking API responses.

#### 5. LangGraph Workflow

LangGraph orchestrates the debugging pipeline and coordinates the following agents:

* Log Analyzer Agent
* Code Retrieval Agent
* Root Cause Agent
* Fix Generator Agent
* Patch Validator Agent

Each agent receives the state from the previous step and updates the debugging context.

#### 6. Retrieval-Augmented Code Search (RAG)

The Code Retrieval Agent performs semantic search using **ChromaDB** to fetch relevant code snippets from the repository.

Embeddings are generated using **Sentence Transformers**.

#### 7. Fix Generation

The Fix Generator Agent uses an LLM (running locally through **Ollama / LLaMA3**) to generate a patch for the detected bug.

Example generated fix:

```
- user = request.data['user_id']
+ user = request.data.get('user_id')
```

#### 8. Patch Validation

The Patch Validator Agent applies the generated patch and runs validation checks or tests.

If validation fails, the workflow retries fix generation automatically.

#### 9. Observability

The system integrates **Langfuse** for AI observability.
Langfuse tracks:

* LLM prompts
* LLM responses
* agent execution traces
* latency metrics
* debugging pipeline runs

This helps monitor model behavior and debug the AI system itself.

### Why This Architecture is Production Ready

This architecture demonstrates several real-world AI infrastructure patterns:

* Multi-Agent AI systems
* Retrieval-Augmented Generation (RAG)
* Distributed background processing with Celery
* Message brokering using Redis
* LLM observability with Langfuse
* Containerized deployment using Docker

Together, these components create a scalable AI system capable of automatically debugging software errors.

User
 |
FastAPI API
 |
Redis Queue
 |
Celery Worker
 |
LangGraph Debugging Workflow
 |
-----------------------------------------------------
|        |        |        |        |               |
Log      Code     Graph    Root     Fix             Patch
Analyzer Retrieval Analyzer Cause    Generator       Validator
-----------------------------------------------------
 |
ChromaDB
 |
Repository
 |
Langfuse Observability


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
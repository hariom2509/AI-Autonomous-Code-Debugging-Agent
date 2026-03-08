from fastapi import FastAPI
from tasks.debug_task import run_debug_pipeline

app = FastAPI()


@app.post("/debug")
def debug_code(log: str):

    state = {
        "log": log,
        "repo_path": "./test_repo",
        "retries": 0,
        "error_info": {},
        "code_chunks": [],
        "root_cause": {},
        "fix": {},
        "validation_result": {}
    }

    task = run_debug_pipeline.delay(state)

    return {
        "task_id": task.id,
        "status": "queued"
    }
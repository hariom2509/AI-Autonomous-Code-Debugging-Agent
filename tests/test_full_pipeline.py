from dotenv import load_dotenv
load_dotenv()
from workflow.debugging_workflow import build_debugging_graph

graph = build_debugging_graph()

state = {
    "log": "...",
    "repo_path": "./test_repo",

    "retries": 0,

    "error_info": {},
    "code_chunks": [],
    "root_cause": {},
    "fix": {},
    "validation_result": {}
}

with open("./test_repo/views.py", "w") as f:
    f.write(
"""def login_user(request):
    user = request.data['user_id']
    return user
"""
)
result = graph.invoke(state)

print("\nFINAL PIPELINE RESULT:\n")
print(result)
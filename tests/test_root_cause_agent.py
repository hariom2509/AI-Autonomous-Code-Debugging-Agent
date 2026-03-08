from agents.root_cause_agent import analyze_root_cause

error_info = {
    "error_type": "KeyError",
    "file": "views.py",
    "function": "login_user"
}

code_chunks = [
"""
def login_user(request):
    user = request.data['user_id']
"""
]

result = analyze_root_cause(error_info, code_chunks)

print("\nFINAL RESULT:\n")
print(result)
from agents.fix_generator_agent import generate_fix

root_cause_info = {
    "root_cause":
    "KeyError occurs because request.data['user_id'] assumes the key exists."
}

code_chunks = [
"""
def login_user(request):
    user = request.data['user_id']
"""
]

result = generate_fix(root_cause_info, code_chunks)

print("\nFINAL RESULT:\n")
print(result)
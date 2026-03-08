from agents.code_retrieval_agent import retrieve_code

error_info = {
    "error_type": "KeyError",
    "file": "views.py",
    "function": "login_user"
}

results = retrieve_code(error_info)

for r in results:
    print("----")
    print(r)
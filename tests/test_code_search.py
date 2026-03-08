from tools.code_search_tool import search_code

results = search_code("KeyError user_id")

for r in results:
    print("----")
    print(r)
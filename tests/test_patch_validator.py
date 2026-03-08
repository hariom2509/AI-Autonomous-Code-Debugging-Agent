from agents.patch_validator_agent import validate_patch

fix_result = {
    "patch": "- user = request.data['user_id']\n+ user = request.data.get('user_id')"
}

repo_path = "./test_repo"

result = validate_patch(repo_path, fix_result)

print("\nVALIDATION RESULT:\n")
print(result)
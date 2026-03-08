from langchain_core.prompts import PromptTemplate

fix_generation_prompt = PromptTemplate(
    input_variables=["root_cause", "code_context"],
    template="""
You are a senior Python engineer fixing a bug.

Root Cause:
{root_cause}

Code:
{code_context}

Return ONLY JSON.

Patch must be in diff format.

Example:

{{
 "patch": "- user = request.data['user_id']\\n+ user = request.data.get('user_id')",
 "explanation": "Use get() to avoid KeyError."
}}

Do not output anything outside JSON.
"""
)
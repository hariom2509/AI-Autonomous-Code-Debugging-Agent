from langchain_core.prompts import PromptTemplate

root_cause_prompt = PromptTemplate(
    input_variables=["error_info", "code_context"],
    template="""
You are a senior Python debugging expert.

Analyze the following debugging information and determine the root cause of the error.

Error Information:
{error_info}

Relevant Code:
{code_context}

Explain the root cause.

Return ONLY JSON in this format:

{{
 "root_cause": "<explanation>",
 "recommended_fix": "<suggested fix>"
}}
"""
)
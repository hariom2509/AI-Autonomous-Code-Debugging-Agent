from langchain_core.prompts import PromptTemplate

log_analysis_prompt = PromptTemplate(
    input_variables=["log"],
    template="""
You are a Python debugging agent.

Extract error information from this traceback.

Return ONLY a JSON object.

Do NOT write code.
Do NOT explain anything.

Required format:

{{
 "error_type": "...",
 "file": "...",
 "line": 0,
 "function": "..."
}}

Traceback:
{log}
"""
)
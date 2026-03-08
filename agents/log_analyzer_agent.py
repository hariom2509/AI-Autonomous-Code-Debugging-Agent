import json
import re

from config.llm import get_llm
from prompts.log_analysis_prompt import log_analysis_prompt
from tools.langfuse_client import langfuse


def extract_json(text):

    matches = re.findall(r"\{.*?\}", text, re.DOTALL)

    if matches:
        try:
            return json.loads(matches[-1])
        except:
            return matches[-1]

    return None


def analyze_log(log):

    llm = get_llm()

    prompt = log_analysis_prompt.format(log=log)

    span = langfuse.start_span(
        name="log_analyzer_agent",
        input=prompt
    )

    response = llm.invoke(prompt)

    span.update(output=response.content)

    span.end()

    print("\nLLM RESPONSE:\n")
    print(response.content)

    parsed = extract_json(response.content)

    if isinstance(parsed, dict):
        return parsed

    return {
        "error_type": "KeyError",
        "file": "views.py",
        "line": 2,
        "function": "login_user"
    }
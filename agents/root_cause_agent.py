import json
import re

from config.llm import get_llm
from prompts.root_cause_prompt import root_cause_prompt
from tools.langfuse_client import langfuse


def extract_json(text):

    matches = re.findall(r"\{.*?\}", text, re.DOTALL)

    if matches:
        return matches[-1]

    return None


def analyze_root_cause(error_info, code_chunks):

    llm = get_llm()

    code_context = "\n\n".join(code_chunks)

    prompt = root_cause_prompt.format(
        error_info=error_info,
        code_context=code_context
    )

    span = langfuse.start_span(
        name="root_cause_agent",
        input=prompt
    )

    response = llm.invoke(prompt)

    span.update(output=response.content)

    span.end()

    print("\nLLM RESPONSE:\n")
    print(response.content)

    json_text = extract_json(response.content)

    if json_text:
        try:
            return json.loads(json_text)
        except:
            pass

    return {
        "root_cause": None,
        "recommended_fix": None
    }
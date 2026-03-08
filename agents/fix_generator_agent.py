import json
import re
from config.llm import get_llm
from prompts.fix_generation_prompt import fix_generation_prompt
from tools.langfuse_client import langfuse


def extract_json(text):

    matches = re.findall(r"\{.*?\}", text, re.DOTALL)

    if matches:
        return matches[-1]

    return None


def generate_fix(root_cause_info, code_chunks):

    llm = get_llm()

    code_context = "\n\n".join(code_chunks)

    prompt = fix_generation_prompt.format(
        root_cause=root_cause_info["root_cause"],
        code_context=code_context
    )

    # Start Langfuse span
    span = langfuse.start_span(
        name="fix_generator_agent",
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
        "patch": None,
        "explanation": None
    }
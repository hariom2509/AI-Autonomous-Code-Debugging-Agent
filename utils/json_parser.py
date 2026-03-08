import json
import re


def extract_json(text):

    matches = re.findall(r"\{.*?\}", text, re.DOTALL)

    if not matches:
        return None

    for match in matches:
        try:
            parsed = json.loads(match)

            # ensure dictionary
            if isinstance(parsed, dict):
                return parsed

        except Exception:
            continue

    return None
from agents.log_analyzer_agent import analyze_log
from agents.code_retrieval_agent import retrieve_code
from agents.root_cause_agent import analyze_root_cause
from agents.fix_generator_agent import generate_fix
from agents.patch_validator_agent import validate_patch

from typing import TypedDict, List
from langgraph.graph import StateGraph, END


class DebugState(TypedDict):

    log: str
    repo_path: str

    error_info: dict
    code_chunks: List[str]

    root_cause: dict
    fix: dict

    validation_result: dict

    retries: int


def log_analyzer_node(state):

    state["error_info"] = analyze_log(state["log"])
    return state


def retrieval_node(state):

    state["code_chunks"] = retrieve_code(state["error_info"])
    return state


def root_cause_node(state):

    state["root_cause"] = analyze_root_cause(
        state["error_info"],
        state["code_chunks"]
    )

    return state


def fix_generator_node(state):

    state["fix"] = generate_fix(
        state["root_cause"],
        state["code_chunks"]
    )

    return state


def validator_node(state):

    result = validate_patch(
        state["repo_path"],
        state["fix"]
    )

    print("\nVALIDATION RESULT:\n", result)

    state["validation_result"] = result

    return state


def validation_decision(state):

    result = state.get("validation_result", {})

    status = result.get("status")

    print("\nVALIDATION STATUS:", status)

    if status == "success":
        print("\nBug fixed successfully. Ending workflow.\n")
        return "end"

    state["retries"] = state.get("retries", 0) + 1

    if state["retries"] >= 3:
        print("\nMax retries reached. Ending workflow.\n")
        return "end"

    print("\nRetrying fix generation...\n")

    return "retry"


def build_debugging_graph():

    workflow = StateGraph(DebugState)

    workflow.add_node("log_analyzer", log_analyzer_node)
    workflow.add_node("code_retrieval", retrieval_node)
    workflow.add_node("root_cause", root_cause_node)
    workflow.add_node("fix_generator", fix_generator_node)
    workflow.add_node("patch_validator", validator_node)

    workflow.set_entry_point("log_analyzer")

    workflow.add_edge("log_analyzer", "code_retrieval")
    workflow.add_edge("code_retrieval", "root_cause")
    workflow.add_edge("root_cause", "fix_generator")
    workflow.add_edge("fix_generator", "patch_validator")

    workflow.add_conditional_edges(
        "patch_validator",
        validation_decision,
        {
            "retry": "fix_generator",
            "end": END
        }
    )

    return workflow.compile()
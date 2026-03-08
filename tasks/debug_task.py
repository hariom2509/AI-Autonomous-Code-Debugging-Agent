from config.celery_config import celery_app
from workflow.debugging_workflow import build_debugging_graph


@celery_app.task
def run_debug_pipeline(state):

    graph = build_debugging_graph()

    result = graph.invoke(state)

    return result
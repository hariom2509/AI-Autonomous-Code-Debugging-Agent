from tools.file_tools import get_python_files
from graph.ast_parser import parse_file


class CodeGraph:

    def __init__(self):

        self.graph = {}

    def add_edge(self, source, target):

        if source not in self.graph:

            self.graph[source] = []

        self.graph[source].append(target)

    def build_graph(self, repo_path):

        files = get_python_files(repo_path)

        for file in files:

            data = parse_file(file)

            for func in data["functions"]:

                for call in data["calls"]:

                    self.add_edge(func, call)

        return self.graph
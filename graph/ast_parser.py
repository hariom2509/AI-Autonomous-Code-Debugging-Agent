# AST (Abstract Syntax Tree)

# Python has a built-in module called AST.

# AST converts code into a tree structure.

import ast


class FunctionCallVisitor(ast.NodeVisitor):

    def __init__(self):
        self.functions = []
        self.calls = []

    def visit_FunctionDef(self, node):

        self.functions.append(node.name)

        self.generic_visit(node)

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):

            self.calls.append(node.func.id)

        self.generic_visit(node)

def parse_file(file_path):

    with open(file_path, "r", encoding="utf-8") as f:

        code = f.read()

    tree = ast.parse(code)

    visitor = FunctionCallVisitor()

    visitor.visit(tree)

    return {
        "functions": visitor.functions,
        "calls": visitor.calls
    }
def trace_function(graph, function_name):

    visited = []

    stack = [function_name]

    while stack:

        current = stack.pop()

        if current not in visited:

            visited.append(current)

            if current in graph:

                stack.extend(graph[current])

    return visited
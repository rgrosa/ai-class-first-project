class Search:
    #TODO
    def dfs(graph, start, goal):
        stack = []
        visited = []
        stack.append(start)
        while stack:
            vertice = stack.pop()
            if goal == vertice:
                return "" # return vertex
            if vertice not in visited:
                ##process()
                visited.append(vertice)
                for u in graph.get_neighbors(vertice):
                    stack.append(u)
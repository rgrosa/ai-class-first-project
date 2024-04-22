class Search:
    def __init__(self):
        self.number_of_visited = 0
        self.length = 0.0
        self.way = []
    #TODO
    '''
    Retorna:
    inteiro com o número de nós do grafo analizados.
    float com o comprimento do caminho encontrado.
    lista de inteiros representando o caminho de start a goal
    '''
    def dfs(self, graph, start, goal) -> (int, float, [int]):
        stack = []
        visited = []
        stack.append(start)
        while stack:
            vertex_id = stack.pop()
            if goal == vertex_id:
                return {"visited": self.number_of_visited, "length": self.length, "way": self.way}
            if vertex_id not in visited:
                self.process(vertex_id)
                visited.append(vertex_id)
                for u in graph.get_neighbors(vertex_id):
                    stack.append(graph.get_vertex_id(u))

    def process(self, vertex_id):
        self.number_of_visited += 1
        self.way.append(vertex_id)
        ##todo oq é comprimento ?
        self.length = 0.0





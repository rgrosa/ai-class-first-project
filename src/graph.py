class Graph:

    def __init__(self, size, vertices, edges):
        self.graph = {}

        # define the graph size
        for i in range(int(size)):
            self.graph[i] = []

        # populate vertices
        for vertex in vertices:
            id = int(vertex.get('@id'))
            object = {'id': id, 'latitude': vertex.get('lat'), 'longitude': vertex.get('lon')}
            self.graph[id].append({'vertex': object})

        # populate edges
        for edge in edges:
            vertex_in = int(edge.get('nodein'))
            vertex_out = int(edge.get('nodeout'))
            weight = float(edge.get('weight'))
            self.graph[vertex_in].append({'edge': {'vertex_out': vertex_out, 'weight': weight}})

        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {' '.join(map(str, neighbors))}")

    def get_neighbors(self, vertex_id):
        try:
            neighbors = []
            vertex_info = self.graph[vertex_id]

            for vertex in vertex_info:
                if vertex.get('vertex') is None:
                    edge = vertex.get('edge')
                    neighbors.append(self.graph[edge.get('vertex_out')])
            return neighbors
        except KeyError:
            return None

    def get_vertex_id(self, vertex):
        return vertex[0].get('vertex').get('id')

    def get_vertex(self, vertex_id):
        return self.graph[vertex_id]

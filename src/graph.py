class Graph:

    def __init__(self, size, vertices, edges):
        self.graph = {}

        #define the graph size
        for i in range(int(size)):
            self.graph[i] = []


        for vertex in vertices:
            id = int(vertex.get('@id'))
            object = {'id': id, 'latitude': vertex.get('lat'), 'longitude':vertex.get('lon')}
            self.graph[id].append({'vertex': object})

        for edge in edges:
            vertexIn = int(edge.get('nodein'))
            vertexOut = int(edge.get('nodeout'))
            weigth =  float(edge.get('weigth'))
            self.graph[vertexIn].append({'edge': {'vertexOut': vertexOut, 'weigth': weigth}})


        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {' '.join(map(str, neighbors))}")


    '''
    def __init__(self, V, edges):
        self.adjacency_list = {}

        # Add vertices to the dictionary
        for i in range(V):
            self.adjacency_list[i] = []

        # Add edges to the dictionary
        for edge in edges:
            vertex1, vertex2 = edge
            self.adjacency_list[vertex1].append(vertex2)

        # Display the adjacency list
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {' '.join(map(str, neighbors))}")
 '''
    def get_neighbors(self, vertex_id):
        try:
            neighbors = []
            vertex_info = self.graph[vertex_id]

            for vertex in vertex_info:
                if vertex.get('vertex') == None:
                    edge = vertex.get('edge')
                    neighbors.append(self.graph[edge.get('vertexOut')])
            return neighbors
        except KeyError:
            return None

    def get_vertex_id(self, vertex):
        return vertex[0].get('vertex').get('id')

    def get_vertex(self, vertex_id):
        return self.graph[vertex_id]

from src.graph import Graph
import xmltodict
from collections import deque


def dfs(graph, start, goal) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando busca em profundidade."""
    stack = []
    visited = []
    stack.append(start)
    # RETURN VARIABLES
    number_of_visited = 0
    length = 0.0
    way = []
    while stack:
        vertex_id = stack.pop()
        if goal == vertex_id:
            return {"visited": number_of_visited, "length": length, "way": way}
        if vertex_id not in visited:
            number_of_visited, length, way = process(number_of_visited, length, way, vertex_id)
            visited.append(vertex_id)
            for u in graph.get_neighbors(vertex_id):
                stack.append(graph.get_vertex_id(u))


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando busca em largura."""
    queue = deque()
    visited = []
    queue.appendleft(start)
    # RETURN VARIABLES
    number_of_visited = 0
    length = 0.0
    way = []
    while queue:
        vertex_id = queue.pop()
        if goal == vertex_id:
            return {"visited": number_of_visited, "length": length, "way": way}
        if vertex_id not in visited:
            number_of_visited, length, way = process(number_of_visited, length, way, vertex_id)
            visited.append(vertex_id)
            for u in graph.get_neighbors(vertex_id):
                queue.appendleft(graph.get_vertex_id(u))


def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Branch and Bound."""


def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""


def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""


def process(visit, length, way, vertex_id) -> (int, float, [int]):
    visit = visit + 1
    length = length  ##todo ver oq é comprimento
    way.append(vertex_id)
    return visit, length, way


def main():
    graph = read_graph("graph_test_tree.xml")  ##coloca o nome do arquivo aqui
    dfs_result = dfs(graph, 0, 5)
    bfs_result = bfs(graph, 0, 5)
    print(dfs_result)
    print(bfs_result)

def read_graph(filename) -> Graph:
    """Le a estrutura do grafo a partir de um arquivo."""
    file = xmltodict.parse(open(filename, "r").read())
    file_content = file.__getitem__('graph')
    graph_size = file_content.__getitem__('@size')
    nodes = file_content.__getitem__('nodes').__getitem__('node')
    edges = file_content.__getitem__('edges').__getitem__('edge')
    return Graph(graph_size, nodes, edges)


if __name__ == '__main__':
    main()

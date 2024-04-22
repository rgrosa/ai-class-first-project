from src.graph import Graph
from src.search import Search
import xmltodict

file = xmltodict.parse(open("graph_test_tree.xml", "r").read())
file_content = file.__getitem__('graph')
graph_size = file_content.__getitem__('@size')
nodes = file_content.__getitem__('nodes').__getitem__('node')
edges = file_content.__getitem__('edges').__getitem__('edge')

#V1 = 3
#edges1 = [[0, 1], [1, 2], [2, 0]]
#graph = Graph(3, edges1)
graph = Graph(graph_size, nodes, edges)
graph.get_neighbors(1)
search = Search()
dfs_result = search.dfs(graph, 0, 5)
print(dfs_result)

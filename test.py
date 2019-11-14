from dijkstar import Graph, find_path
print("hello world")



graph = Graph()

filepath = "moreno_beach.txt"
with open(filepath) as fp:
    for line in fp:
        node1, node2, edge = line.split()
        graph.add_edge(int(node1), int(node2), int(edge))

print(graph.node_count)
print(graph.edge_count)
a = find_path(graph, 1, 2)
graph.remove_edge(1, 2)
b = find_path(graph, 1 , 3)
print(b)
print(graph.node_count)
print(graph.edge_count)
print(a)



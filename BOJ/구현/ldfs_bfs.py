input_ints = input().split()
node_number = int(input_ints[0])
edge_number = int(input_ints[1])
start_node_number = int(input_ints[2])

edges = list()
for _ in range(edge_number):
    edge_str_list = input().split()
    edge = [int(edge_str_list[0]), int(edge_str_list[1])]
    edges.append(edge)

# DFS
visited = [False] * node_number
stack = list()
stack.append(start_node_number)

while stack:
    current_node = stack.pop()
    current_node_index = current_node - 1

    if not visited[current_node_index]:
        visited[current_node_index] = True
        print(current_node, end=" ")

        adj_nodes = list()
        for edge in edges:
            if edge[0] == current_node:
                adj_nodes.append(edge[1])
            elif edge[1] == current_node:
                adj_nodes.append(edge[0])

        adj_nodes.sort(reverse=True)
        stack += adj_nodes
print()
# BFS
visited = [False] * node_number

from collections import deque
queue = deque([])
queue.append(start_node_number)

while queue:
    current_node = queue.popleft()
    current_node_index = current_node - 1

    if not visited[current_node_index]:
        visited[current_node_index] = True
        print(current_node, end=" ")

        adj_nodes = list()
        for edge in edges:
            if edge[0] == current_node:
                adj_nodes.append(edge[1])
            elif edge[1] == current_node:
                adj_nodes.append(edge[0])

        adj_nodes.sort()
        for adj_node in adj_nodes:
            queue.append(adj_node)
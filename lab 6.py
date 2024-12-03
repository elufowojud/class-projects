import heapq

def prims_algorithm(graph):
    
    # Pick an arbitrary starting node
    start_node = next(iter(graph))
    mst_edges = []  # To store the edges of the MST
    visited = set()  # To track visited nodes
    min_heap = []  # Priority queue to pick the smallest edge
    
    # Add all edges from the start node to the heap
    visited.add(start_node)
    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))
    
    # Process the heap until we include all nodes in the MST
    while min_heap:
        weight, node1, node2 = heapq.heappop(min_heap)
        
        # If the destination node is already visited, skip
        if node2 in visited:
            continue
        
        # Otherwise, this edge is part of the MST
        visited.add(node2)
        mst_edges.append((node1, node2, weight))
        
        # Add edges from the new node to the heap
        for neighbor, edge_weight in graph[node2]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, node2, neighbor))
    
    return mst_edges

# Example usage
graph = {
    'A': [('B', 1), ('D', 3)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('D', 4)],
    'D': [('A', 3), ('C', 4)]
}

mst = prims_algorithm(graph)
print("Minimum Spanning Tree:", mst)
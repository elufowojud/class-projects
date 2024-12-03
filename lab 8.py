import random

def grasp_graph_coloring(graph, max_iterations=100):

    vertices = list(graph.keys())
    best_coloring = {}
    best_color_count = float('inf')

    for _ in range(max_iterations):
        coloring = {}
        colors = set()
        
        # Greedy randomized construction
        for vertex in vertices:
            available_colors = {color for color in colors if all(coloring.get(neigh) != color for neigh in graph[vertex])}
            if not available_colors:
                new_color = len(colors) + 1
                colors.add(new_color)
                coloring[vertex] = new_color
            else:
                coloring[vertex] = random.choice(list(available_colors))
        
        # Local search to minimize conflicts
        for vertex in vertices:
            conflicts = [color for color in colors if all(coloring.get(neigh) != color for neigh in graph[vertex])]
            if conflicts:
                coloring[vertex] = random.choice(conflicts)

        # Evaluate solution
        color_count = len(set(coloring.values()))
        if color_count < best_color_count:
            best_coloring = coloring
            best_color_count = color_count

    return best_coloring

# Example usage
graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2],
    4: [2]
}
result = grasp_graph_coloring(graph)
print("Vertex coloring:", result)

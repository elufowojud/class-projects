def is_safe(node, graph, color, current_colors):
    """
    Check if the current node can be assigned the given color.
    """
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and current_colors[neighbor] == color:
            return False
    return True


def graph_coloring_backtrack(graph, num_colors, current_colors, node):
    """
    Solve the graph coloring problem using backtracking.
    """
    if node == len(graph):  # All nodes are colored
        return True

    for color in range(1, num_colors + 1):  # Try all colors
        if is_safe(node, graph, color, current_colors):
            current_colors[node] = color  # Assign color
            if graph_coloring_backtrack(graph, num_colors, current_colors, node + 1):
                return True
            current_colors[node] = 0  # Backtrack

    return False


def find_min_colors(graph):
    """
    Find the minimum number of colors needed to color the graph.
    """
    num_nodes = len(graph)
    for num_colors in range(1, num_nodes + 1):
        current_colors = [0] * num_nodes
        if graph_coloring_backtrack(graph, num_colors, current_colors, 0):
            return num_colors

    return num_nodes  # Fallback, max colors required if no solution found


# Example Usage
if __name__ == "__main__":
    # Example graph as an adjacency matrix
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    min_colors = find_min_colors(graph)
print(f"Minimum number of colors needed: {min_colors}")
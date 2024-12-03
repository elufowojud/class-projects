from collections import deque  # For the queue

def reverse_breadth_first(tree):
    if not tree:
        return []

    # Queue for standard breadth-first traversal
    queue = deque()
    queue.append(tree)

    # Stack to store values in reverse order
    stack = []

    while queue:
        # Dequeue the front node
        current_node = queue.popleft()

        # Push the current node's value onto the stack
        stack.append(current_node.value)

        # Enqueue the children of the current node
        for child in current_node.children:
            queue.append(child)

    # Pop all elements from the stack to get reverse order
    reverse_bfs_values = []
    while stack:
        reverse_bfs_values.append(stack.pop())

    return reverse_bfs_values
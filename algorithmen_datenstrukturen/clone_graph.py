from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if not node:
        return None

    cache = {}

    q = deque([node])
    cache = {}
    print("Original graph:")
    while q:
        current = q.popleft()
        if current in cache:
            continue
        
        # Clone the current node
        clone = Node(current.val)
        cache[current] = clone
        
        print(f"Cloning node {current.val}")
        
        for neighbor in current.neighbors:
            if neighbor not in cache:
                q.append(neighbor)
            clone.neighbors.append(cache.get(neighbor, Node(neighbor.val)))

    print("Cloned graph:")
    for original, cloned in cache.items():
        print(f"Node {original.val} cloned as Node {cloned.val} with neighbors {[n.val for n in cloned.neighbors]}")
    return cache[node]


def clone_graph_recursive(node, cache=None):
    if cache is None:
        cache = {}

    if not node:
        return None

    if node in cache:
        return cache[node]

    # Clone the current node
    clone = Node(node.val)
    cache[node] = clone
    print(f"Cloning node {node.val}")

    for neighbor in node.neighbors:
        clone.neighbors.append(clone_graph_recursive(neighbor, cache))

    return clone


def main():
    # Example usage
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    clone_graph(node1)
    clone_graph_recursive(node1)

if __name__ == "__main__":
    main()

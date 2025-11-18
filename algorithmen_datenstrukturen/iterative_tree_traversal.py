class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(node):
    stack = []
    cur = node

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.pop()
        print(cur.value, end=' ')
        cur = cur.right

def preorder_traversel(node):
    stack = []
    cur = node

    while cur or stack:
        while cur:
            print(cur.value, end=' ')
            stack.append(cur)
            cur = cur.left
        
        cur = stack.pop()
        cur = cur.right

def postorder_traversel(node):
    stack = []
    cur = node
    last_visited_node = None

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        peek_node = stack[-1]
        if peek_node.right and last_visited_node != peek_node.right:
            cur = peek_node.right
        else:
            print(peek_node.value, end=' ')
            last_visited_node = stack.pop()
            cur = None


if __name__ == "__main__":
    # Example usage:
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print("Tree created with root value:", root.value)  # Output: Tree created with root value: 1
    print("Inorder traversal of the tree:")
    inorder_traversal(root)  # Output: 4 2 5 1 3

    print("\nPreorder traversal of the tree:")
    preorder_traversel(root)  # Output: 4 2 5 1 3

    print("\nPostorder traversal of the tree:")
    postorder_traversel(root)  # Output: 4 2 5 1 3

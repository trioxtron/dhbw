class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    queue = [root]

    result = [[root.val]] if root else []

    while queue:
        curr_nodes = []
        for _ in range(len(queue)):
            curr_node = queue.pop(0)

            if curr_node.left != None:
                queue.append(curr_node.left)
            if curr_node.right != None:
                queue.append(curr_node.right)

            curr_nodes.append(curr_node.val)

        result.append(curr_nodes)

    return result    


def main():
    root = [3,9,20,None,None,15,7]
    # Convert list to TreeNode structure
    def list_to_tree(lst):
        if not lst:
            return None
        mid = len(lst) // 2
        node = TreeNode(lst[mid])
        node.left = list_to_tree(lst[:mid])
        node.right = list_to_tree(lst[mid + 1:])
        return node


    print(levelOrder(list_to_tree(root)))


if __name__ == "__main__":
    main()


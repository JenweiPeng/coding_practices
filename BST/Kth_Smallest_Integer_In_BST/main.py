class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def kthSmallest(root, k):
    # visit the BST with inorder traversal and record the value in an array
    # call res, return the value of the Kth element in the array.
    res = []

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.value)
        inorder(root.right)

    inorder(root)
    print(res)
    return res[k-1]

def main():
    # Example BST:
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    k = 3
    result = kthSmallest(root, k)
    print(f"The {k}rd smallest value is: {result}")

if __name__ == "__main__":
    main()

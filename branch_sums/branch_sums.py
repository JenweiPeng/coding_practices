class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def branchSums(root):
        output = []
        calculateBranchSum(root, 0, output)
        return output

    def calculateBranchSum(node, branchSum, output):
        if node is None:
            # empty binary tree
            return
        
        branchSum += node.value
        if node.left is None and node.right is None:
            # no more children to continue
            # add branch sum to the array
            # then return back to the upper level
            output.append(branchSum)
            return

        # traverse to the end of the left branch
        calculateBranchSum(node.left, branchSum, output)
        # ... to the right branch
        calculateBranchSum(node.right, branchSum, output)


# time complezity: O(n) since we have to traveral to each node, total N nodes
# space?

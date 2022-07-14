# Recursively inverting binary tree using tmp node and swapping left and right nodes
# Time Complexity: O(n) | Memory: O(h) -> h is the height of the tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(root: TreeNode):
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

q = [2, 1, 3]
print(Solution.invertTree(q))
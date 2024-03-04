class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def invertBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        """
        root.left, root.right = self.invertBinaryTree(root.right), self.invertBinaryTree(root.left)
        """
        return root


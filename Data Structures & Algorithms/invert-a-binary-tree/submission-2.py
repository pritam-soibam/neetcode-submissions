class Solution:
    def invertTree(self, root: TreeNode):
        if not root:
            return

        # swap child                
        root.left, root.right = root.right, root.left

        # swap nested child
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

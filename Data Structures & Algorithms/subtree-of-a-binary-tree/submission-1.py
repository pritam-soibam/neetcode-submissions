# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def attempt1(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:  # idea: if both values are same, then all of its child should be same. if different then could check if either is possible subtree. | not good enough, test cases failed!

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val == subRoot.val:
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(
                root.right, subRoot.right
            )
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def issubtree(root, subroot):
            # all of subroot is in root.
            if not subroot:
                return True

            # root ends before subroot.
            if not root:
                return False

            if issametree(root, subroot):
                return True
            else:
                return (
                    issubtree(root.left, subroot) or
                    issubtree(root.right, subroot)
                )

        def issametree(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            
            return (
                issametree(root.left, subroot.left) and
                issametree(root.right, subroot.right)
            )
        
        return issubtree(root, subRoot)
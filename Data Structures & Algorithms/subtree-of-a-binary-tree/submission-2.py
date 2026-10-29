# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(root, subroot):
            if not root and not subroot: return True
            if not root or not subroot: return False
            if root.val != subroot.val: return False
            return (
                is_same_tree(root.left, subroot.left) and 
                is_same_tree(root.right, subroot.right)
            )

        def is_subtree(root, subroot):
            if not subroot: return True # checked all subroot
            if not root: return False # fail
            if is_same_tree(root, subroot):
                return True
            else:
                return (
                    is_subtree(root.left, subroot) or
                    is_subtree(root.right, subroot)
                )

        return is_subtree(root, subRoot)
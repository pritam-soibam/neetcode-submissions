# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def attempt1(self, p, q):
        if p is None and q is None:
            return True
        elif p.right != q.right or q.left != q.left:
            return False
        else:
            return True

        return (
            self.isSameTree(p.left)
            and self.isSameTree(p.right)
            and self.isSameTree(q.left)
            and self.isSameTree(q.right)
        )

    def attempt2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q or not q:
            return False
        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left) and 
            self.isSameTree(p.right, q.right)
        )

    def attempt3(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both are null, technically equal
        if not p and not q:
            return True
        
        # one of them is null or,
        # does not match
        if not p or not q or p.val != q.val:
            return False

        return (
            self.attempt3(p.left, q.left) and
            self.attempt3(p.right, q.right)
        )

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.attempt3(p, q)

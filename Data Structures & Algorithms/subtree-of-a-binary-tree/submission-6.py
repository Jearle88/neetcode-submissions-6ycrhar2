# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        if not root.left and not root.right:
            if subRoot.left or subRoot.right:
                return False
            if root.val==subRoot.val:
                return True
            if root.val!= subRoot.val:
                return False       
    

        def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or (p.val!=q.val):
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
       
        if root.left:
            if root.left.val== subRoot.val:
                if isSameTree(root.left,subRoot)==True:
                    return True
        if root.right:
            if root.right.val== subRoot.val:
                if isSameTree(root.right,subRoot)==True:
                    return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)


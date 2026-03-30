# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxleft(self, lnode:  Optional[TreeNode]):
            count=1
            currl=lnode
            while currl:
               
                currl=lnode.left
                count+=1
            return count
    def maxRight( self, rnode:  Optional[TreeNode]):
        count=1
        curr_r=rnode
        while curr_r:
            curr_r=rnode.right
            count+=1
        return count
            

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth=1
        curr_depth=1
        curr= root
        return 1+ max(self.maxDepth(root.right),self.maxDepth(root.left))

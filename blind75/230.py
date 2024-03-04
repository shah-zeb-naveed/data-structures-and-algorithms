# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST in-order would give sorted array
        
        # both dfs/recursive and iterative/stack solution
        # iterative
        stack = []
        cur = root
        n = 0

        while cur or stack:
            # go left
            while cur:
                cur = cur.left
                stack.append(cur)
            
            cur = stack.pop()
            n += 1
            if n == k: return cur.val
            cur = cur.right
                        
            
        

        # recursion
        vals = []

        def dfs(node):
            if not node or len(vals) >= k:
                return

            dfs(node.left)
            vals.append(node.val)
            dfs(node.right) 
        dfs(root)
        return vals[k - 1]

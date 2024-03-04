# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        # vals = defaultdict(list)
        # def dfs(node, depth):
        #     if not node:
        #         return
            
        #     vals[depth].append(node.val)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        
        # dfs(root, 0)
        # return vals.values()

        # bfs
        from collections import deque

        levels = []
        q = deque([root])

        while q:
            qlen = len(q)
            cur_level = []
            for i in range(qlen):
                node = q.popleft()
                cur_level.append(node.val)
                left, right = node.left, node.right
                if left: q.append(left)
                if right: q.append(right)
            
            levels.append(cur_level)
        
        return levels
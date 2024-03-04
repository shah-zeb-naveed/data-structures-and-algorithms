# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cur_max = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0 
            
            left_path_sum = dfs(node.left)
            right_path_sum = dfs(node.right)

            max_path_sum = max(
                node.val,
                node.val + left_path_sum,
                node.val + right_path_sum
            )

            print('max_path_sum: ', max_path_sum)

            cur_node_sum = max(max_path_sum, left_path_sum + node.val + right_path_sum)
            print('cur_node_sum: ', cur_node_sum)
            self.cur_max = max(cur_node_sum, self.cur_max)
            
            # could've also taken positive left and right and taken node.val out of max
            return max_path_sum

        dfs(root)
        return self.cur_max
            
            
        
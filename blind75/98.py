# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid_dfs(node, left_boundary, right_boundary):
            if not node: return True
            if not (left_boundary < node.val < right_boundary): return False   

            return (valid_dfs(node.left, left_boundary, node.val) and
                    valid_dfs(node.right, node.val, right_boundary))

        return valid_dfs(root, float('-inf'), float('inf'))

        # def dfs(root):   
        #     if not root:
        #         return None, None, True

            # Athough this solutioj works but is difficult to come up with
            # SHOULD'VE CHECKED THE SIMPLE NODE CONDITION ITSELF FIRST BEFORE CONTIUNUING
            # TO CHILDREN
            # THIS SOLUTIION DECIDES VALIDITY BASED ON CHILDREN'S RANGE AND VALIDITY
            # SIMPLER SOLUTION ABOVE DECIDES CHILDREN'S VALIDITY BASED ON PARENT
            # THERE IS A SUBTLE DIFFERENCE THAT SIMPLIFIES THE IMPLMENTATION
            # DEFINE BOUNDAYR FROM TOP-DOWN APPROACH
            # INSTEAD OF LOOKING AT FROM BOTTOM-UP

        #     min_left, max_left, valid_left = dfs(root.left)
        #     min_right, max_right, valid_right = dfs(root.right)

        #     valid = valid_left and valid_right
        #     print('Root: ', root.val)
        #     print('Valid: ', valid)
        #     if max_left is not None:
        #         valid = valid and max_left < root.val        
        #     if min_right is not None:
        #         valid = valid and root.val < min_right
        #     print('Mini right', min_right)
        #     print('Valid After: ', valid)
        #     minimum, maximum = root.val, root.val
        #     if min_left: minimum = min(minimum, min_left)
        #     if max_right: maximum = max(maximum, max_right)
        #     return minimum, maximum, valid

        # _, _, valid = dfs(root)
        # return valid



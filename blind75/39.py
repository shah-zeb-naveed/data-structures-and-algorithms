class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        
        def dfs(i, cur, summed):
            if summed == target:
                res.append(cur.copy())
                return
            
            if summed > target or i == len(candidates):
                return

            # with
            cur.append(candidates[i])
            dfs(i, cur, summed + candidates[i])

            # without
            cur.pop()
            dfs(i + 1, cur, summed)

        dfs(0, [], 0)

        return res
        
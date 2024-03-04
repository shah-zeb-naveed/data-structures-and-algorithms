class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        stack = []
        results = []

        def backtrack(n_closed, n_open):
            if n_closed == n_open == n:
                results.append(''.join(stack))
                return

            if n_open < n:
                stack.append('(')
                backtrack(n_closed, n_open + 1)
                stack.pop()

            if n_closed < n_open:
                stack.append(')')
                backtrack(n_closed + 1, n_open)
                stack.pop()
            
        backtrack(0, 0)
        return results

        # closing =  [')'] * n
        # opening =  ['('] * n

        # elements =  opening + closing
        # print(elements)

        # results = []
        # perm = []

        # def generate_permutations(i):
        #     # base case
        #     if i == len(elements) - 1:
        #         perm.append(elements[i])
        #         results.append(perm)
        #         print(results)
        #         return
            
        #     print('non base case')
        #     for j in range(i, len(elements)):
        #         if j > i and elements[j] == elements[j - 1]:
        #             print('same element. skipping')
        #             continue
                
        #         print('apapneding: ', elements[j])
        #         perm.append(elements[j])
        #         generate_permutations(j + 1)
        #         perm.pop()
        
        # generate_permutations(0)
        # print(results)


        
        
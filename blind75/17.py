class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digits_d = {'2':['a','b','c'], 
                '3':['d','e','f'],
                '4':['g','h','i'], 
                '5':['j','k','l'], 
                '6':['m','n','o'], 
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        combos = []
        combo = []
        def backtrack(i):
            if i == len(digits):
                combos.append(''.join(combo))
                return
            # print('----------')
            # print(i)
            # print(digits)
            # print(digits[i])
            
            for c in digits_d[digits[i]]:
                # print(c)
                combo.append(c)
                # print('i + 1: ', i + 1)
                backtrack(i + 1)
                combo.pop()
        
        backtrack(0)
        return combos
        
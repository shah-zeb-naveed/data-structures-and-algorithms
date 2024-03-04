class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter = dict()
        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1

        for c in t:
            if c not in counter:
                return False
            
            if counter[c] == 1:
                counter.pop(c)
            else:
                counter[c] -= 1
        
        return len(counter) == 0

        
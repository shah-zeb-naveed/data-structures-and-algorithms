class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
      if len(strs) == 1:
        return strs[0]

      prefix = []
      i = 0

      while i <= len(strs[0]) - 1:
        for w in strs[1:]:
          if i >= len(w) or w[i] != strs[0][i]:
            return ''.join(prefix)

        prefix.append(strs[0][i])
        i += 1

      return ''.join(prefix)


        
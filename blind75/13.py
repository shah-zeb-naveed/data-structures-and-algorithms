class Solution:
    def romanToInt(self, s: str) -> int:

      i = len(s) - 1

      value_map = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
      }

      sub_map = {
        'I' : ['V', 'X'],
        'X' : ['L', 'C'],
        'C' : ['D', 'M']
      }

      val = 0
      while i >= 0:
        sym_val = value_map[s[i]]
        if i < len(s) - 1:
          for neg_key in sub_map:
            if s[i] == neg_key and s[i + 1] in sub_map[neg_key]:
              sym_val *= -1
              break
        
        val += sym_val
        i -= 1
      
      return val
        
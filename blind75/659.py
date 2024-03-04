class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        
        print(encoded)
        return ''.join(encoded)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decoded = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            
            length = int(str[i : j])

            this_decoded = str[j + 1: j + 1 + length]
            i = j + 1 + length
        
            decoded.append(this_decoded)
            
        return decoded


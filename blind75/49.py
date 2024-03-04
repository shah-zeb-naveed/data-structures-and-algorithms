class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counter = defaultdict(list)

        for s in strs:
            char_array = [0] * 26
            for c in s:
                char_array[ord(c) - ord('a')] += 1

            counter[tuple(char_array)].append(s)

        return counter.values()

        
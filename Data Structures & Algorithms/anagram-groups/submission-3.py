class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord(char) - ord("a")] += 1
        #count the freq of the letters

            d[tuple(freq)].append(string)
        return list(d.values())
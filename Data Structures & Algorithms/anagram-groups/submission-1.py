class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            # 1. Frequency array for letters 'a' through 'z'
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            
            d[tuple(count)].append(word)

        return list(d.values())
        
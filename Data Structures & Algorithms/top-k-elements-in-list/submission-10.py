class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        # 2. Map frequency -> list of numbers with that frequency
        d_inverse = defaultdict(list)
        for n, count in d.items():
            d_inverse[count].append(n)  # Append to avoid overwriting

        #ordered_freqs = sorted(d_inverse.keys(), reverse=True)
        # tentativa de melhorar o algoritmo ao retirar o sort
        res = []

        for freq in range(len(nums), 0, -1):
            res.extend(d_inverse[freq])
            if len(res) >= k:
                return res

        return res
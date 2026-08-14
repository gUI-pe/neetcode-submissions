class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Contar as frequências - O(N)
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        # 2. Criar o array de baldes (buckets)
        # O tamanho é len(nums) + 1 porque a frequência máxima possível é len(nums)
        freq_buckets = [[] for _ in range(len(nums) + 1)]

        # 3. Preencher os baldes usando a frequência como índice - O(N)
        for num, freq in count.items():
            freq_buckets[freq].append(num)

        res = []

        # 4. Percorrer os baldes de trás para frente (da maior frequência para a menor) - O(N)
        for freq in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)

    # Inicializa o heap com os primeiros k elementos únicos
    unique = list(count.keys())
    heap = [(count[num], num) for num in unique[:k]]
    heapq.heapify(heap)  # O(k)

    # Itera sobre o restante mantendo o tamanho k
    for num in unique[k:]:
      if count[num] > heap[0][0]:
        heapq.heapreplace(heap, (count[num], num))  # ou heappushpop

    return [num for _, num in heap]
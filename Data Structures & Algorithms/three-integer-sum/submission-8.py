from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        trios = set()
        pares_vistos = set()
        
        # Guarda apenas o ÚLTIMO índice de cada valor: O(1) de espaço por número
        ultimo_indice = {n: i for i, n in enumerate(nums)}

        for i in range(size - 1):
            for j in range(i + 1, size):
                val1, val2 = nums[i], nums[j]
                
                # Se já processamos esse par de valores antes, pula imediatamente
                par = (val1, val2) if val1 <= val2 else (val2, val1)
                if par in pares_vistos:
                    continue
                pares_vistos.add(par)

                diff = -(val1 + val2)

                # Busca direta em O(1): sem laço for sobre k
                if diff in ultimo_indice:
                    k = ultimo_indice[diff]
                    # Garante que o terceiro elemento fica estritamente à frente de j
                    if k > j:
                        # Ordena apenas os 3 números para garantir unicidade no set
                        trios.add(tuple(sorted((val1, val2, diff))))

        return [list(t) for t in trios]
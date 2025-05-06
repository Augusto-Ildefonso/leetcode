"""
Minha resolução
Tempo: 1791 ms (vence 16.73%)
Memória: 18.47 MB (vence 79.37%)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

""" 
Resolução com menor tempo: 21 ms

Logo de cara podemos ver que o tempo dela será menor pois ela não tem dois for aninhados, desse modo o tempo dela seria O(n), enquanto a minha resolução é O(n^2) já que tem dois for aninhados
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i,n in enumerate(nums): # Cria um dicionário em que a chave é o número da lista e o valor é o seu índice
            indices[n] = i
    
        for i,n in enumerate(nums): # Itera para cada elemento da lista pegando o seu índice e o seu valor
            diff = target - n # Armazena a diferença do número atual até o número objetivo
            if diff in indices and indices[diff] != i: # Verifica se tem alguma chave que equivale a essa diferença e se ela é diferente do próprio número que temos
                return [i, indices[diff]] # Se tiver essa chave, retornamos o nosso i atual e o valor do dicionário que corresponde ao outro índice


"""
Resolução com menor consumo de memória: 18.2 MB
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # Itera sobre a lista
            for j in range(i + 1, len(nums)): # Itera novamente sobre a lista e começando do elemento seguinte
                if nums[j] == target - nums[i]: # Verifica se o número é o que queremos
                    return [i, j]
        return [] # Retorna lista vazia se não tiver um valor correto

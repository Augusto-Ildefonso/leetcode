"""
Minha solução (tive que ver algumas outras resoluções para entender como usar o ListNode)

Observações: 
- dificuldade em entender como usar o objeto e como funcionava a lista ligada
- criamos a dummy para poder já ter inicializado a lista antes de realizar as somas e criarmos os próximos nós e por isso passamos o próximo da dummy como retorno já que assim teremos de fato o primeiro elemento da lista
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        output = dummy
        carry = 0

        while l1 or l2 or carry:
            sumres = carry

            if l1:
                sumres += l1.val
                l1 = l1.next
            if l2:
                sumres += l2.val
                l2 = l2.next

            output.next = ListNode(sumres % 10)
            output = output.next
            carry = int(sumres // 10)
        
        return dummy.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_1 = []
        stack_2 = []
        fin_list = []
        l1_cur = l1
        while l1_cur.next != None:
            stack_1.append(l1_cur.val)
            
            l1_cur = l1_cur.next
            
        stack_1.append(l1_cur.val)
        
        l2_cur = l2
        while l2_cur.next != None:
            stack_2.append(l2_cur.val)
            
            l2_cur = l2_cur.next
            
        stack_2.append(l2_cur.val)
        
        tmp_add = 0
        while stack_1 != [] or stack_2 != []:
            if stack_1 != [] and stack_2 != []:
                add = stack_1.pop() + stack_2.pop() + tmp_add
            elif stack_1 != [] and stack_2 == []:
                add = stack_1.pop() + tmp_add
            else:
                add = stack_2.pop() + tmp_add
            if add > 9:
                tmp_add = 1
                add = add - 10
            else:
                tmp_add = 0
            fin_list.append(add)
            
        if tmp_add != 0:
            fin_list.append(tmp_add)
        
        first = True
        for val in fin_list:
            if first:
                ln = ListNode(val=val, next=None)
                first = False
            else:
                ln = ListNode(val=val, next=ln)
        return ln
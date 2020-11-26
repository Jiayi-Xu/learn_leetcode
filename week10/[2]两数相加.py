# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        方案一：add进位单独计算
        """
        # dummy = p = ListNode() #保存头结点，返回结果
        # add = 0
        # while l1 or l2 or add:
        #     # l1 l2长度不一时候，会有一个为None
        #     tmp = (l1.val if l1 else 0) + (l2.val if l2 else 0)
        #     p.next = ListNode((tmp+add)%10)
        #     p = p.next
        #     add = (tmp+add) // 10
        #     if l1 :
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        #
        # return dummy.next

        """
        方案二：直接用s代表对应位置的和
        """
        dummy = p = ListNode() #保存头结点，返回结果
        s = 0
        while l1 or l2 or s:
            # l1 l2长度不一时候，会有一个为None
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s = s // 10
            if l1 :
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)

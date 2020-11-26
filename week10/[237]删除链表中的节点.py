class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 先把下一个节点的值赋给它
        node.val = node.next.val
        # 再将node的下一个节点删除
        node.next = node.next.next
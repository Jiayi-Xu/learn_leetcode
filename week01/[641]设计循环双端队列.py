# 设计实现双端队列。 
# 你的实现需要支持以下操作： 
# 
#  
#  MyCircularDeque(k)：构造函数,双端队列的大小为k。 
#  insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。 
#  insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。 
#  deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。 
#  deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。 
#  getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。 
#  getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。 
#  isEmpty()：检查双端队列是否为空。 
#  isFull()：检查双端队列是否满了。 
#  
# 
#  示例： 
# 
#  MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
# circularDeque.insertLast(1);			        // 返回 true
# circularDeque.insertLast(2);			        // 返回 true
# circularDeque.insertFront(3);			        // 返回 true
# circularDeque.insertFront(4);			        // 已经满了，返回 false
# circularDeque.getRear();  				// 返回 2
# circularDeque.isFull();				        // 返回 true
# circularDeque.deleteLast();			        // 返回 true
# circularDeque.insertFront(4);			        // 返回 true
# circularDeque.getFront();				// 返回 4
#   
# 
#  
# 
#  提示： 
# 
#  
#  所有值的范围为 [1, 1000] 
#  操作次数的范围为 [1, 1000] 
#  请不要使用内置的双端队列库。 
#  
#  Related Topics 设计 队列 
#  👍 57 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        # 参数设置参考了https://leetcode-cn.com/problems/design-circular-deque/solution/python-liang-chong-jie-fa-zhi-zhen-chun-shu-zu-by-/
        # All values will be in the range of [0, 1000] 所以设置默认值为非负整数
        self._capacity = k  # 标记队列最大长度
        self._size = 0  # 标记当前队列长度
        self._dequeue = [-1 for _ in range(k)]  # 队列空间初始化
        self._front, self._rear = 0, 0  # front指向队头元素，rear指向队尾空闲位置

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # 如果队列满 则返回false
        if self.isFull():
            return False

        # if self._capacity is 10, and self._front is 0, which means self._data[0] is occupied and is the front.
        # Then an insertFront operation will put a new element on self._data[9],
        # so the new self._front will be (0 - 1) % 10, which is 9.
        if self.isEmpty():
            self._dequeue[self._front] = value
        else:
            self._front = (self._front - 1) % self._capacity
            self._dequeue[self._front] = value
        self._size += 1
        return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # 如果队列满 则返回false
        if self.isFull():
            return False
        # 假设队列长度10，
        # rear在位置9，（9+1）%10 =0 则插入位置在0
        # rear在位置0 则插入位置就是rear
        if self.isEmpty():
            self._dequeue[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._dequeue[self._rear] = value
        self._size += 1
        return True


        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        # 如果队列满 则返回false
        if self.isEmpty():
            return False
        # 初始化front对应的值 假设长度为10， front位置在3，删除后则对应为4
        self._dequeue[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        # 如果队列满 则返回false
        if self.isEmpty():
            return False
        # 初始化rear对应的值 假设长度为10， rear位置在9，删除后则对应为8
        self._dequeue[self._rear] = -1
        self._rear = (self._rear - 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return  self._dequeue[self._front]
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return self._dequeue[self._rear]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self._size == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self._size == self._capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)

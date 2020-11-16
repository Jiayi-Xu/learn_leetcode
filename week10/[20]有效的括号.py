class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        # 如果输入长度就为基数，则返回False
        if len(s) % 2 == 1:
            return False
        for ch in s:
            # 左括号入栈
            if ch in dic:
                stack.append(ch)
            # 右括号进行比较
            else:
                if stack and dic[stack[-1]] == ch:
                        stack.pop()
                else:
                    return False
        return len(stack)==0
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for ch in s:
            if ch == '[':
                stack.append(ch)

            elif ch == ']':
                encod_ch = []
                while stack[-1] != '[':
                    encod_ch.append(stack.pop())
                stack.pop()
                time = []
                while stack and stack[-1].isdigit():
                    time.append(stack.pop())
                stack.append(''.join(encod_ch[::-1])*int(''.join(time[::-1])))
            else:
                stack.append(ch)

        return ''.join(stack)


# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack, res, multi = [], "", 0
#         for c in s:
#             if c == '[':
#                 stack.append([multi, res])
#                 res, multi = "", 0
#             elif c == ']':
#                 cur_multi, last_res = stack.pop()
#                 res = last_res + cur_multi * res
#             elif '0' <= c <= '9':
#                 multi = multi * 10 + int(c)            
#             else:
#                 res += c
#         return res

# 参考链接：https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/

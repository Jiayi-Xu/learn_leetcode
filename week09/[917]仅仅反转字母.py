class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # 使用两个指针 i指向开始，j指向最后，每当i为字母时候，j相应往前移动以找到一个字母
        res = []
        j = len(S)-1
        for i in range(len(S)):
            if S[i].isalpha():
                # j不断前移直到找到字母
                while not S[j].isalpha():
                    j -= 1
                res.append(S[j])
                j -= 1
            else:
                res.append(S[i])


        return "".join(res)
class Solution:
    def reverseWords(self, s: str) -> str:
        lst =  s.strip().split()
        return ' '.join(lst[::-1])
        # return " ".join(reversed(s.split()))
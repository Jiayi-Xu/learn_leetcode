
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        lst = [1 for _ in range(n)]

        # p1,p2,p3指向首个丑数
        p1 = p2 = p3 = 0

        for i in range(1,n):
            lst[i] = minVal = min(lst[p1]*2, lst[p2]*3, lst[p3]*5)

            if lst[p1]*2 == minVal:
                p1 += 1
            if lst[p2]*3 == minVal:
                p2 += 1
            if lst[p3]*5 == minVal:
                p3 += 1

        return lst[-1]
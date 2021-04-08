class Solution:
    def myPow(self, x, n):

        if n == 0:
            return 1
        if n < 0:
            n, x = -n, 1 / x

        lower = self.myPow(x, n // 2)

        print(lower)

        return lower * lower * x if n % 2 else lower * lower

a = Solution()
a.myPow(2,10)
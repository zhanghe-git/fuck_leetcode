class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        step = [i for i in range(n)]
        step[0], step[1] = 1, 2
        for i in range(2, n):
            step[i] = step[i-1] + step[i-2]
        return step[n-1]

    # 递归方式，O(n2)复杂度, 超时
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)

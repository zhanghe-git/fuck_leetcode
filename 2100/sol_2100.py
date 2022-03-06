from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        result = []
        n = len(security)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i - 1] + 1
            if security[n - i ] >= security[n -i -1]:
                right[n - i -1] = right[len(security) -i] + 1
        for i in range(time, n-time):
            if left[i] >= time and right[i] >= time:
                result.append(i)
        return result

'''
class Solution:
    # 普通解法，暴力遍历，该方法在leetcode上会超时
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        result = []
        # 选出 pos 范围
        pending_pos = [ i for i in range(time, len(security) - time)]
        for pos in pending_pos:
            # 判断前面是否递减
            t1 = (security[pos - time : pos + 1] == sorted(security[pos-time : pos + 1], reverse = True))
            # 判断后面是否递增
            t2 = (security[pos : pos + time + 1 ] == sorted(security[pos: pos + time + 1]))
            if t1 and t2:
                result.append(pos)
        return result
'''

if __name__ == '__main__':
    s = Solution()
    print(s.goodDaysToRobBank([5,3,3,3,5,6,2], 2))

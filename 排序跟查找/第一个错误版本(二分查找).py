class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        
        while start < end:
            mid = start + (end - start) / 2  # 防止溢出
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        if start == end:
            return start
        


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW_COUNT, COL_COUNT = len(matrix), len(matrix[0])
        l, r = 0, ROW_COUNT*COL_COUNT - 1

        while l <= r:
            m = l + (r - l)//2
            val = matrix[m // COL_COUNT][m % COL_COUNT]
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return True
        return False

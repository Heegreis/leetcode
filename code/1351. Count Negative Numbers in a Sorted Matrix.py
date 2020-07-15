class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 無腦暴力解
        # negative_count = 0
        # for row in grid:
        #     for element in row:
        #         if element < 0:
        #             negative_count += 1
        # return negative_count

        # 一行解
        # return sum([1 for row in grid for element in row if element < 0])

        # while loop 且不從頭計算 (別人的解答)
        m, n = len(grid), len(grid[0])
        r, c, cnt = 0, n - 1, 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                cnt += m - r
                c -= 1
            else:
                r += 1
        return cnt

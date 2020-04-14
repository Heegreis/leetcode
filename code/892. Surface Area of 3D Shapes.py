class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x_axio = len(grid)
        near_num = 0
        box_num = 0
        for j in range(0, x_axio):
            for i in range(0, x_axio):
                num = grid[i][j]
                box_num += num
                if num > 0:
                    tower_near = num - 1
                    near_num += tower_near
                if i < x_axio - 1:
                    num_xP = grid[i + 1][j]
                    if num <= num_xP:
                        near_num += num
                    if num > num_xP:
                        near_num += num_xP
                if j < x_axio - 1:
                    num_yP = grid[i][j + 1]
                    if num <= num_yP:
                        near_num += num
                    if num > num_yP:
                        near_num += num_yP
        surface = (box_num * 6) - (near_num * 2)
        return surface
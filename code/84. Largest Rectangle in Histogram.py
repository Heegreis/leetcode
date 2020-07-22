class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 暴力解 會 time out
        """
        global_max_rect = 0
        for i, value in enumerate(heights):
            right_index = i
            for ri in range(i, len(heights)):
                if heights[ri] < value:
                    break
                right_index = ri
            left_index = i
            for li in range(i, -1, -1):
                if heights[li] < value:
                    break
                left_index = li
            cur_rect = (right_index - left_index + 1) * value
            if cur_rect > global_max_rect:
                global_max_rect = cur_rect
        return global_max_rect
        """

        # stack版 8行 解答
        s, res, heights = [], 0, [0] + heights + [0]
        for i, height in enumerate(heights):
            if len(s) > 0:
                while height < heights[s[-1]]:
                    top = s.pop()
                    res = max(res, heights[top] * (i - s[-1] - 1))
            s.append(i)
        return res
class Solution:
    # 使用84的程式碼
    def largestRectangleArea(self, heights):
        s, res, heights = [], 0, [0] + heights + [0]
        for i, height in enumerate(heights):
            if len(s) > 0:
                while height < heights[s[-1]]:
                    top = s.pop()
                    res = max(res, heights[top] * (i - s[-1] - 1))
            s.append(i)
        return res
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        if len(matrix) > 0:
            heights = [0] * len(matrix[0])
            # for row in matrix:
            #     for i in range(0, len(heights)): heights[i]+=1 if row[i]=="1" else 0
            for row in matrix:
                for i, v in enumerate(row):
                    if v == "1":
                        heights[i] += 1
                    else:
                        heights[i] = 0
                res = max(res, self.largestRectangleArea(heights))
        return res
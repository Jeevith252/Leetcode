class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area=0
        heights.append(0)
        stack=[]
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h= heights[stack.pop()]

                if not stack:
                    w=i
                else:
                    w = i-stack[-1]-1
                area = max(area, h*w)
            stack.append(i)
        return area
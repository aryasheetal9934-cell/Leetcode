class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_water=0
        left,right=0,n-1
        while left<right:
           width=right-left
           min_height=min(height[left],height[right])
           max_water=max(max_water,width*min_height)
           if height[left]<height[right]:
              left+=1
           else:
              right-=1
        return max_water
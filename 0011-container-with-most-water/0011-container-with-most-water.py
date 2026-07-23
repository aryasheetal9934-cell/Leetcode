class Solution:
   # Function to find max water container
   def maxArea(self, height):
       n = len(height)
       max_water = 0
       left, right = 0, n - 1  # Two pointers


       # Iterate while the two pointers haven't met
       while left < right:
           width = right - left  # Width between lines
           min_height = min(height[left], height[right])  # Height of container
           max_water = max(max_water, width * min_height)  # Update max area if current is larger


           # Move the pointer at the smaller height
           if height[left] < height[right]:
               left += 1
           else:
               right -= 1


       return max_water
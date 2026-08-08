class Solution(object):
   def fourSum(self, nums, target):
       """
       :type nums: List[int]
       :type target: int
       :rtype: List[List[int]]
       """
       nums.sort()  # Sort the array
       unique_quadruplets = set()
       n = len(nums)


       # Pick the first and second elements
       for i in range(n - 3):
           for j in range(i + 1, n - 2):
               val = target - nums[i] - nums[j]
               low, high = j + 1, n - 1


               # Two-pointer approach for remaining two numbers
               while low < high:
                   total = nums[low] + nums[high]


                   if total == val:
                       unique_quadruplets.add((nums[i], nums[j], nums[low], nums[high]))
                       low += 1
                       high -= 1
                   elif total < val:
                       low += 1  # Increase sum
                   else:
                       high -= 1  # Decrease sum


       return [list(quad) for quad in unique_quadruplets]  # Convert to list of lists



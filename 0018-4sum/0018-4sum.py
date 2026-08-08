class Solution(object):
   def fourSum(self, nums, target):

       nums.sort()  
       ans = set()
       n = len(nums)

       for i in range(n - 3):
           for j in range(i + 1, n - 2):
               val = target - nums[i] - nums[j]
               left, right = j + 1, n - 1

               while left < right:
                   total = nums[left] + nums[right]

                   if total == val:
                       ans.add((nums[i], nums[j], nums[left], nums[right]))
                       left += 1
                       right -= 1
                   elif total < val:
                       left += 1  
                   else:
                       right -= 1 


       return [list(quad) for quad in ans]  



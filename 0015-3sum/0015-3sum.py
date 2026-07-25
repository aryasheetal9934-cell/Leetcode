class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
         
       nums.sort()  
       ans = set()  
       n = len(nums)

       for i in range(n - 2):
           right, left = i + 1, n - 1
           target = -nums[i]  


           while right < left:
               total = nums[right] + nums[left]
               if total == target:
                   
                   ans.add((nums[i], nums[right], nums[left]))
                   right += 1
                   left-= 1
               elif total < target:
                   
                   right += 1
               else:
                   
                   left -= 1


    
       return [list(triplet) for triplet in ans]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
         
       nums.sort()  # Step 1: Sort the array
       ans = set()  # Step 2: Use a set to avoid duplicates
       n = len(nums)


       # Step 3: Iterate through the array
       for i in range(n - 2):
           low, high = i + 1, n - 1
           target = -nums[i]  # Step 4: We want two numbers that sum to -nums[i]


           # Step 5: Two-pointer approach
           while low < high:
               total = nums[low] + nums[high]
               if total == target:
                   # Found a valid triplet
                   ans.add((nums[i], nums[low], nums[high]))
                   low += 1
                   high -= 1
               elif total < target:
                   # Need a larger sum
                   low += 1
               else:
                   # Need a smaller sum
                   high -= 1


       # Step 6: Convert set of tuples to list of lists
       return [list(triplet) for triplet in ans]

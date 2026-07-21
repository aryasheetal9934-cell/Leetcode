class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        currsum=0
        for num in nums:
            currsum += num
            max_sum=max(max_sum,currsum)
            if(currsum<0):
             currsum=0
        return max_sum
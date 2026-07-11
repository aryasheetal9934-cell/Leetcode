class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()

        count = 1
        n = len(nums)

        for i in range(n - 2, -1, -1):
            if nums[i] != nums[i + 1]:
                count += 1
                if count == 3:
                    return nums[i]

        return nums[-1]

        
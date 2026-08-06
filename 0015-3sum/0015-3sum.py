class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        ans = set()
        n = len(nums)

        for i in range(n - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                total = nums[left] + nums[right]

                if total == target:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return [list(triplet) for triplet in ans]
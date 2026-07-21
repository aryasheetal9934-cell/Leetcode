class Solution:
    def permute(self, nums):
        ans = []

        def solve(temp):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return

            for num in nums:
                if num not in temp:
                    temp.append(num)
                    solve(temp)
                    temp.pop()

        solve([])
        return ans
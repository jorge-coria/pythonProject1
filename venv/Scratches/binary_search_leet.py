# Find target number in array of integers: return its index, else return -1
# Time Complexity: O(log n) | Memory: O(1)


class Solution:
    def search(nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            guess = nums[m]

            if guess == target:
                return m
            elif guess > target:
                r = m - 1
            else:
                l = m + 1

        return -1

u = [1, 2, 3, 4, 8, 9, 10]
print(Solution.search(u, 10))
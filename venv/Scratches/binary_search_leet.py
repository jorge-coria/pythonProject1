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
v = [-1, 8, 100, 2000, 20000, 300000]
w = [-50, -25, -1, 15, 25, 50, 100, 150, 1000, 20000]

print(Solution.search(u, 10)) # Index : 6
print(Solution.search(v, 20000)) # Index : 4
print(Solution.search(w, 25)) # Index : 4
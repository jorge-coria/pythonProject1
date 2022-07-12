# Iterate prices list using two pointers, updating maxProfit until it's returned at end of program
# Time Complexity: O(n) | Memory: O(1)

class Solution:
    def maxProfit(prices) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP

test1 = [9,8,5,6,7]
test2 = [1, 6, 8, 12]
test3 = [7, 1, 10, 5, 20]

print('Max Profit from: ' + str(test1) + ' is: ' + str(Solution.maxProfit(test1)))
print('Max Profit from: ' + str(test2) + ' is: ' + str(Solution.maxProfit(test2)))
print('Max Profit from: ' + str(test3) + ' is: ' + str(Solution.maxProfit(test3)))
# Iterate through list and save value:index pairs in empty dictionary until we find two numbers who's sum is target
# Time + Memory Complexity: O(n)

def twoSum(list, target):
    hash_map = {}

    for i, n in enumerate(list):
        diff = target - n
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[n] = i

    return []


print(twoSum([3, 10, 2, 3, 1], 4))
print(twoSum([3, 10, 2, 3, 1], 6))
print(twoSum([3, 10, 2, 3, 1], 5))

# Compares the count of each char of each string, return True if s is an anagram of t
# Time + Memory Complexity: O(s + t)

class Solution:
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

a, b = 'anagram', 'nagaram'
c, d = 'rat', 'car'
e, f = 'brag', 'grab'
r, s = 'disney', 'neydis'
t, u = 'neydis', 'disney'

print('Is '+ a + ' an anagram of ' + b + '? >> ' + str(Solution.isAnagram(a, b)))
print('Is '+ c + ' an anagram of ' + d + '? >> ' + str(Solution.isAnagram(c, d)))
print('Is '+ e + ' an anagram of ' + f + '? >> ' + str(Solution.isAnagram(e, f)))
print('Is '+ r + ' an anagram of ' + s + '? >> ' + str(Solution.isAnagram(r, s)))
print('Is '+ t + ' an anagram of ' + u + '? >> ' + str(Solution.isAnagram(t, u)))
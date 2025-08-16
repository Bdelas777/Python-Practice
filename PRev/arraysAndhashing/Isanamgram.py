# two strings are anagrams if they can be rearranged to form each other.
# Example: "anagram" and "nagaram" are anagrams.
# O(nlogn+mlogm)
def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# O(n) solution using a dictionary to count characters.
def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]] = 1+ countT.get(t[i],0)
        return countS == countT
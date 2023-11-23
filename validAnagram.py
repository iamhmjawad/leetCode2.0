class Solution:
    # Solution 1
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # creating a hash map for both strings
        countS, countT = {}, {}

        for char in s:
            # get function returns the value of the key, if the key is not present, it returns 0
            countS[char] = countS.get(char, 0) + 1

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        for key in countS:
            # if the character does not even exist in countT, the default will be 0
            if countS[key] != countT.get(key, 0):
                return False
        return True

    # Solution 2
    # return Counter(t) == Counter(s)

    # Solution 3
    # return sorted(s) == sorted(t)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        l = 0
        for r, c in enumerate(s2):
            if c not in count:
                while l < r:
                    count[s2[l]] += 1
                    l += 1
                l += 1 # skip over the current character
            else:
                count[c] -= 1
                while count[c] < 0:
                    count[s2[l]] += 1
                    l += 1
            
            if r - l + 1 == len(s1):
                return True
        return False


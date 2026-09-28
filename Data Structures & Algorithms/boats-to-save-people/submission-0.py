class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l < r:
            res += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
        res += int(l == r)
        return res
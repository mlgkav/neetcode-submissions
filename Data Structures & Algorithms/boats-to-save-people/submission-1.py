class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weight_count = [0] * (limit + 1)
        for p in people:
            weight_count[p] += 1

        i = 0
        for weight, count in enumerate(weight_count):
            for _ in range(count):
                people[i] = weight
                i += 1

        l, r = 0, len(people) - 1
        res = 0
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            res += 1
        res += int(l == r)
        return res
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEat(speed):
            t = 0
            for p in piles:
                t += math.ceil(float(p)/speed)
            return t <= h
    
        while l <= r:
            m = (l + r)//2
            print(m)
            if canEat(m):
                r = m - 1
            else:
                l = m + 1
        
        return l
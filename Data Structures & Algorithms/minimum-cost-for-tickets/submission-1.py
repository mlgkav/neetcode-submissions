from collections import deque
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp_7 = deque()
        dp_30 = deque()
        dp = 0
        
        for day in days:
            # 1. Remove 7-day and 30-day passes that have expired
            while dp_7 and dp_7[0][0] + 7 <= day:
                dp_7.popleft()
            while dp_30 and dp_30[0][0] + 30 <= day:
                dp_30.popleft()
            
            # 2. Append current day with potential future costs
            dp_7.append((day, dp + costs[1]))
            dp_30.append((day, dp + costs[2]))
            
            # 3. Take the minimum of buying a 1-day pass, 7-day pass, or 30-day pass
            dp = min(dp + costs[0], dp_7[0][1], dp_30[0][1])
            
        return dp
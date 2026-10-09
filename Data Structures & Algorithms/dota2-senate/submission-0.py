from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque([i for i, senator in enumerate(senate) if senator == "R"])
        d_queue = deque([i for i, senator in enumerate(senate) if senator == "D"])

        next_pos = len(senate)
        while r_queue and d_queue:
            r_pos = r_queue.popleft()
            d_pos = d_queue.popleft()

            if r_pos < d_pos:
                r_queue.append(next_pos)
            else:
                d_queue.append(next_pos)
            next_pos += 1

        return "Radiant" if r_queue else "Dire"

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        res = 0
        prev_dest_time = 0
        for pos, spd in cars:
            dest_time = (target - pos)/spd
            if dest_time > prev_dest_time:
                res += 1
                prev_dest_time = dest_time
        
        return res

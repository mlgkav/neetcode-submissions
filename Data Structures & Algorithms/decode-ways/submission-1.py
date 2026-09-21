class Solution:
    def numDecodings(self, s: str) -> int:
        # fibonacci style solution using O(1) space
        if s[0] == "0":
            return 0
        ways_n_minus_1 = ways_n_minus_2 = 1
        for i in range(1, len(s)):
            digit = int(s[i])
            prev_digit = int(s[i - 1])
            
            if digit == 0:
                if prev_digit != 1 and prev_digit != 2:
                    return 0
                ways_n_minus_1, ways_n_minus_2 = ways_n_minus_2, 0
                print(ways_n_minus_1, ways_n_minus_2)
                continue

            ways_n = ways_n_minus_1
            if (prev_digit == 1 or 
                prev_digit == 2 and 0 <= digit <= 6):
                ways_n += ways_n_minus_2
            
            ways_n_minus_1, ways_n_minus_2 = ways_n, ways_n_minus_1
            print(ways_n_minus_1, ways_n_minus_2)
        
        return ways_n_minus_1
        




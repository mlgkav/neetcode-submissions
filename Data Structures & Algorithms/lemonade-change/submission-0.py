class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                fives -= 1
                tens += 1
            elif bill == 20:
                if tens:
                    tens -= 1
                else:
                    fives -= 2
                fives -= 1
            
            if fives < 0 or tens < 0:
                return False

        return True

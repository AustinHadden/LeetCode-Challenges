class Solution:
    def numberOfSteps (self, num: int) -> int:
        numSteps = 0
        while(num != 0):
            if(num % 2 == 0):
                num = num/2
            else:
                num -= 1
            numSteps +=1
        return numSteps
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 1
        lim = int((-1+(1+8*N)**0.5)/2)
        
        for k in range(2,lim+1):    
            q = N//k
            if k%2 == 0:
                l, r = q-k//2, q-k//2 + k  
            else:
                l, r = q-k//2-1, q-k//2 -1+k
            if r*(r+1)//2-l*(l+1)//2 == N:
                ans+=1
        return ans
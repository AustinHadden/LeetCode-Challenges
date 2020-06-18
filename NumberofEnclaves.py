class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        stack = []
        for i in range(m):
            if A[i][0]==1:
                A[i][0]=2
                if 1<=i<=m-2 and A[i][1]==1 and n>=2:
                    A[i][1]=2
                    stack.append((i,1))
            if A[i][-1]==1:
                A[i][-1]=2
                if 1<=i<=m-2 and A[i][-2]==1 and n>=2:
                    A[i][-2]=2
                    stack.append((i,-2))
        for j in range(n):
            if A[0][j]==1:
                A[0][j]=2
                if 1<=j<=n-2 and A[1][j]==1 and m>=2:
                    A[1][j]=2
                    stack.append((1,j))
            if A[-1][j]==1:
                A[-1][j]=2
                if 1<=j<=n-2 and A[-2][j]==1 and m>=2:
                    A[-2][j]=2
                    stack.append((-2,j))
        while stack:
            site = stack.pop()
            for pos in ((-1,0),(1,0),(0,-1),(0,1)):
                if A[site[0]+pos[0]][site[1]+pos[1]]==1:
                    A[site[0]+pos[0]][site[1]+pos[1]]=2
                    stack.append((site[0]+pos[0],site[1]+pos[1]))
        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j]==1:
                    count += 1
        return count
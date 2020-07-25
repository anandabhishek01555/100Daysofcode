class Solution:
    def partition(self, A, pivot):
            l=0
            h=len(A)-1
            i = ( l - 1 )
            x = A[h]
            for j in range(l , h):
                if   A[j] <= x:
                    i = i+1
                    A[i],A[j] = A[j],A[i]
            A[i+1],A[h] = A[h],A[i+1]
            return (i+1)
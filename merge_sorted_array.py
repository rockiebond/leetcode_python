class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m-1
        j = n-1
        k = m+n-1
        while k>=0:
            if j<0 or (i>=0 and A[i]>B[j]):
                A[k]=A[i]
                k=k-1
                i=i-1
            else:
                A[k]=B[j]
                k=k-1
                j=j-1
solution=Solution()
A=[1,3,5,0,0]
B=[2,4]
solution.merge(A,3,B,2)
print A

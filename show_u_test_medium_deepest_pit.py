# Base on mike solution, O(n) is possiable to achieve it.

# as long as see it into three status:
# 1. non status
# 2. Descending ~ falling status
# 3. Ascending ~ raising status

 A[0] =  0
 A[1] =  1
 A[2] =  3
 A[3] = -2
 A[4] =  0
 A[5] =  1
 A[6] =  0
 A[7] = -3
 A[8] =  2
 A[9] =  3

N = len(A)

 for i in range(0, N - 2):
    #  code here...
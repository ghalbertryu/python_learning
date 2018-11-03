import numpy as np

A = np.arange(3, 15)
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# print(A[3])  # 6

A = np.arange(3, 15).reshape((3, 4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""
# print(A[2]) # [11 12 13 14]
# print(A[1][1])      # 8
# print(A[1, 1])      # 8
# print(A[1, 1:3])    # [8 9]

for row in A:
    continue
    print(row)
"""    
[ 3,  4,  5, 6]
[ 7,  8,  9, 10]
[11, 12, 13, 14]
"""

for column in A.T:
    continue
    print(column)
"""  
[ 3,  7,  11]
[ 4,  8,  12]
[ 5,  9,  13]
[ 6, 10,  14]
"""

A = np.arange(3, 15).reshape((1, 3, 4))
print(A.flatten()) # 轉為一階矩陣
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for item in A.flat:
    print(item)
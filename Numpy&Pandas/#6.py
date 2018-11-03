import numpy as np

A = np.arange(2, 14).reshape((3, 4))

A = np.array([[ 0, 4, 4, 5],
               [ 6, 7, 8, 9],
               [10,11,0,23]])

# print(np.argmin(A))  # 最小元素index
# print(np.argmax(A))  # 最大元素index

# print(np.mean(A))        # 平均數
# print(np.average(A))     # 平均數

# print(np.median(A))       # 中位數

# print(np.diff(A)) # 兩元素相差
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]

# print(np.nonzero(A)) # 非零元素向量
# (array([0,0,0,0,1,1,1,1,2,2,2,2]),array([0,1,2,3,0,1,2,3,0,1,2,3]))

A = np.arange(14,2, -1).reshape((3,4))
# array([[14, 13, 12, 11],
#       [10,  9,  8,  7],
#       [ 6,  5,  4,  3]])

# print(np.sort(A)) # column排序
# array([[11,12,13,14]
#        [ 7, 8, 9,10]
#        [ 3, 4, 5, 6]])
# A=np.random.random((2,2,2))
print(A)
print(np.transpose(A)) # 轉置矩陣
# print(A.T)
# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])
# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])
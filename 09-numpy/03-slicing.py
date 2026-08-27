import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# array[start:end:step]

print(array[0]) # [1 2 3 4]
print(array[1]) # [5 6 7 8]
print(array[2]) # [9 10 11 12]
print(array[3]) # [13 14 15 16]

print(array[-1]) # [13 14 15 16]
print(array[-2]) # [9 10 11 12]
print(array[-3]) # [5 6 7 8]
print(array[-4]) # [1 2 3 4]

print(array[0:3])
# [[1 2 3 4] 
#  [5 6 7 8] 
#  [9 10 11 12]]

print(array[0:4:2])
# [[1 2 3 4] 
#  [9 10 11 12]]

print(array[::-1])
# [[13 14 15 16]
#  [9 10 11 12]
#  [5 6 7 8]
#  [1 2 3 4]]

print(array[:, 3])
print(array[:, -1])
# [4 8 12 16]

print(array[:, 0:3])
# [[1 2 3]
#  [5 6 7]
#  [9 10 11]
#  [13 14 15]]

print(array[:, ::2])
# [[1 3]
#  [5 7]
#  [9 11]
#  [13 15]]

print(array[0:2, 0:2])
# [[1 2]
#  [5 6]]

print(array[2:4, 0:2])
# [[9 10]
#  [13 14]]
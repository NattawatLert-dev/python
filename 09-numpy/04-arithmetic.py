import numpy as np

# Scalar arithmetic

array = np.array([1, 2, 3])

print(array + 1) # [2 3 4]
print(array - 2) # [-1 0 1]
print(array * 3) # [3 6 9]
print(array / 4) # [0.25 0.5 0.75]
print(array ** 5) # [ 1 32 243]

# Vectorized math funcs

print(np.sqrt(array)) # [1.         1.41421356 1.73205081]

array1 = np.array([1.01, 2.5, 3.99])

print(np.round(array1)) # [1. 2. 4.]
print(np.floor(array1)) # [1. 2. 3.]
print(np.ceil(array1))  # [2. 3. 4.]
print(np.pi)

# Elemet-wise arithmetic

array2 = np.array([1, 2, 3])
array3 = np.array([4, 5, 6])

print(array2 + array3) # [5 7 9]
print(array2 - array3) 
print(array2 * array3) 
print(array2 / array3) 
print(array2 ** array3)

# Comparison operator

number = np.arange(1, 11).reshape(2, 5)
print(number % 2 == 0)
# [[False True False  True False]
#  [ True False True False True]]

Odd = number[number % 2 == 0]
print(Odd)
# [ 2  4  6  8  10]

number[number % 2 == 0] = 0
print(number)
# [[1 0 3 0 5]
#  [0 7 0 9 0]]
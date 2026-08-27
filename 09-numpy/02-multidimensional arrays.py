import numpy as np

array = np.array([
    [
        ['A', 'B', 'C'], 
        ['D', 'E', 'F'], 
        ['G', 'H', 'I']
    ],

    [
        ['J', 'K', 'L'], 
        ['M', 'N', 'O'], 
        ['P', 'Q', 'R']
    ],

    [
        ['S', 'T', 'U'], 
        ['V', 'W', 'X'], 
        ['Y', 'Z', ' ']
    ]
])

word = array[2, 0, 1] + array[1, 0, 2] + array[0, 1, 1]
print(word) # TLE

print(array.shape) # (3, 3, 3) (ชั้น, จำนวน row, จำนวน column)
print(array.ndim) # 3 (number of dimension)
print(array.size) # 27

import os
import numpy as np

# clear the console
if os.name == 'nt':
    os.system('cls')
elif os.name == 'posix':
    os.system('clear')
else:
    print('\n' * 100) # just print some lines

# Q
# What is the transpose of this vector?
# | 25|
# |  2|
# | -3|
# |-33|

# A
# Using code the transpose looks like the same vector since their dimension is 1? 
# v = np.array([25,2,-3,-23], dtype=np.short)
# print(v.T) # |25 2 -3 -23|

# Q
# Using algebraic notation, what are the dimensions of this matrix Y?
# |  42   4   7 99 |
# | -99  -3  17 22 |

# A
# The dimensions of the matrix are 2x4, indicated that it is a matrix with 2 rows and 4 columns 
# v = np.array([
#     [42, 4, 7,99],
#     [99,-3,17,22]]
# )
# print(v.shape) # (2,4)

# Q
# Using algebraic notation, what is the position of the element in this matrix Y with the value of 17

# A
# The position is 2 ,3. Including the fact that counting starts at zeros in arrays, 1,2 instead
# In algebraic notation: Y 2,3
# v = np.array([
#     [42, 4, 7,99],
#     [99,-3,17,22]]
# )
# print(v[1][2])

# Q
# What is Y transpose
# |  42   4   7 99 |
# | -99  -3  17 22 |

# A
# Y transpose equals the following vector:
# | 42,-99 |
# |  4, -3 |
# |  7, 17 |
# | 22, 99 |
# v = np.array([
#     [42, 4, 7,99],
#     [-99,-3,17,22]]
# )
# print(v.T)
    
# Q
# What is the Haamard product of these matrices
# | 25,10 |   | -1,7 |
# |       | O |      |
# | -2,1  |   | 10,8 |

# A    
# v1 = np.array([[25,10],[-2,1]])
# v2 = np.array([[-1,7],[10,8]])
# print(v1*v2)

# Q
# What is the dotproduct of the tensors w and x?
# w = np.array([-1,2,-2])
# x = np.array([5,10,0])

# A
v = [a*b for a, b in zip(w,x)]
print(sum(v))
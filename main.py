import numpy as np

zeros = np.zeros((8,8), dtype=float)
# print(zeros)

v = np.array([
    [42, 4, 7,99],
    [99,-3,17,22]]
)
# print(v.T)

def subtract(V,n):
    return V-n
# print(subtract(np.array([2,3,4]), 1))

def power(V,n):
    pow = [v**n for v in V]
    return pow
# print(power([1,2,4], 2))

def powernp(V,n):
    return V**n
# print(powernp(np.array([2,3,4]), 2))

def hadamard(Y1, Y2):
    return Y1*Y2
# print(hadamard(np.array([2,3]),np.array([3,3])))

v = np.array([2,3,5,6])
# print(v.sum())

arr = np.array([
    [ 2, 3],
    [ 4, 6],
    [ 8,12],
    [16,24],
    [32,48]])

print(arr.sum(axis=0)) # counting all cols
print(arr.sum(axis=1)) # counting all rows
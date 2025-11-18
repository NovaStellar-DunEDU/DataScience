import numpy as np

arr = np.array({1,2,3,4})
print("Array from 1-4", arr)

zeros = np.zeros((3,3))
print("Zeros Array: \n", zeros)

ones = np.ones(((2,4)))
print("Ones Array: \n", ones)

range_array = np.arange(1,10,3)
print("Range 1-10:\n", range_array)

linspace_array = np.linspace(0,1,5)
print("Linspace Array:\n", linspace_array)

rows = cols = 1000
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print("Manual 1000x1000 matrix: \n", matrix)

zeros_matrix = np.zeros((1000,1000))
print("Numpy 1000x1000 matrix: \n", zeros_matrix)

data = list(range(10))
print("Data:\n", data)

result = []
for x in data:
    result.append(x*10)
print("Manual Result:\n", result)

math_array = np.arange(10)
math_result = math_array * 10
print("Numpy Math Result: \n", math_result)

print("Shape of zeros matrix:\n", zeros_matrix.shape)
#tuple of 1000 by 1000
print("Number of Dimensions of zeroes matrix: \n", zeros_matrix.ndim)

newShapeArray = zeros_matrix.reshape(10, 100000)
print("New Shape of Zeros Matrix:\n", newShapeArray)
print("Shape of newly shaped matrix:\n", newShapeArray.shape)
print("Number of Dimensions of newly shaped matrix: \n", newShapeArray.ndim)

slicedArray = np.arange(20).reshape(4,5)
print("Sliced Array:\n", slicedArray)
print("Second row, third column: \n", slicedArray[1,2])
print("All rows, first column only: \n", slicedArray[:,0])
print("Subset of rows and columns:\n", slicedArray[1:3, 2:5])
print("Flattened:\n", slicedArray.flatten())

a = np.arange(1,6)
b = np.arange(6,11)
print("A array = ", a)
print("B array = ", b)

print("Add: ", a+b)
print("Subtract: ", a-b)
print("Multiply: ", a*b)
print("Divide: ", a/b)

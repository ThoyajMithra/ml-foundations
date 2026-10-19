import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[1,3,6],[2,2,8],[2,9,5]])


print(A+B)
print(A-B)
print(A@B)
print(A*B)
print(np.linalg.det(A))
print(np.eye(4))
print(np.maximum(0,A))



matrix = np.array([[1, 2, 3], [4, 5, 6]])
bias = np.array([10, 20, 30])
print(matrix + bias)
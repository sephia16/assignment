import numpy as np

M = np.arange(2,27)
print(M)


M = M.reshape(5,5)
print(M)

# for i in range(1,4):
#     for j in range(1,4):
#         M[i,j] = 0
M[1:-1,1:-1] = 0
print(M)

M = M@M
print(M)


v = M[0,0:5]
print(v)

print(np.sqrt(v@v))
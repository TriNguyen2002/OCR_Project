import numpy as np

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])


# u = np.unique(a)

indices_ls = np.unique(a, True)

print(indices_ls)
# for x in (0,4):
#     for y in (0,4):
#         a[x,:] = 1
#         a[:,y] = 1
#         a[2,2] = 9


# print(a)
# print(f"the shape of the matrix is {a.shape}")
import numpy as np

a = np.array([[1,2,3],[4,5,6]])

# get dimension
x = (a.ndim)
#   get shape
x = (a.shape)
#   get type 
x = (a.dtype)
#   get size of type
x = (a.itemsize)
#   get element size
x = (a.size)
#   get total size
x = (a.nbytes)

"""
    Axes are defined for arrays with more than one dimension
    EX: 2-d has axis 0 & axis 1
"""
mat = np.zeros(5)

mat = np.full((2,2),12)

mat = np.full_like(a, 12)

# get unique value frequency, will return 2 ndarry (unique and indices_list)
indices_ls = np.unique(a, return_counts = True)

# return unique value indices, will return 2 ndarry (unique and indices_list)
indices_ls = np.unique(a,return_index=True)
 

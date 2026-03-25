import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """

    A = np.asarray(A, dtype=float)
    elements = []
    for idx_i, i in enumerate(A):
        for idx_j, j in enumerate(i):
            if idx_i == idx_j:
                elements.append(j)
    
    if len(elements) == A.shape[0]:
        return np.sum(elements)
        
    
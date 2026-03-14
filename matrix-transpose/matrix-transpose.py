import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """

    rows = np.shape(A)[0]
    columns = np.shape(A)[1]

    A_transpose = []
    for column in range(columns):
        B = []      # Temperary Matrix
        for row in range(rows):
            B.append(A[row][column])
        A_transpose.append(B)

    return np.asarray(A_transpose, dtype=float)
import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """

    ## Method 1
    # v = np.asarray(v, dtype=float)

    # vec_v_len = len(v)
    # zeros_matrix = np.zeros((vec_v_len, vec_v_len))

    # for idx_i, i in enumerate(zeros_matrix):
    #     for idx_j, j in enumerate(i):
    #         if idx_i == idx_j:
    #             zeros_matrix[idx_i][idx_j] = v[idx_i]

    # diag_matrix = zeros_matrix
    # return diag_matrix

    ## Method 2
    return np.diag(v)
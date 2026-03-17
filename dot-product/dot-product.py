import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    try:
        x_array = np.asarray(x)
        y_array = np.asarray(y)
        
        product = np.dot(x_array, y_array)
        return product
    except:
        raise ValueError
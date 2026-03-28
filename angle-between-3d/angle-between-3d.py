import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    v = np.asarray(v, dtype=float)
    w = np.asarray(w, dtype=float)

    mag_v = np.linalg.norm(v)
    mag_w = np.linalg.norm(w)
    
    if (mag_v < 0) or (mag_w < 0):
        return np.nan

    cos_theta = np.clip(np.dot(v,w) / (mag_v * mag_w), -1, 1)
    theta = np.arccos(cos_theta)

    return theta
import numpy as np
from scipy.linalg import expm # type: ignore
# Based on the original M-file by Ashish Tewari (2006), extracted from the book:
# "Atmospheric and Space Flight Dynamics: Modeling and Simulation with MATLAB and Simulink"
# This is a Python adaptation made by Diego Baeza for educational purposes.

def quaternion(C):
    """
    Converts a rotation matrix to a unit quaternion.

    Given a 3x3 rotation matrix `C`, this function computes the corresponding
    quaternion `q = [q1, q2, q3, q4]`, where the first three elements represent 
    the vector part and the last element (`q4`) is the scalar part.

    Parameters
    ----------
    C : numpy.ndarray
        A 3x3 rotation matrix. Must be orthogonal and with determinant 1.

    Returns
    -------
    q : numpy.ndarray
        A 1D array of shape (4,) representing the quaternion [q1, q2, q3, q4].

    Notes
    -----
    - The algorithm selects the dominant quaternion component to ensure numerical stability.
    - The output quaternion is normalized.
    """
    T = np.linalg.trace(C)
    qsq = np.array([
        (1+2*C[0,0]-T)/4,
        (1+2*C[1,1]-T)/4,
        (1+2*C[2,2]-T)/4,
        (1+T)/4
    ])
    i = np.argmax(qsq)
    x = qsq[i]
    q = np.zeros(4)
    if i == 3:  
        q[3] = np.sqrt(x)
        q[0] = (C[1, 2] - C[2, 1]) / (4 * q[3])
        q[1] = (C[2, 0] - C[0, 2]) / (4 * q[3])
        q[2] = (C[0, 1] - C[1, 0]) / (4 * q[3])
    elif i == 2:  
        q[2] = np.sqrt(x)
        q[0] = (C[0, 2] + C[2, 0]) / (4 * q[2])
        q[1] = (C[2, 1] + C[1, 2]) / (4 * q[2])
        q[3] = (C[0, 1] - C[1, 0]) / (4 * q[2])
    elif i == 1:  
        q[1] = np.sqrt(x)
        q[0] = (C[0, 1] + C[1, 0]) / (4 * q[1])
        q[2] = (C[2, 1] + C[1, 2]) / (4 * q[1])
        q[3] = (C[2, 0] - C[0, 2]) / (4 * q[1])
    elif i == 0:  
        q[0] = np.sqrt(x)
        q[1] = (C[0, 1] + C[1, 0]) / (4 * q[0])
        q[2] = (C[0, 2] + C[2, 0]) / (4 * q[0])
        q[3] = (C[1, 2] - C[2, 1]) / (4 * q[0])
    return q

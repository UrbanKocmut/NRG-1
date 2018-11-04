import numpy as np


# CYKA http://tizian.cs.uni-bonn.de/publications/BaudsonKlein.pdf


# https://math.stackexchange.com/questions/1076177/3d-coordinates-of-circle-center-given-three-point-on-the-circle
def midpoint(p1, p2, p3):
    u1 = p2 - p1
    w1 = (p3 - p1) * u1
    u = u1 / np.linalg.det(u1)
    w = w1 / np.linalg.det(w1)
    v = w * u
    bx = (p2 - p1) * u
    cx = (p3 - p1) * u
    cy = (p3 - p1) * v
    h = ((cx - bx / 2) ** 2 + cy ** 2 - (bx / 2) ** 2) / (2 * cy)
    return p1 + (bx / 2) * u + h * v


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


class Tetraeder:

    # ZRAČUNA KROGLO KI OBDAJA  TETRAEDER
    def centerPoint(self):
        p1 = self.points[0]
        p2 = self.points[1]
        p3 = self.points[2]
        p4 = self.points[3]
        M1 = np.linalg.det(np.array([
            [p1[0], p1[1], p1[2], 1],
            [p2[0], p2[1], p2[2], 1],
            [p3[0], p3[1], p3[2], 1],
            [p4[0], p4[1], p4[2], 1]
        ]))
        M2 = np.linalg.det(np.array([
            [p1 * p1, p1[1], p1[2], 1],
            [p2 * p2, p2[1], p2[2], 1],
            [p3 * p3, p3[1], p3[2], 1],
            [p4 * p4, p4[1], p4[2], 1]
        ]))
        M3 = np.linalg.det(np.array([
            [p1 * p1, p1[0], p1[2], 1],
            [p2 * p2, p2[0], p2[2], 1],
            [p3 * p3, p3[0], p3[2], 1],
            [p4 * p4, p4[0], p4[2], 1]
        ]))
        M4 = np.linalg.det(np.array([
            [p1 * p1, p1[0], p1[1], 1],
            [p2 * p2, p2[0], p2[1], 1],
            [p3 * p3, p3[0], p3[1], 1],
            [p4 * p4, p4[0], p4[1], 1]
        ]))
        M5 = np.linalg.det(np.array([
            [p1 * p1, p1[0], p1[1], p1[2]],
            [p2 * p2, p2[0], p2[1], p2[2]],
            [p3 * p3, p3[0], p3[1], p3[2]],
            [p4 * p4, p4[0], p4[1], p4[2]]
        ]))
        # CAN THROW EXCEPTION IF M1 IS 0, BE CAREFULL!!
        x0 = M2 / (2 * M1)
        y0 = M3 / (2 * M1)
        z0 = M4 / (2 * M1)
        r2 = x0 ** 2 + y0 ** 2 + z0 ** 2 - (M5 / M1)

        self.center = np.array([x0, y0, z0])
        self.r = r2 ** 0.5

    def __init__(self, points):
        self.points = np.array(points)

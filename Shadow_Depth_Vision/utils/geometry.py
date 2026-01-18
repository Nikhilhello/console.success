import numpy as np

def inverse_square_law(intensity, distance):
    """
    I ∝ 1 / d^2
    """
    if distance <= 0:
        return 0
    return intensity / (distance ** 2)

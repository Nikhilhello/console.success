import numpy as np
from utils.constants import CALIBRATION_K

def estimate_depth_cm(shadow_area):
    """
    Physics-based depth estimation using inverse square relationship
    Z = K / sqrt(ShadowArea)
    """
    if shadow_area <= 0:
        return 999.0

    depth = CALIBRATION_K / np.sqrt(shadow_area)
    return round(depth, 2)

from utils.constants import ACTION_THRESHOLD_CM

def classify_action(depth_cm):
    """
    Classify action based on depth threshold
    """
    if depth_cm < ACTION_THRESHOLD_CM:
        return "Touching Face / Eating"
    else:
        return "No Action"

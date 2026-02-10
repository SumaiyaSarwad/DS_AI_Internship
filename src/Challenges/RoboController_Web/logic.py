# logic.py

from data import DISTANCES, DEFAULT_DISTANCE

def calculate_distance(source, destination):
    return DISTANCES.get((source, destination), DEFAULT_DISTANCE)

def decide_action(obstacle):
    if obstacle == "Human":
        return "Slow and Move Safely", "Very Slow"
    elif obstacle == "Animal":
        return "Move Carefully", "Slow"
    elif obstacle == "Vehicle":
        return "Change Path", "Slow"
    elif obstacle == "Wall":
        return "Avoid Wall", "Slow"
    else:
        return "Move Forward", "Fast"

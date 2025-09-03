import math
from typing import Dict

def calculate_anchor_decay(initial_weight: float, decay_rate: float, time_elapsed: int) -> float:
    """
    Calculates current weight of an audit anchor after exponential decay.
    
    Args:
        initial_weight: Initial severity weight (A₀)
        decay_rate: Exponential decay rate (λ)
        time_elapsed: Number of audit cycles since creation (t)
        
    Returns:
        Decayed anchor weight
    """
    return initial_weight * math.exp(-decay_rate * time_elapsed)

def normalize(prob_dict: Dict[str, float]) -> Dict[str, float]:
    """
    Normalizes a probability dictionary so all values sum to 1.
    
    Args:
        prob_dict: Dictionary of probabilities
        
    Returns:
        Normalized dictionary
    """
    total = sum(prob_dict.values())
    if total == 0:
        return {k: 0 for k in prob_dict.keys()}
    return {k: v / total for k, v in prob_dict.items()}

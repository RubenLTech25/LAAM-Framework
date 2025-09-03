import math
import random
from typing import Dict, Literal

def calculate_anchor_decay(initial_weight: float, decay_rate: float, time_elapsed: int) -> float:
    """
    Calculates the current weight of an audit anchor after exponential decay.
    Args:
        initial_weight: The initial severity weight of the anchor (A₀).
        decay_rate: The exponential decay rate (λ). Higher values mean faster decay.
        time_elapsed: The number of audit cycles since the anchor was created (t).
    Returns:
        The decayed anchor weight.
    """
    return initial_weight * math.exp(-decay_rate * time_elapsed)

def normalize(prob_dict: dict) -> dict:
    """
    Normalizes a probability dictionary so all values sum to 1.
    """
    total = sum(prob_dict.values())
    return {k: v / total for k, v in prob_dict.items()}

class BayesianAuditor:
    """
    A class to model the Bayesian belief updating system for an auditor.
    """
    def __init__(self, sector: str = 'tax'):
        self.sector_priors = {
            'tax': {'C': 0.6, 'R': 0.3, 'E': 0.1},
            'healthcare': {'C': 0.5, 'R': 0.35, 'E': 0.15},
            'labor': {'C': 0.7, 'R': 0.25, 'E': 0.05}
        }
        self.beliefs = self.sector_priors.get(sector, {'C': 0.6, 'R': 0.3, 'E': 0.1}).copy()
        self.signal_likelihood = {
            'clean': {'C': 0.9, 'R': 0.4, 'E': 0.05},
            'vague': {'C': 0.05, 'R': 0.4, 'E': 0.3},
            'missing_doc': {'C': 0.02, 'R': 0.3, 'E': 0.6},
            'unsafe_condition': {'C': 0.0, 'R': 0.5, 'E': 0.2}
        }

    def update_beliefs(self, signal: str):
        """
        Updates the auditor's beliefs about the auditee's type (C, R, E)
        using Bayes' Theorem.
        """
        posterior_numerator = {}
        for entity_type in self.beliefs:
            posterior_numerator[entity_type] = self.signal_likelihood[signal][entity_type] * self.beliefs[entity_type]
        self.beliefs = normalize(posterior_numerator)

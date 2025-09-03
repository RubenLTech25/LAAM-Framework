import random
from typing import Dict, List, Literal
from .utils import normalize

class RegulatedEntity:
    """Represents Player 1 - The Auditee"""
    
    def __init__(self, true_type: str, materiality: float = 1.0):
        self.true_type = true_type  # 'C', 'R', or 'E'
        self.materiality = materiality
        self.audit_history = []
        
    def generate_signal(self) -> str:
        """Entity emits signals based on its true type"""
        signal_weights = {
            "C": {"clean": 0.9, "missing_doc": 0.1},
            "R": {"clean": 0.4, "vague": 0.4, "unsafe_condition": 0.2},
            "E": {"vague": 0.6, "missing_doc": 0.4}
        }
        signals, weights = zip(*signal_weights[self.true_type].items())
        return random.choices(signals, weights=weights, k=1)[0]
    
    def submit_compliance_fix(self, sector: str) -> Dict[str, bool]:
        """Entity can submit sector-specific evidence to reduce scrutiny"""
        proofs = {
            "tax": ["system_upgrade", "accountant_certified"],
            "healthcare": ["billing_audit", "staff_trained"],
            "labor": ["safety_training", "equipment_upgrade"]
        }
        return {k: True for k in proofs.get(sector, [])}

class Auditor:
    """Represents Player 2 - The Regulator"""
    
    def __init__(self, sector: str, trait: Literal["Grumpy", "Neutral", "Naive"] = "Neutral"):
        self.sector = sector
        self.trait = trait
        self.anchors = []
        self.fairness_params = {
            "tax": {"λ": 0.3, "grim_trigger": 5.0},
            "healthcare": {"λ": 0.5, "grim_trigger": 4.0},
            "labor": {"λ": 0.2, "grim_trigger": 6.0}
        }[sector]
        
        # Trait bias adjustment
        self.bias = {"Grumpy": 0.9, "Neutral": 0.5, "Naive": 0.1}[trait]
        self.fairness_params["λ"] *= self.bias
        
        # Initialize Bayesian beliefs
        self.bayesian_auditor = BayesianAuditor(sector)
    
    def add_anchor(self, violation: str, weight: float):
        """Adds an audit anchor with given weight"""
        self.anchors.append(weight)
    
    def assess_risk(self) -> str:
        """Assesses risk and returns enforcement strategy"""
        total_anchor_weight = sum(self.anchors)
        grim_trigger = self.fairness_params["grim_trigger"]
        
        if total_anchor_weight > grim_trigger:
            return "FULL_SCOPE"
        elif total_anchor_weight > grim_trigger * 0.5:
            return "TARGETED_REVIEW"
        else:
            return "LIMITED_REVIEW"

class BayesianAuditor:
    """Bayesian belief updating system"""
    
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
        """Updates beliefs using Bayes' Theorem"""
        posterior_numerator = {}
        for entity_type in self.beliefs:
            likelihood = self.signal_likelihood.get(signal, {}).get(entity_type, 0.1)
            posterior_numerator[entity_type] = likelihood * self.beliefs[entity_type]
        
        self.beliefs = normalize(posterior_numerator)

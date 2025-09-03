"""
LAAM (Lopez Audit Anchor Model) - A game-theoretic framework for fair enforcement systems.
"""

from .core import (
    calculate_anchor_decay,
    normalize,
    BayesianAuditor,
    RegulatedEntity,
    Auditor
)
from .fairness import (
    enforce_fairness,
    has_compliance_upgrades,
    apply_forgiveness,
    adjust_anchor_weight
)
from .logger import log_decision

__version__ = "0.1.0"
__author__ = "Ruben Lopez"
__email__ = "lopezruben189@yahoo.com"

__all__ = [
    'calculate_anchor_decay',
    'normalize',
    'BayesianAuditor',
    'RegulatedEntity',
    'Auditor',
    'enforce_fairness',
    'has_compliance_upgrades',
    'apply_forgiveness',
    'adjust_anchor_weight',
    'log_decision'
]

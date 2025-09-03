from typing import List, Dict, Any

def enforce_fairness(audit_scope: str, anchors: list, entity: dict) -> str:
    """
    Applies fairness thresholds to constrain enforcement decisions.
    Embodies Axiom 6: Algorithmic Counterweights.

    Args:
        audit_scope: Initial intended audit scope ('full', 'targeted', 'limited')
        anchors: List of active anchor weights
        entity: Auditee attributes and history

    Returns:
        Adjusted audit scope based on fairness rules
    """
    GRIM_THRESHOLD = 2.5  # Threshold for persistent evasion

    if sum(anchors) > GRIM_THRESHOLD:
        final_scope = "Full audit + penalty review"
        reason = "Anchor sum exceeded grim threshold"
    elif has_compliance_upgrades(entity):
        final_scope = "Limited review"  # Forgiveness trigger
        reason = "Compliance upgrades verified"
    else:
        final_scope = audit_scope
        reason = "Default scope retained"

    # Log the decision for transparency
    log_decision(
        original_scope=audit_scope,
        final_scope=final_scope,
        reason=reason
    )
    return final_scope

def has_compliance_upgrades(entity: Dict[str, Any]) -> bool:
    """
    Checks if entity has documented corrective actions.
    
    Args:
        entity: Auditee's data dictionary
        
    Returns:
        True if compliance upgrades are verified
    """
    return entity.get("compliance_upgrades", False)

def apply_forgiveness(anchors: List[float], clean_cycles: int, threshold: int = 3) -> List[float]:
    """
    Down-weights anchors after a threshold of consecutive clean cycles.
    
    Args:
        anchors: List of current anchor weights
        clean_cycles: Number of consecutive cycles with no new anchors
        threshold: Forgiveness threshold (n)
        
    Returns:
        Decayed anchors if threshold met, otherwise original
    """
    if clean_cycles >= threshold:
        return [a * 0.5 for a in anchors]  # Apply 50% reduction
    return anchors

def adjust_anchor_weight(base_weight: float, recurrence_count: int) -> float:
    """
    Applies recurrence-based penalty to increase weight of chronic issues.
    
    Args:
        base_weight: Base weight for violation type
        recurrence_count: How many times issue has occurred
        
    Returns:
        Adjusted anchor weight
    """
    recurrence_penalty = [1.0, 1.5, 2.0]  # Multipliers for 1st, 2nd, 3rd+ occurrence
    penalty_index = min(recurrence_count - 1, len(recurrence_penalty) - 1)
    return base_weight * recurrence_penalty[penalty_index]

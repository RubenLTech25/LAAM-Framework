from datetime import datetime
from typing import Optional

def log_decision(original_scope: str, final_scope: str, reason: str, 
                auditor_id: Optional[str] = None, entity_id: Optional[str] = None):
    """
    Logs audit scope adjustments for transparency and accountability.
    
    Args:
        original_scope: Initial audit scope
        final_scope: Final scope after fairness rules
        reason: Justification for the change
        auditor_id: Optional auditor identifier
        entity_id: Optional auditee identifier
    """
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "auditor_id": auditor_id,
        "entity_id": entity_id,
        "original_scope": original_scope,
        "final_scope": final_scope,
        "reason": reason
    }
    
    # In production, this would write to a database or file
    print(f"[AUDIT LOG] {log_entry}")
    
    # For demonstration, we'll also return the log entry
    return log_entry

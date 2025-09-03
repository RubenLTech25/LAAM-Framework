from laam.core import BayesianAuditor, calculate_anchor_decay

def main():
    print("=== LAAM Framework Demo ===\n")
    
    # Demo 1: Bayesian Updating
    print("1. Bayesian Belief Update Example:")
    auditor = BayesianAuditor(sector='tax')
    print(f"   Initial Beliefs: {auditor.beliefs}")
    auditor.update_beliefs('missing_doc')
    print(f"   Beliefs after 'missing_doc' signal: {auditor.beliefs}\n")

    # Demo 2: Anchor Decay
    print("2. Anchor Decay Example:")
    weight = calculate_anchor_decay(initial_weight=1.0, decay_rate=0.3, time_elapsed=2)
    print(f"   A weight of 1.0 decays to {weight:.4f} after 2 cycles.\n")

if __name__ == "__main__":
    main()

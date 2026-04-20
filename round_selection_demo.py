# round_selection_demo.py
# Demonstration of round allocation in ORSS
# Based on Equations (5) and (10) in the paper

def round_allocation(R_min, R_max, H_i, lambda_E, mu_C):
    """
    Compute the number of rounds R_i for a sensor node.
    Parameters:
        R_min: minimum allowed rounds
        R_max: maximum allowed rounds
        H_i: entropy value of the node (normalized [0,1])
        lambda_E: entropy scaling factor
        mu_C: collision resistance modifier
    Returns:
        R_i: allocated rounds for the node
    """
    delta_R = R_max - R_min
    # Equation (10): R_i >= R_min + ΔR * (λ_E / H_i + μ_C)
    R_i = R_min + delta_R * ((lambda_E / H_i) + mu_C)
    # Ensure R_i stays within [R_min, R_max]
    R_i = max(R_min, min(R_i, R_max))
    return R_i

if __name__ == "__main__":
    # Example parameters (from paper assumptions)
    R_min = 12
    R_max = 24
    lambda_E = 0.5   # entropy scaling factor
    mu_C = 0.2       # collision resistance modifier

    # Example entropy values for 5 sensor nodes
    entropy_values = [0.45, 0.50, 0.55, 0.60, 0.70]

    print("Round allocation results:")
    for i, H_i in enumerate(entropy_values, start=1):
        R_i = round_allocation(R_min, R_max, H_i, lambda_E, mu_C)
        print(f"Node {i}: Entropy={H_i:.2f}, Rounds={R_i:.2f}")

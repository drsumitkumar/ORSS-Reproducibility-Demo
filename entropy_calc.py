# entropy_calc.py
# Shannon entropy calculation with normalization
# Based on Equation (1) in the paper

import math
from collections import Counter

def shannon_entropy(data, normalize=True):
    """
    Compute Shannon entropy H(X) for a given dataset.
    data: list of observed sensor readings (categorical or discrete values)
    normalize: if True, normalize entropy to [0,1]
    """
    counts = Counter(data)
    total = len(data)

    probabilities = [count / total for count in counts.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)

    if normalize:
        # Maximum entropy occurs when all states are equally likely
        max_entropy = math.log2(len(counts))
        if max_entropy > 0:
            entropy /= max_entropy
    return entropy

if __name__ == "__main__":
    # Example dataset: simulated soil moisture readings (discretized levels)
    dataset = [30, 32, 31, 30, 33, 32, 31, 30, 30, 32,
               31, 33, 30, 32, 31, 30, 33, 32, 31, 30]

    H = shannon_entropy(dataset, normalize=True)
    print("Dataset:", dataset)
    print(f"Normalized Entropy H(X) = {H:.4f}")

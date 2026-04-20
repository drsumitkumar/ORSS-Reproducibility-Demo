# ORSS Reproducibility Demo

This repository provides a minimal reproducibility package for the Optimized Round-Selected SHAKE256 (ORSS) framework, as described in the paper.

## Contents
- entropy_calc.py: Python script to compute Shannon entropy H(X) with normalization.
- round_selection_demo.py: Python script to demonstrate round allocation using entropy scaling factor (λ_E) and collision resistance modifier (μ_C).
- sample_data.csv: Dataset of 100 sensor nodes with normalized entropy values and allocated rounds.
- README.md: Documentation and reproducibility statement.

## Usage
1. Run `entropy_calc.py` to compute entropy for a dataset.
2. Run `round_selection_demo.py` to see how rounds are allocated based on entropy values.
3. Use `sample_data.csv` as a reference dataset to reproduce the results.

## Reproducibility Statement
We conducted the full experiments with node sizes ranging from 10 to 100 offline due to hardware constraints. To ensure reproducibility, we share simplified Python code and a representative dataset so that the computational steps can be independently verified.

## License
MIT License (permissive open-source).
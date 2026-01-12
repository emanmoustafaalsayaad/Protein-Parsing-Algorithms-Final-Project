# Protein Parsing Algorithm Comparison

This project compares four different algorithmic approaches for the **Protein Parsing** problem on large datasets, with a focus on demonstrating the efficiency gains of a **Trie-based dynamic programming** solution.

---

## Comparison Plan

The goal is to evaluate and compare the following four approaches:

1. **Brute Force**
2. **Top-Down Dynamic Programming (Memoization)**
3. **Bottom-Up Dynamic Programming (Tabulation)**
4. **Trie-based Dynamic Programming**

The comparison covers:
- Correctness validation using predefined test cases
- Empirical performance benchmarking for increasing input sizes
- Alignment between theoretical and practical time complexity

---

## Implemented Changes

### Algorithms

A new script was created:

**`protein_parsing_approaches.py`**

It contains a `ProteinSolver` class with the following methods:

- `max_division_brute_force`  
  Recursive brute-force approach with exponential complexity **O(kⁿ)**.

- `max_division_top_down_dp`  
  Recursive dynamic programming with memoization,  
  time complexity **O(N · k²)**.

- `max_division_bottom_up_dp`  
  Iterative dynamic programming using tabulation,  
  time complexity **O(N · k²)**.

- `max_division_trie_dp`  
  Optimized iterative DP using a Trie (prefix tree),  
  time complexity **O(N · k)**.

---

### Test Runner

- Validates **all four approaches** against 10 predefined test cases.
- Ensures all methods return identical results.

---

### Benchmarker

- Measures execution time for increasing sequence lengths `N` (from 20 to 50,000).
- Includes:
  - **Brute Force** only for very small `N (≤ 25)` to demonstrate exponential growth.
  - **Top-Down DP** skipped for large `N (> 2,500)` to avoid recursion limits.
- Computes **percentage improvement** of Trie-DP over Bottom-Up DP.

---

### Documentation

- The code includes detailed, line-by-line comments explaining:
  - Algorithm logic
  - Optimization choices
  - Time and space complexity

---

### Renaming

- The script was renamed from  
  `protein_comparison.py`  
  to  
  `protein_parsing_approaches.py`

---

## Verification Plan

### Automated Tests

- The script automatically runs all test cases.
- Assertions ensure that all four approaches produce identical outputs.

### Benchmarks

- Benchmarks confirm a consistent **~11× speedup (90%+ time reduction)** of Trie-DP over Bottom-Up DP for large inputs.

---

## Protein Parsing Algorithm Comparison Results

---

## 1. Test Case Validation

| Sequence (S) | Expected | Brute Force | Top-Down | Bottom-Up | Trie-DP | Status |
|-------------|----------|-------------|----------|-----------|---------|--------|
| ACGT | 2 | 2 | 2 | 2 | 2 | PASS |
| ACGCG | 2 | 2 | 2 | 2 | 2 | PASS |
| AAAA | 4 | 4 | 4 | 4 | 4 | PASS |
| ACGT | 0 | 0 | 0 | 0 | 0 | PASS |
| ATGCGAT | 3 | 3 | 3 | 3 | 3 | PASS |
| ACGTAC | 0 | 0 | 0 | 0 | 0 | PASS |
| ACGT | 1 | 1 | 1 | 1 | 1 | PASS |
| ACGT | 2 | 2 | 2 | 2 | 2 | PASS |
| ATGCGT... | 7 | 7 | 7 | 7 | 7 | PASS |

**Result:**  
All four approaches produced identical, correct results for all 10 test cases.

---

## 2. Time Complexity Comparison

Execution time measured in seconds.  
Parameters: `k = 50`, `|P| = 1000`.

| N (Length) | Brute Force | Top-Down | Bottom-Up | Trie-DP | Improvement (BU vs Trie) |
|-----------|-------------|----------|-----------|---------|--------------------------|
| 20 | 0.3604s | 0.0001s | 0.0001s | 0.0001s | 0.4% |
| 50 | Skipped | 0.0005s | 0.0003s | 0.0001s | 72.4% |
| 100 | Skipped | 0.0013s | 0.0009s | 0.0001s | 87.9% |
| 500 | Skipped | 0.0087s | 0.0062s | 0.0006s | 90.0% |
| 1,000 | Skipped | 0.0181s | 0.0130s | 0.0013s | 90.0% |
| 2,000 | Skipped | 0.0371s | 0.0261s | 0.0027s | 89.7% |
| 5,000 | Skipped | Skipped | 0.0666s | 0.0062s | 90.6% |
| 10,000 | Skipped | Skipped | 0.1337s | 0.0117s | 91.3% |
| 20,000 | Skipped | Skipped | 0.2659s | 0.0221s | 91.7% |
| 50,000 | Skipped | Skipped | 0.6603s | 0.0571s | 91.4% |

---

### Notes on "Skipped"

- **Brute Force:**  
  Skipped for `N > 25` due to exponential complexity **O(kⁿ)**.  
  At `N = 20`, execution already takes ~0.36 seconds.  
  Increasing the input by 30 characters multiplies the workload by approximately `2³⁰` (~1 billion), making execution infeasible.

- **Top-Down DP:**  
  Skipped for `N > 2,500` due to Python recursion depth limits and high function-call overhead.

---

## Conclusion

- **Brute Force** is unusable beyond very small inputs.
- All DP-based approaches are correct, but differ significantly in scalability.
- **Trie-based DP** consistently achieves a **~11× speedup** (over **90% runtime reduction**) compared to Bottom-Up DP for large inputs.

These results confirm that integrating a Trie with dynamic programming provides both theoretical and practical performance advantages for the Protein Parsing problem.

---

## How to Run

### Requirements
- Python 3.8 or higher
- No external libraries required

### Run the Script

```bash
python protein_parsing_approaches.py

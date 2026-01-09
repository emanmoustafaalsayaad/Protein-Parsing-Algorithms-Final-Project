# Protein Parsing – Algorithm Comparison

This repository compares three dynamic programming approaches for solving the **Protein Parsing** problem: identifying the maximum number of non-overlapping protein markers within a DNA sequence.

The project focuses on **correctness verification** and **time complexity comparison** as the sequence length increases.

---

## Algorithms Compared

The following approaches are implemented:

1. **Top-Down DP (Memoization)**  
   Recursive dynamic programming using memoization based on the provided logic.

2. **Bottom-Up DP (Tabulation)**  
   Iterative dynamic programming approach without recursion.

3. **Trie-based DP**  
   Optimized bottom-up DP using a Trie (prefix tree) to eliminate redundant string matching.

---

## Repository Structure

### `protein_comparison.py`

A single Python script containing all implementations and experiments.

#### Core Classes

- **`ProteinSolver`**
  - `max_division_top_down_dp`  
    Recursive DP with memoization.
  - `max_division_bottom_up_dp`  
    Iterative DP using tabulation.
  - `max_division_trie_dp`  
    Trie-optimized iterative DP.

- **`Trie`** and **`TrieNode`**
  - Used by the Trie-based DP method.
  - Optimized using `__slots__` to reduce memory overhead.

---

## Test Runner

The script includes an automated test runner that:

- Iterates through the provided `test_cases`
- Executes all three algorithms on each test case
- Asserts that all results match the expected output
- Prints a formatted table summarizing test results

This ensures correctness before benchmarking.

---

## Benchmarker

The benchmarking section evaluates performance as input size grows.

### Benchmark Details

- Sequence lengths tested:  
  `N = 200, 500, 1k, 5k, 10k, 50k`
- Randomly generated:
  - DNA sequence `S`
  - Protein marker set `P`
- Execution time measured for:
  - Bottom-Up DP
  - Trie-based DP

> **Note:**  
> Top-Down DP may be skipped for very large `N` due to recursion depth limits, or included using `sys.setrecursionlimit`.

### Output

- Prints a comparison table showing execution times for each algorithm at different values of `N`.

---

## Verification Plan

- All provided test cases are executed automatically when running the script
- Results are validated using assertions
- Performance results are inspected via printed comparison tables

---

## How to Run

```bash
python protein_comparison.py

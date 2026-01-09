# Protein Parsing – Algorithm Comparison

This repository compares three dynamic programming approaches for solving the **Protein Parsing** problem: identifying the maximum number of non-overlapping protein markers within a DNA sequence.

The project focuses on **correctness verification** and **time complexity comparison** as the sequence length increases.

---

## Algorithms Compared

The following approaches are implemented:

1. **Top-Down DP (Memoization)**  
   Recursive dynamic programming using memoization based on the provided logic.

2. **Bottom-Up DP (Tabulation)**  
   An iterative dynamic programming approach without recursion.

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


## Protein Parsing Algorithm Comparison Results

---

## 1. Test Case Validation

All three algorithms were validated using a fixed set of test cases.

| Sequence (S) | Expected | Top-Down | Bottom-Up | Trie-DP | Status |
|-------------|----------|----------|-----------|---------|--------|
| ACGT | 2 | 2 | 2 | 2 | PASS |
| ACGCG | 2 | 2 | 2 | 2 | PASS |
| AAAA | 4 | 4 | 4 | 4 | PASS |
| ACGT | 0 | 0 | 0 | 0 | PASS |
| ATGCGAT | 3 | 3 | 3 | 3 | PASS |
| ACGTAC | 0 | 0 | 0 | 0 | PASS |
| ACGT | 1 | 1 | 1 | 1 | PASS |
| (Empty) | 0 | 0 | 0 | 0 | PASS |
| ACGT | 2 | 2 | 2 | 2 | PASS |
| ATGCGT... | 7 | 7 | 7 | 7 | PASS |

**Result:**  
All three approaches produced identical and correct results for all 10 test cases.

---

## 2. Time Complexity Comparison

Execution time measured in seconds.  
Parameters: `k = 50`, `|P| = 1000`.

| N (Length) | Top-Down | Bottom-Up | Trie-DP | Improvement |
|-----------|----------|-----------|---------|-------------|
| 100 | 0.0015s | 0.0010s | 0.0001s | 84.7% |
| 500 | 0.0087s | 0.0059s | 0.0006s | 89.0% |
| 1,000 | 0.0177s | 0.0120s | 0.0010s | 91.3% |
| 2,000 | 0.0379s | 0.0247s | 0.0023s | 90.5% |
| 5,000 | Skipped | 0.0638s | 0.0061s | 90.5% |
| 10,000 | Skipped | 0.1267s | 0.0112s | 91.1% |
| 20,000 | Skipped | 0.2710s | 0.0246s | 90.9% |
| 50,000 | Skipped | 0.6903s | 0.0536s | 92.2% |

> **Note:**  
> Note on "Skipped": The Top-Down approach relies on recursion. For large $N$ (string length), the recursion depth exceeds Python's default limits and incurs significant function call overhead. We skip it for $N > 2,500$ to prevent RecursionError crashes and excessive runtimes.
---

## Conclusion

- All three algorithms are **functionally equivalent** and produce correct results.
- The **Trie-optimized DP** consistently achieves **over 90% runtime reduction** compared to the naive Bottom-Up DP for large input sizes.
- This behavior matches theoretical expectations:  
  naive DP performs **O(N · |P| · k)** work, while Trie-based DP reduces matching to **O(N · k)** by eliminating redundant prefix checks.

These results confirm that integrating a Trie with dynamic programming provides substantial and scalable performance improvements for the Protein Parsing problem.

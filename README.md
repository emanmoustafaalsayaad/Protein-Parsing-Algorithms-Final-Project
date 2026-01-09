## Protein Parsing Algorithm Comparison

This section reports the correctness validation and performance benchmarking results for the three implemented approaches:
Top-Down DP, Bottom-Up DP, and Trie-based DP.

---

## 1. Correctness Validation

All three algorithms were evaluated on a fixed set of test cases to verify functional correctness.

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

**Summary:**  
All three approaches produced identical and correct results for all test cases.

---

## 2. Performance Benchmarking

Execution time was measured in seconds under the following configuration:

- Maximum marker length: `k = 50`
- Number of protein markers: `|P| = 1000`

| N (Sequence Length) | Top-Down DP | Bottom-Up DP | Trie-DP | Time Reduction |
|--------------------|------------|--------------|---------|----------------|
| 100 | 0.0015s | 0.0010s | 0.0001s | 84.7% |
| 500 | 0.0087s | 0.0059s | 0.0006s | 89.0% |
| 1,000 | 0.0177s | 0.0120s | 0.0010s | 91.3% |
| 2,000 | 0.0379s | 0.0247s | 0.0023s | 90.5% |
| 5,000 | — | 0.0638s | 0.0061s | 90.5% |
| 10,000 | — | 0.1267s | 0.0112s | 91.1% |
| 20,000 | — | 0.2710s | 0.0246s | 90.9% |
| 50,000 | — | 0.6903s | 0.0536s | 92.2% |

**Note:**  
The Top-Down DP approach relies on recursion and was intentionally omitted for `N > 2,500` due to Python recursion depth limits and excessive function-call overhead.

---

## Conclusion

- All three algorithms are **functionally equivalent** and consistently produce correct results.
- The **Trie-based DP** provides a **stable performance improvement of over 90%** compared to the standard Bottom-Up DP for large input sizes.
- These results align with theoretical complexity analysis:
  - Bottom-Up DP: **O(N · |P| · k)**
  - Trie-based DP: **O(N · k)**

The empirical benchmarks confirm that integrating a Trie with dynamic programming is a practical and scalable optimization for the Protein Parsing problem.

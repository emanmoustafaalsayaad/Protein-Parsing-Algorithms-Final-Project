import sys
import time
import random

# Increase recursion limit to handle deep recursion in Top-Down DP for larger inputs.
# The default is usually 1000, which is too small for N > 1000.
sys.setrecursionlimit(20000)

# -----------------------------------------------------------------------------
# Data Structures
# -----------------------------------------------------------------------------

class TrieNode:
    # Use __slots__ to optimize memory usage and attribute access speed.
    # This acts like a struct in C, preventing the creation of a dynamic __dict__.
    __slots__ = ['children', 'is_end']
    
    def __init__(self):
        # Dictionary mapping a character (A, C, G, T) to the next TrieNode.
        self.children = {}
        # Boolean flag indicating if this node marks the end of a valid protein marker.
        self.is_end = False

class Trie:
    def __init__(self):
        # Initialize the Trie with an empty root node.
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word (protein marker) into the Trie.
        """
        # Start at the root of the Trie.
        node = self.root
        # Iterate over each character in the marker string.
        for ch in word:
            # If the character doesn't exist in the current node's children, create a new node.
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # Move down to the child node corresponding to the character.
            node = node.children[ch]
        # After processing all characters, mark the final node as the end of a marker.
        node.is_end = True

# -----------------------------------------------------------------------------
# Solver Class
# -----------------------------------------------------------------------------

class ProteinSolver:
    def __init__(self, strand, protein_markers, k):
        """
        Initialize the solver with the DNA strand, set of markers, and max marker length k.
        """
        self.strand = strand                  # The DNA sequence string (S)
        self.protein_markers = protein_markers # The set of valid protein markers (P)
        self.k = k                            # The maximum length of any marker in P
        self.n = len(strand)                  # Length of the DNA sequence
        
        # Memoization table for Top-Down DP approach (initialized to -1)
        self.memo = None 
        # Score table for Bottom-Up DP approach
        self.scores = None 
        
        # Pre-build the Trie structure from the protein markers for the Trie-DP approach.
        # This is done once upon initialization.
        self.trie = Trie()
        for p in protein_markers:
            self.trie.insert(p)

    # =========================================================================
    # 1. TOP DOWN DP APPROACH (Recursion + Memoization)
    # =========================================================================
    def max_division_top_down_dp(self):
        # Initialize memoization table with -1 (indicating uncomputed states).
        # Size is N + 1 to handle indices from 0 to N.
        self.memo = [-1] * (self.n + 1)
        # Start the recursive solution from the beginning of the strand (index 0).
        return self.solve_with_memo(0)

    def solve_with_memo(self, idx):
        # Base Case: If we have reached the end of the strand, return 0 (no more markers can be found).
        if idx == self.n:
            return 0
        # Boundary Check: If index exceeds length (shouldn't happen with correct logic), return 0.
        if idx > self.n:
            return 0
        
        # Check Memoization: If we have already computed the result for this index, return it.
        if self.memo[idx] != -1:
            return self.memo[idx]
        
        # Initialize max score for this position to 0.
        score = 0
        
        # Iterate through all possible split lengths from 1 to k.
        # We try to slice a substring starting at 'idx' of length 'split_len'.
        for split_len in range(1, self.k + 1):
            # If the split goes beyond the end of the strand, stop trying longer splits.
            if idx + split_len > self.n:
                break
            
            # Extract the actual substring from the strand.
            # COST: Slicing takes O(L) time.
            substring = self.strand[idx : idx + split_len]
            
            # Check if this substring constitutes a valid protein marker in our set P.
            # COST: Hashing/Set lookup takes O(L) time.
            if substring in self.protein_markers:
                # If valid, we get 1 point + the best score from the remainder of the strand.
                val = 1 
            else:
                # If invalid (gap/waste), we get 0 points + best score from remainder.
                val = 0
            
            # Recurse for the rest of the strand starting after this substring.
            # Update 'score' if this path yields a better result.
            score = max(score, val + self.solve_with_memo(idx + split_len))

        # Store the computed result in the memo table so we don't re-calculate it.
        self.memo[idx] = score
        return score

    # =========================================================================
    # 2. BOTTOM UP DP APPROACH (Iterative Tabulation)
    # =========================================================================
    def max_division_bottom_up_dp(self):
        # Initialize the DP table with 0s. 
        # self.scores[i] will store the max markers found in the suffix S[i...N].
        self.scores = [0] * (self.n + 1)

        # Iterate backwards from the last character to the first (N-1 down to 0).
        for idx in range(self.n - 1, -1, -1):
            cur_score = 0
            
            # Try all possible lengths from 1 to k at this position 'idx'.
            for cur_split_len in range(1, self.k + 1):
                # Boundary check: don't go past the end of the string.
                if idx + cur_split_len > self.n:
                    break
                
                # Extract substring. COST: O(L)
                substring = self.strand[idx : idx + cur_split_len]
                
                # Check if it's a marker. COST: O(L)
                if substring in self.protein_markers:
                    # Logic: 1 (this marker) + best score of the suffix starting after this marker.
                    cur_score = max(cur_score, 1 + self.scores[idx + cur_split_len])
                else:
                    # Logic: 0 (gap) + best score of the suffix.
                    # This effectively handles the "skip character" case implicitly over many steps,
                    # or explicitly if we consider length 1 as a skip.
                    cur_score = max(cur_score, self.scores[idx + cur_split_len])
            
            # Store the best score found for this starting position.
            self.scores[idx] = cur_score
            
        # The result for the entire string is stored at index 0.
        return self.scores[0]

    # =========================================================================
    # 3. TRIE DP APPROACH (Optimized Iterative)
    # =========================================================================
    def max_division_trie_dp(self):
        # Initialize DP array. dp[i] = max markers found in prefix S[0...i].
        # Note: This uses "Forward DP" logic (building up from index 0 to N),
        # unlike the "Suffix DP" of the Bottom-Up approach above. Both are valid.
        n = self.n
        dp = [0] * (n + 1)

        for i in range(n):
            # Option 1: Skip the current character S[i].
            # The score at i+1 can at least be the score at i (carrying forward the result).
            if dp[i] > dp[i+1]: 
                 dp[i+1] = dp[i]
            else:
                 dp[i+1] = max(dp[i+1], dp[i]) # Standard max logic
            
            # Option 2: Try to match protein markers starting EXACTLY at position i.
            # Instead of slicing strings, we walk down the Trie.
            node = self.trie.root
            
            # We look ahead up to k characters, or until the end of the string.
            for j in range(i, min(i + self.k, n)):
                ch = self.strand[j]
                
                # If the character does NOT exist in the current Trie node's children,
                # then NO marker starts with the prefix S[i...j].
                # We can STOP immediately. This avoids checking longer substrings!
                if ch not in node.children:
                    break
                
                # Move to the next node in the Trie.
                node = node.children[ch]
                
                # If this node represents the end of a valid marker:
                if node.is_end:
                    # We found a marker from S[i...j].
                    # Update dp[j+1] (end of this marker) with:
                    # dp[i] (score before this marker) + 1 (this new marker)
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)
        
        # The final answer is at dp[n].
        return dp[n]


# -----------------------------------------------------------------------------
# 1. Validation Logic
# -----------------------------------------------------------------------------

def run_tests():
    # Define a suite of test cases to verify correctness of all 3 algorithms.
    test_cases = [ 
        {"S": "ACGT", "P": {"A", "CG", "GT"}, "expected_output": 2},
        {"S": "ACGCG", "P": {"AC", "CG", "GCG"}, "expected_output": 2},
        {"S": "AAAA", "P": {"A", "AA"}, "expected_output": 4},
        {"S": "ACGT", "P": {"GG", "TT"}, "expected_output": 0},
        {"S": "ATGCGAT", "P": {"ATG", "GCG", "AT", "T"}, "expected_output": 3},
        {"S": "ACGTAC", "P": set(), "expected_output": 0},
        {"S": "ACGT", "P": {"ACGT"}, "expected_output": 1},
        {"S": "", "P": {"ACGT"}, "expected_output": 0},
        {"S": "ACGT", "P": {"AC", "CG", "GT"}, "expected_output": 2},
        {"S": "ATGCGTACGTTAGCTAGGCTACGTAGCTAG", "P": {"ATG", "GTT", "AGC", "TAG", "ACG"}, "expected_output": 7}
    ]

    print("\n" + "="*80)
    print("TEST CASE VALIDATION")
    print("="*80)
    print(f"{'S':<20} | {'Expected':<8} | {'Top-Down':<8} | {'Bottom-Up':<9} | {'Trie-DP':<8} | {'Status'}")
    print("-" * 80)

    for tc in test_cases:
        S = tc["S"]
        P = tc["P"]
        # Calculate max K based on the provided markers. Default to 1 if empty.
        k = max((len(p) for p in P), default=0) if P else 0 
        if k == 0: k = 1

        # Instantiate the solver
        solver = ProteinSolver(S, P, k)
        
        # Run all three methods
        res_td = solver.max_division_top_down_dp()
        res_bu = solver.max_division_bottom_up_dp()
        res_trie = solver.max_division_trie_dp()
        expected = tc["expected_output"]

        # Check if all match the expected output
        passed = (res_td == expected) and (res_bu == expected) and (res_trie == expected)
        status = "PASS" if passed else "FAIL"
        
        # Truncate S for display if too long
        s_disp = S if len(S) <= 18 else S[:15] + "..."
        
        # Print row in the results table
        print(f"{s_disp:<20} | {expected:<8} | {res_td:<8} | {res_bu:<9} | {res_trie:<8} | {status}")

# -----------------------------------------------------------------------------
# 2. Benchmark Logic
# -----------------------------------------------------------------------------

def generate_dna(length):
    # Generates a random DNA string of length 'length'
    return ''.join(random.choice("ACGT") for _ in range(length))

def generate_markers(num_markers, max_k):
    # Generates a set of 'num_markers' random unique DNA strings of max length 'max_k'
    markers = set()
    while len(markers) < num_markers:
        length = random.randint(1, max_k)
        marker = ''.join(random.choice("ACGT") for _ in range(length))
        markers.add(marker)
    return markers

def run_benchmarks():
    print("\n" + "="*95)
    print("TIME COMPLEXITY COMPARISON (Time in seconds)")
    print("="*95)
    # Table Header
    header = f"{'N (Length)':<12} | {'Top-Down':<12} | {'Bottom-Up':<12} | {'Trie-DP':<12} | {'Improvement':<12}"
    print(header)
    print("-" * len(header))

    # Define range of N (sequence lengths) to test.
    # We go up to 50,000 to show the performance gap clearly.
    N_values = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    
    for n in N_values:
        # Fixed parameters for the benchmark
        k = 50                 # Max marker length
        num_markers = 1000     # Size of marker set
        
        # Generate random test data
        S = generate_dna(n)
        P = generate_markers(num_markers, k)
        
        solver = ProteinSolver(S, P, k)

        # 1. Top Down Benchmark
        # We skip Top-Down for N > 2500 because deep recursion is very slow in Python
        # and risks hitting recursion limits despite sys.setrecursionlimit.
        if n <= 2500:
            start = time.time()
            solver.max_division_top_down_dp()
            t_td_val = time.time() - start
            s_td = f"{t_td_val:.4f}s"
        else:
            s_td = "Skipped"

        # 2. Bottom Up Benchmark
        start = time.time()
        solver.max_division_bottom_up_dp()
        t_bu_val = time.time() - start
        s_bu = f"{t_bu_val:.4f}s"

        # 3. Trie DP Benchmark
        start = time.time()
        solver.max_division_trie_dp()
        t_trie_val = time.time() - start
        s_trie = f"{t_trie_val:.4f}s"

        # Calculate Improvement % (Reduction in time from Bottom-Up to Trie-DP)
        # Formula: (Time_BU - Time_Trie) / Time_BU * 100
        if t_bu_val > 0:
            improvement = (t_bu_val - t_trie_val) / t_bu_val * 100
            s_imp = f"{improvement:.1f}%"
        else:
            s_imp = "N/A"

        # Print benchmark row
        print(f"{n:<12} | {s_td:<12} | {s_bu:<12} | {s_trie:<12} | {s_imp:<12}")

if __name__ == "__main__":
    # First, run validation to ensure correctness
    run_tests()
    # Then, run strict performance benchmarks
    run_benchmarks()

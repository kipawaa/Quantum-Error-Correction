# Abstract
Quantum computing in the modern sense originates around 1980, with a number of important theoretical results published between 1985 and 2000.
These results, such as Shor's algorithm for integer factorization, and Grover's search algorithm provide significant speedups from their classical counterparts.
Since then, the difficulty has been to construct a quantum computer sufficiently large to use the algorithms in practice.
One key factor to enabling these algorithms is to adequately correct errors that accumulate during quantum computation.

This report presents stabilizer codes - quantum error correcting codes based in subspace correction.
We discuss bit-flip and phase flip errors, justify that correcting these errors is sufficient for correcting arbitrary errors, and provide codes capable of correcting each of these.
Finally, we provide Qiskit implementations of these codes that verify their correctness and feasibility.

# Variational Approach to Quantum State Discrimination

## Abstract

Quantum state discrimination is an important task for quantum information processing. It is known that in quantum mechanics, one could only perfectly discriminate orthogonal states. When the states are non-orthogonal, several strategies can be adopted to discriminate them. One such strategy is the minimum error strategy where we minimize the probability of error resulting from imperfect discriminations. However, exact solution is only known for two states discrimination case.
In this project, we are expecting a search based algorithm to help find the optimal quantum circuit for state discrimination.

## Optimization Algorithm  
  - Local search based: simple hill climbing
    We use step by step approach of approximation to reach the top of the hill in success rate.

## Result  
### Discrimination results  
- **The quantum states in forms of (a,b) in (a * |0> +  b * |1>)**
  qp_1:  (1, 0)  
  qp_2:  (0.7071067811865476, 0.7071067811865476)  
  qp_3:  (0, 1)  
  qp_4:  (0.7071067811865476, 0.7071067811865476j)  
  qp_5:  (0.5, 0.8660254037844386)  
  qp_6:  (0.8660254037844386, 0.5)  
  qp_7:  (0.5773502691896257, 0.816496580927726)  
  qp_8:  (0.816496580927726, 0.5773502691896257)  

- **Discrimination success rates**  
  indexing: (1)q-(2) qp_(3) qp_(4) --> (1): number of qubits, (2): experiment index, (3),(4): state index  
  
  2q-1 qp_1 qp_2 (Theoretical maximum is about 85%)  
  average is:  0.8289742857142854  
  stddev is:  0.01667364264891369  
    
  2q-2 qp_1 qp_3  
  average is:  0.9775971428571428  
  stddev is:  0.018997885274365647  
  
  2q-3 qp_7 qp_8  
  average is:  0.6590907142857144  
  stddev is:  0.008105584211404091  
  
  2q-4 qp_5 qp_6  
  average is:  0.7422142857142857  
  stddev is:  0.009714390755734603  
  
  3q-1 qp_1 qp_2 qp_3 (Theoretical maximum is about 67%)  
  average is:  0.6167666666666666  
  stddev is:  0.03715883325521523  
  
  3q-2 qp_1 qp_2 qp_4  
  average is:  0.5366933333333334  
  stddev is:  0.0192063461734223  
  
  3q-3 qp_1 qp_5 qp_6  
  average is:  0.5426266666666667  
  stddev is:  0.046376988546763864  

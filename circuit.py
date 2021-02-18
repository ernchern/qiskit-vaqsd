import qiskit

import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)

def build_circuit(params, a_1, b_1, a_2, b_2, shots = 1000, verbose = False):
    '''
    Inputs:
        measure_index: index of a qubit to measure
        params: numpy array of [theta, phi, lam]
        shots: number of executions of the circuit
		a_1:
		b_1:
		a_2:
		b_2:
    Output:
        out_counts: numpy array of probabilities of outcomes in the order: '00', '01', '10', '11'
    '''
    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')
    # Create a Quantum Circuit acting on the q register
    circuit1 = QuantumCircuit(1, 1)

    circuit1.u3(2*np.arccos(a_1),np.arccos(np.real(b_1)/abs(b_1)),0,0)
	
    circuit1.u3(params[0],params[1],params[2],0)
    
    circuit1.measure([0], [0])
    
    # Execute the circuit on the qasm simulator
    job1 = execute(circuit1, simulator, shots = shots)

    # Grab results from the job
    result1 = job1.result()

    # Returns counts
    counts1 = result1.get_counts(circuit1)
    
    
    # Create a Quantum Circuit acting on the q register
    circuit2 = QuantumCircuit(1, 1)

    #circuit2.h(0)
	
    circuit2.u3(2*np.arccos(a_2),0,0,0)
    
    circuit2.u3(params[0],params[1],params[2],0)
    
    circuit2.measure([0], [0])
    
    # Execute the circuit on the qasm simulator
    job2 = execute(circuit2, simulator, shots = shots)

    # Grab results from the job
    result2 = job2.result()

    # Returns counts
    counts2 = result2.get_counts(circuit2)
    
    if verbose:
        print(circuit1)
        print(circuit2)

    for i in ['0', '1']:
        if not i in counts1:
            counts1[i] = 0
            
    for i in ['0', '1']:
        if not i in counts2:
            counts2[i] = 0
            
            
    out_prob = (counts1['0']+counts2['1'])/(2*shots)

    return out_prob

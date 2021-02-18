import qiskit

import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)


def build_circuit(params,shots=1000):
    '''
    Inputs:
    
        params: numpy array of [theta, phi, lam]
        shots: number of executions of the circuit
    Output:
        out_counts: numpy array of probabilities of outcomes in the order: '00', '01', '10', '11'
    '''
    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')

    # Create a Quantum Circuit acting on the q register
    circuit = QuantumCircuit(2, 2)

    # Add a H gate on qubit 1
    circuit.h(1)

    # # Add a U3 gate with random parameters
    circuit.u3(params[0],params[1],params[2],0)
    circuit.u3(params[0],params[1],params[2],1)

    # Map the quantum measurement to the classical bits
    circuit.measure([0,1], [0,1])

    # Execute the circuit on the qasm simulator
    job = execute(circuit, simulator, shots=shots)

    # Grab results from the job
    result = job.result()

    # Returns counts
    counts = result.get_counts(circuit)
    
    out_counts = np.array([counts['00'],counts['01'],counts['10'],counts['11']])/shots

    return out_counts


import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)

def setQubit(circuit, a, b):
    if b!=0 :
        circuit.u3(2*np.arccos(a),np.arccos(np.real(b)/abs(b)),0,0)
    else:
        circuit.u3(2*np.arccos(a),0,0,0)
        
def addLayer(circuit, params, index):
    circuit.u3(params[0],params[1],params[2],index)
    
def build_circuit(params, a_1, b_1, a_2, b_2, a_3, b_3, bias, shots = 1000, verbose = False):
    '''
    Inputs:
        params: 4 by 3 array of nodes
        shots: number of executions of the circuit
        a_n and b_n : nth qubit's parameters 
    Output:
        p_success: Success rate
		p_inconclusive: Probability of getting the leftover output
    '''
    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')
    # Create a Quantum Circuit acting on the q register
    circuit1 = QuantumCircuit(2, 2)
    circuit2 = QuantumCircuit(2, 2)
    circuit3 = QuantumCircuit(2, 2)
    
    #Set the quits
    setQubit(circuit1, a_1, b_1)
    setQubit(circuit2, a_2, b_2)
    setQubit(circuit3, a_3, b_3)
    
    params = params.reshape((2,3))
	
    #"Neural layers"
    addLayer(circuit1, params[0][:],0)
    addLayer(circuit1, params[1][:],1)
    
    addLayer(circuit2, params[0][:],0)
    addLayer(circuit2, params[1][:],1)
    
    addLayer(circuit3, params[0][:],0)
    addLayer(circuit3, params[1][:],1)
    
#     #CNOT gate
    circuit1.cx(0,1)
    circuit2.cx(0,1)
    circuit3.cx(0,1)
    
    # #"Neural layers"
    # addLayer(circuit1, params[2][:],0)
    # addLayer(circuit1, params[3][:],1)
    
    # addLayer(circuit2, params[2][:],0)
    # addLayer(circuit2, params[3][:],1)
    
    # addLayer(circuit3, params[2][:],0)
    # addLayer(circuit3, params[3][:],1)
    
    # #     #CNOT gate
    # circuit1.cx(1,0)
    # circuit2.cx(1,0)
    # circuit3.cx(1,0)

#   Measure    
    circuit1.measure([0,1], [0,1])
    circuit2.measure([0,1], [0,1])
    circuit3.measure([0,1], [0,1])
    
    
    # Execute the circuit on the qasm simulator
    job1 = execute(circuit1, simulator, shots = shots)
    job2 = execute(circuit2, simulator, shots = shots)
    job3 = execute(circuit3, simulator, shots = shots)

    # Grab results from the job
    result1 = job1.result()
    result2 = job2.result()
    result3 = job3.result()

    # Returns counts
    counts1 = result1.get_counts(circuit1)
    counts2 = result2.get_counts(circuit2)
    counts3 = result3.get_counts(circuit3)
    
    if verbose:
        print(circuit1)
        print(counts1)
        print(circuit2)
        print(counts2)
        print(circuit3)
        print(counts3)

    for i in ['00', '01','10','11']:
        if not i in counts1:
            counts1[i] = 0
        if not i in counts2:
            counts2[i] = 0
        if not i in counts3:
            counts3[i] = 0
            
            
    p_success = (counts1['00']+counts2['01']+counts3['10'])/(3*shots)
    p_inconclusive = (counts1['11']+counts2['11']+counts3['11'])/(3*shots)
            
    #obj_value = p_success / (p_inconclusive + bias*shots)
    #obj_value = 1.5 * p_success - p_inconclusive
	

    return (p_success, p_inconclusive)

import circuit
import cirquit_3q
import numpy as np
import cmath

# counts_distribution =  circuit.evaluate(parameter, shot_size)

#evaluate = lambda params, shot_size: (circuit.build_circuit(params,0,shot_size/2)[1]+circuit.build_circuit(params,1,shot_size/2)[0])/2

# evaluate = lambda param, shot_size :circuit.build_circuit(param,np.sqrt(1/3),np.sqrt(2/3),np.sqrt(2/3),np.sqrt(1/3),shot_size) 


def optimize_circuit(quantum_pairs, iteration_limit, initial_step_size, shot_size, minimum_step, dim = 3, verbose = True):
	
	
	parameters = np.random.rand(dim) * 2 * np.pi

	if dim == 3:
		evaluate = lambda param, shot_size :circuit.build_circuit(param, quantum_pairs[0][0], quantum_pairs[0][1], quantum_pairs[1][0], quantum_pairs[1][1], shot_size)
	elif dim == 6:
		evaluate = lambda param, shot_size :cirquit_3q.build_circuit(param, quantum_pairs[0][0], quantum_pairs[0][1], quantum_pairs[1][0], quantum_pairs[1][1], quantum_pairs[2][0], quantum_pairs[2][1], shot_size)
	
	iteration = 0
	# initial input
	
	# evaluate with initial input
	reference_result = evaluate(parameters, shot_size)
	step_size = initial_step_size
	
	search = True
	while(search):
		# Take steps
		variations = create_variations(parameters, step_size, dim)
		
		# Evaluate all the variations
		result = []
		for step in variations:
			result.append(evaluate(step, shot_size))
		
		# Change current parameters to the best among 6
		result = np.array(result)
		iteration += 1
		
		# If it's local optima, try smaller step
		if result.max() > reference_result:
			step_size = (reference_result - result.max())/step_size
			reference_result = result.max()
			parameters = variations[result.argmax()]
			if verbose:
				print(result, "\t", step_size, "\t", reference_result)
				print(evaluate(parameters,1000))
		# check termination criteria
		elif iteration_limit < iteration or step_size < minimum_step:
			#termination condition
			search = False
		print(iteration, "/1000", end = "\r")
	return parameters, reference_result/1.5
		
		
def create_variations(parameters, step_size, dim = 3):
	result = []
	for i in range(dim):
		displacement = np.zeros(dim) 
		displacement[i] = step_size
		result += [parameters + displacement, parameters - displacement]
	return result
		
if __name__ == "__main__":
	qp_1 = (np.sqrt(1/2), complex(0,np.sqrt(1/2)))
	qp_2 = (np.sqrt(1/2), np.sqrt(1/2))
	qp_3 = (1, 0)
	
	# print("2q")
	# for i in range(5):
		# print(optimize_circuit((qp_1, qp_2), 1000, 0.001, 7000, 0.0000001, 3, False))
		
	print("3q")
	for i in range(30):
		print(optimize_circuit((qp_1, qp_2, qp_3), 1000, 0.001, 7000, 0.0000001, 6, False))
	
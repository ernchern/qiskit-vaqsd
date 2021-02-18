import circuit
import cirquit_3q
import numpy as np
import cmath

def optimize_circuit(quantum_pairs, iteration_limit, initial_step_size, shot_size, minimum_step, dim = 3, verbose = True):

	if dim == 3:
		evaluate = lambda param, shot_size :circuit.build_circuit(param, quantum_pairs[0][0], quantum_pairs[0][1], quantum_pairs[1][0], quantum_pairs[1][1], shot_size)
		fit = lambda param, shot_size: evaluate(param, shot_size)[0]
	elif dim == 6 or dim == 12:
		evaluate = lambda param, shot_size :cirquit_3q.build_circuit(param, quantum_pairs[0][0], quantum_pairs[0][1], quantum_pairs[1][0], quantum_pairs[1][1], quantum_pairs[2][0], quantum_pairs[2][1], shot_size)
		fit = lambda param, shot_size: 3 * evaluate(param, shot_size)[0] - evaluate(param, shot_size)[1]
		
	
	iteration = 0
	# initial input
	parameters = np.random.rand(dim) * 2 * np.pi
	#parameters = np.array([6.15037858, 0.85563339, 3.328638  , 1.5923119 , 3.38266249, 5.14854546, 6.11542253, 2.75850265, 0.17123437, 4.75742343, 6.2216515 , 2.82630081])
	
	# evaluate with initial input
	reference_result = fit(parameters, shot_size)
	step_size = initial_step_size
	
	search = True
	while(search):
		# Take steps
		variations = create_variations(parameters, step_size, dim)
		
		# Evaluate all the variations
		result = []
		for step in variations:
			result.append(fit(step, shot_size))
		
		# Change current parameters to the best among 6
		result = np.array(result)
		iteration += 1
		
		# Adjust step size for better approximation
		
		# If new search has better result
		if result.max() > reference_result:
			step_size = (reference_result - result.max())/step_size
			reference_result = result.max()
			parameters = variations[result.argmax()]
			if verbose:
				print(result, "\t", step_size, "\t", reference_result)
				print(fit(parameters, shot_size))
				print("inconclusive")
				print(evaluate(parameters,shot_size)[1])
		# check termination criteria
		if iteration_limit < iteration or step_size < minimum_step or result.max() == 1:
			#termination condition
			search = False
		print(iteration, "/", iteration_limit, end = "\r")
	return parameters, evaluate(parameters, shot_size)[0]
		
		
def create_variations(parameters, step_size, dim = 3):
	result = []
	for i in range(len(parameters)):
		while parameters[i] > 2*np.pi:
			parameters[i] -= 2*np.pi
		while parameters[i] < 0:
			parameters[i] += 2*np.pi
	for i in range(dim):
		displacement = np.zeros(dim) 
		displacement[i] = step_size
		result += [parameters + displacement, parameters - displacement]
	return result
		

import circuit
import numpy as np

# counts_distribution =  circuit.evaluate(parameter, shot_size)

#evaluate = lambda params, shot_size: (circuit.build_circuit(params,0,shot_size/2)[1]+circuit.build_circuit(params,1,shot_size/2)[0])/2

evaluate = lambda param, shot_size :circuit.build_circuit(param, np.sqrt(1/3),np.sqrt(2/3),shot_size) 

def optimize_circuit(iteration_limit, initial_step_size, shot_size, minimum_step,verbose = True):
	
	iteration = 0
	# initial input
	parameters = np.random.rand(3) * 2 * np.pi
	
	# evaluate with initial input
	reference_result = evaluate(parameters, shot_size)
	step_size = initial_step_size
	
	search = True
	while(search):
		# Take steps
		variations = create_variations(parameters, step_size)
		
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
	return parameters, reference_result
		
		
def create_variations(parameters, step_size):
	nar = np.array
	return [nar([parameters[0] + step_size, parameters[1], parameters[2]]),
		nar([parameters[0] - step_size, parameters[1], parameters[2]]),
		nar([parameters[0], parameters[1] + step_size, parameters[2]]),
		nar([parameters[0], parameters[1] - step_size, parameters[2]]),
		nar([parameters[0], parameters[1], parameters[2] + step_size]),
		nar([parameters[0], parameters[1], parameters[2] - step_size])]
		
if __name__ == "__main__":
	for i in range(30):
		print(optimize_circuit(1000, 0.001, 7000, 0.0000001, False))
	
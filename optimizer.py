
import circuit

# counts_distribution =  circuit.evaluate(parameter, shot_size)

def optimize_circuit(iteration_limit, initial_step_size, shot_size, minimum_step):
	
	iteration = 0
	# initial input
	parameters = np.random.rand(3) * 2 * np.pi
	# evaluate with initial input
	reference_result = evaluate(parameters)
	
	step_size = initial_step_size
	
	search = True
	
	while(search):
		# take steps
		variations = create_variations(parameters, step_size)
		# evaluate and compare
		result = []
		for step in variations:
			result.append(evaluate(step, shot_size))
		
		# change current state to the optimal step and retry
		# if it's local optima, try smaller step
		# check termination criteria
		result = np.array(result)
		if result.max() > reference_result:
			reference_result = result.max()
			parameters = variations[result.argmax()]
		elif step_size > minimum_step:
			step_size = step_size / 2
		else:
			search = False
	return parameters, reference_result
		
		
def create_variations(parameters, step_size):
	nar = np.array
	return [nar(parameters[0] + step_size, parameters[1], parameters[2]),
		nar(parameters[0] - step_size, parameters[1], parameters[2]),
		nar(parameters[0], parameters[1] + step_size, parameters[2]),
		nar(parameters[0], parameters[1] - step_size, parameters[2]),
		nar(parameters[0], parameters[1], parameters[2] + step_size)],
		nar(parameters[0], parameters[1], parameters[2] - step_size)]
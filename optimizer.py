
import circuit
import numpy as np

# counts_distribution =  circuit.evaluate(parameter, shot_size)

evaluate = circuit.build_circuit

def optimize_circuit(iteration_limit, initial_step_size, shot_size, minimum_step):
	
	iteration = 0
	# initial input
	parameters = np.random.rand(3) * 2 * np.pi
	# evaluate with initial input
	reference_result = evaluate(parameters, shot_size)[1]
	
	step_size = initial_step_size
	
	search = True
	
	while(search):
		# take steps
		variations = create_variations(parameters, step_size)
		# evaluate and compare
		result = []
		for step in variations:
			result.append(evaluate(step, shot_size)[1])
		
		# change current state to the optimal step and retry
		# if it's local optima, try smaller step
		# check termination criteria
		result = np.array(result)
		print(result, end = "\t")
		iteration += 1
		if result.max() > reference_result:
			step_size = (reference_result - result.max())/step_size
			reference_result = result.max()
			parameters = variations[result.argmax()]
			print(step_size)
		#elif step_size > minimum_step:
			#step_size = step_size / 2
		elif iteration_limit < iteration or step_size < minimum_step:
			search = False
	print()
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
	print(optimize_circuit(1000, 0.1, 7000, 0.0000001) )
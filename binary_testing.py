from optimizer import *
import numpy as np

# plus_ = np.array((np.sqrt(1/2), np.sqrt(1/2)),dtype='d')
# minus_ = np.array((np.sqrt(1/2), -np.sqrt(1/2)),dtype='d')

# qp_1 = tuple(np.sqrt(1/2) * plus_ + np.sqrt(1/2) * minus_)
# qp_2 = tuple(np.sqrt(1/2) * plus_ + -np.sqrt(1/2) * minus_)
# qp_3 = tuple(plus_)

qp_1 = (1,0)
qp_2 = (0,1)
qp_3 = (np.sqrt(1/2),np.sqrt(1/2))

print (qp_1)
print (qp_2)
print (qp_3)

print("2q")
# for i in range(100):
	# print(optimize_circuit((qp_1, qp_2), 1000, 0.001, 7000, 0.0000001, 3, False))
	
print("3q")
p_succs = []
for i in range(30):
	temp = optimize_circuit((qp_1, qp_2, qp_3), 1000, 0.001, 7000, 0.0000001, 6, False) 
	print(temp)
	p_succs.append(temp[1])
print("average is: ", p_succs.average())
print("stddev is: ", p_succs.stddev())
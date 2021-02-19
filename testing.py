from optimizer import *
import numpy as np

# plus_ = np.array((np.sqrt(1/2), np.sqrt(1/2)),dtype='d')
# minus_ = np.array((np.sqrt(1/2), -np.sqrt(1/2)),dtype='d')

# qp_1 = tuple(np.sqrt(1/2) * plus_ + np.sqrt(1/2) * minus_)
# qp_2 = tuple(np.sqrt(1/2) * plus_ + -np.sqrt(1/2) * minus_)
# qp_3 = tuple(plus_)

qp_1 = (1,0)
qp_2 = (np.sqrt(1/2),np.sqrt(1/2))
qp_3 = (0,1)
qp_4 = (np.sqrt(1/2), complex(0,np.sqrt(1/2)))

print ("qp_1: ", qp_1)
print ("qp_2: ",qp_2)
print ("qp_3: ",qp_3)
print ("qp_4: ",qp_4)
p_succs=[]
print("2q qp_1 qp_2")
for i in range(100):
	temp = optimize_circuit((qp_1, qp_2), 50, 1, 7000, 0.03, 3, False)
	print(temp)
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
	
print("3q-1 qp_1 qp_2 qp_3")
p_succs = []
for i in range(50):
	temp = optimize_circuit((qp_1, qp_2, qp_3), 50, 1, 7000, 0.03, 12, False) 
	print(temp)
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())

print("3q-2 qp_1 qp_2 qp_4")
p_succs = []
for i in range(50):
	temp = optimize_circuit((qp_1, qp_2, qp_4), 50, 1, 7000, 0.03, 12, False) 
	print(temp)
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
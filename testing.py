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
qp_5 = (np.sqrt(1/4),np.sqrt(3/4))
qp_6 = (np.sqrt(3/4),np.sqrt(1/4))
qp_7 = (np.sqrt(1/3),np.sqrt(2/3))
qp_8 = (np.sqrt(2/3),np.sqrt(1/3))

print ("qp_1: ",qp_1)
print ("qp_2: ",qp_2)
print ("qp_3: ",qp_3)
print ("qp_4: ",qp_4)
print ("qp_5: ",qp_5)
print ("qp_6: ",qp_6)
print ("qp_7: ",qp_7)
print ("qp_8: ",qp_8)
print ()

p_succs=[]
print("2q-1 qp_1 qp_2")
for i in range(100):
	temp = optimize_circuit((qp_1, qp_2), 50, 1, 7000, 0.01, 3, False)
	print(temp[0],"\t","{:.5f}".format(temp[1]))
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
print()

p_succs = []
print("2q-2 qp_1 qp_3")
for i in range(100):
	temp = optimize_circuit((qp_1, qp_3), 50, 1, 7000, 0.01, 3, False)
	print(temp[0],"\t","{:.5f}".format(temp[1]))
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
print()

p_succs = []
print("2q-3 qp_7 qp_8")
for i in range(100):
	temp = optimize_circuit((qp_7, qp_8), 50, 1, 7000, 0.01, 3, False)
	print(temp[0],"\t","{:.5f}".format(temp[1]))
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
print()

p_succs = []
print("2q-4 qp_5 qp_6")
for i in range(100):
	temp = optimize_circuit((qp_5, qp_6), 50, 1, 7000, 0.01, 3, False)
	print(temp[0],"\t","{:.5f}".format(temp[1]))
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
print()
		
		
print("3q-1 qp_1 qp_2 qp_3")
p_succs = []
for i in range(50):
	temp = optimize_circuit((qp_1, qp_2, qp_3), 50, 1, 7000, 0.03, 12, False) 
	print(temp[0],"\t","{:.5f}".format(temp[1]))
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
print()

print("3q-2 qp_1 qp_2 qp_4")
p_succs = []
for i in range(50):
	temp = optimize_circuit((qp_1, qp_2, qp_4), 50, 1, 7000, 0.03, 12, False) 
	print(temp[0],"\t","{:.5f}".format(temp[1]))
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
print()

print("3q-3 qp_1 qp_5 qp_6")
p_succs = []
for i in range(50):
	temp = optimize_circuit((qp_1, qp_5, qp_6), 50, 1, 7000, 0.03, 12, False) 
	print(temp[0],"\t","{:.5f}".format(temp[1]))
	p_succs.append(temp[1])
print("average is: ", np.array(p_succs).mean())
print("stddev is: ", np.array(p_succs).std())
print()
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
simulator = Aer.get_backend('qasm_simulator')

matriz=[[0 for i in range (4)] for i in range (4)]

"circuito para la entrada 00 "
circuit = QuantumCircuit(2, 1)
circuit.barrier(0,1)
circuit.cx(0,1)
circuit.barrier(0,1)
circuit.measure([1],[0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

colum_0="00"
row_0="0"+str(list(counts.keys())[0])

#Pasar de numeros binarios a naturales para agregar completar la matriz
matriz[int(row_0,2)][int(colum_0,2)]=1

print("Resultado para "+colum_0+": "+row_0)
print(circuit)

"circuito para la entrada 01 "
circuit = QuantumCircuit(2, 1)
circuit.x(1)
circuit.barrier(0,1)
circuit.cx(0,1)
circuit.barrier(0,1)
circuit.measure([1],[0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

colum_1="01"
row_1="0"+str(list(counts.keys())[0])

#Pasar de numeros binarios a naturales para agregar completar la matriz
matriz[int(row_1,2)][int(colum_1,2)]=1

print("Resultado para 01:","0"+str(list(counts.keys())[0]))
print(circuit)

"circuito para la entrada 10 "
circuit = QuantumCircuit(2, 1)
circuit.x(0)
circuit.barrier(0,1)
circuit.cx(0,1)
circuit.barrier(0,1)
circuit.measure([1],[0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

colum_2="10"
row_2="1"+str(list(counts.keys())[0])

#Pasar de numeros binarios a naturales para agregar completar la matriz
matriz[int(row_2,2)][int(colum_2,2)]=1

print("Resultado para 10:","1"+str(list(counts.keys())[0]))
print(circuit)

"circuito para la entrada 11 "
circuit = QuantumCircuit(2, 1)
circuit.x(0)
circuit.x(1)
circuit.barrier(0,1)
circuit.cx(0,1)
circuit.barrier(0,1)
circuit.measure([1],[0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

colum_3="11"
row_3="1"+str(list(counts.keys())[0])

#Pasar de numeros binarios a naturales para agregar completar la matriz
matriz[int(row_3,2)][int(colum_3,2)]=1

print("Resultado para 11:","1"+str(list(counts.keys())[0]))
print(circuit)

print("La matriz correspondiente del circuito")
for i in matriz:
    print(*i)

#Resultado del algoritmo Deutsch en la función a

circuit = QuantumCircuit(2, 1)

circuit.x(1)
circuit.barrier(0,1)
circuit.h(0)
circuit.h(1)
circuit.barrier(0,1)

#función d
circuit.cx(0,1)

circuit.barrier(0,1)
circuit.h(0)
circuit.measure([0], [0])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

print("\nResultado del algoritmo Deutsch para la función d:",list(counts.keys())[0])
print(circuit)
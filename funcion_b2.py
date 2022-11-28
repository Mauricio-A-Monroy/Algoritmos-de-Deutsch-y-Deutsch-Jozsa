import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
simulator = Aer.get_backend('qasm_simulator')

matriz=[[0 for i in range (32)] for i in range (32)]

#Ciclo para probar todas las entradas posibles
for i in range(32):
    entrada = list('{0:05b}'.format(i))
    circuit = QuantumCircuit(5, 1)
    #Ciclo para completar la matriz
    for j in range(5):
        if entrada[j] == "1":
            circuit.x(j)
    #Circuito de la función
    circuit.barrier(0, 1, 2, 3, 4)
    circuit.toffoli(2,3,4)
    circuit.x(2)
    circuit.x(3)
    circuit.toffoli(2, 3, 4)
    circuit.x(2)
    circuit.x(3)
    circuit.barrier(0, 1, 2, 3, 4)
    circuit.measure([4], [0])

    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)

    colum_0 = '{0:05b}'.format(i)
    row_0 = colum_0[:4] + str(list(counts.keys())[0])

    # Pasar de numeros binarios a naturales para agregar completar la matriz
    matriz[int(row_0, 2)][int(colum_0, 2)] = 1

    print("Resultado para " + colum_0 + ": " + row_0)
    print(circuit)

print("La matriz correspondiente del circuito")
for i in matriz:
    print(*i)

#Implementación de Deutsch-Jozsa par esta función
circuit = QuantumCircuit(5, 4)
circuit.x(4)
circuit.barrier(0, 1, 2, 3, 4)
for i in range(5):
    circuit.h(i)
circuit.barrier(0, 1, 2, 3, 4)
circuit.toffoli(2,3,4)
circuit.x(2)
circuit.x(3)
circuit.toffoli(2, 3, 4)
circuit.x(2)
circuit.x(3)
circuit.barrier(0, 1, 2, 3, 4)
for i in range(4):
    circuit.h(i)
for i in range(4):
    circuit.measure([i], [i])

compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

print("\nResultado del algoritmo Deutsch-Jozsa para la función B:",list(counts.keys())[0])
print(circuit)
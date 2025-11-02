from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# 2. Apply a Hadamard gate to put the qubit into superposition
qc.h(0)

# 3. Measure the qubit
qc.measure(0, 0)

print("Circuit diagram:")
print(qc.draw())

# 4. Run the circuit on a simulator (USING THE WORKING METHOD)
simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(qc, shots=10000).result()

# 5. Get and print the results
counts = result.get_counts()
print("Measurement results:", counts)

# 6. Visualize the results as a histogram
plot_histogram(counts)
plt.show()

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)

qc.measure([0, 1], [0, 1])

print("circuit diagram")
print(qc.draw())

sim = Aer.get_backend('qasm_simulator')
result = sim.run(qc, shots=10000).result()
counts = result.get_counts()

print("Measurement result:", counts)
plot_histogram(counts)
plt.show()

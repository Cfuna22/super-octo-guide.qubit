print("Testing basic quantum functionality...")

from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Minimal quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Run it
backend = Aer.get_backend('qasm_simulator')
job = backend.run(qc, shots=100)
result = job.result()
counts = result.get_counts()

print("Circuit:", qc.draw())
print("Results:", counts)

if len(counts) == 2:
    print("🎉 PERFECT! Quantum superposition working!")
else:
    print("Results:", counts)

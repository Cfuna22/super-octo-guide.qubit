print("🧪 Testing Quantum Computing Setup...")

try:
    # Test imports
    from qiskit import QuantumCircuit
    from qiskit_aer import Aer
    from qiskit import execute
    from qiskit.visualization import plot_histogram
    import matplotlib.pyplot as plt
    
    print("✅ All imports successful!")
    
    # Test quantum circuit
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    
    print("✅ Quantum circuit created!")
    print("Circuit diagram:")
    print(qc.draw())
    
    # Test simulation
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=100).result()
    counts = result.get_counts(qc)
    
    print("✅ Quantum simulation working!")
    print(f"Results: {counts}")
    
    print("\n🎉 Everything is working perfectly!")
    print("You're ready for quantum computing!")
    
except Exception as e:
    print(f"❌ Error: {e}")

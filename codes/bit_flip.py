from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, random_statevector

from random import random

def get_encode_circuit():
    """
    returns a 3-qubit QuantumCircuit implementing the encoding circuit for the
    3-qubit bit-flip code.
    """
    
    enc_circuit = QuantumCircuit(3)
    
    enc_circuit.cx(0, 1)
    enc_circuit.cx(0, 2)
    
    return enc_circuit 


def get_channel_circuit():
    """
    returns a 3-qubit QuantumCircuit implementing a random 3-qubit channel 
    circuit with up to one bit-flip error.
    """
    
    channel_circuit = QuantumCircuit(3)

    p = random()

    if p < 0.25:
        channel_circuit.x(0)

    if .25 <= p < .5:
        channel_circuit.x(1)

    if .5 <= p <= .75:
        channel_circuit.x(2)

    return channel_circuit


def get_decode_circuit():
    """
    returns a 3-qubit QuantumCircuit implementing the decoding circuit for the
    3-qubit bit-flip code.
    """
    
    decode_circuit = QuantumCircuit(3)

    decode_circuit.cx(0, 1)
    decode_circuit.cx(0, 2)

    decode_circuit.ccx(1, 2, 0)

    return decode_circuit


def main():
    # create the complete circuit from the components
    encode_circuit = get_encode_circuit()
    channel_circuit = get_channel_circuit()
    decode_circuit = get_decode_circuit()

    circuit = QuantumCircuit(3)
    circuit.compose(encode_circuit, inplace=True)
    circuit.barrier()
    circuit.compose(channel_circuit, inplace=True)
    circuit.barrier()
    circuit.compose(decode_circuit, inplace=True)

    print(circuit)
    
    # create a random initial state
    state = random_statevector(2) # get a random dimension 2 state vector
    zerozero = Statevector.from_label('00')
    input_state = state
    print(f"input state: {state}")

    # run with initial state
    
    state.tensor(zerozero).evolve(circuit)
    output_state = state
    print(f"output state: {state}")

    if input_state == output_state:
        print("Successfully correct errors!")
    else:
        print("Uh oh... these don't look the same...")


if __name__ == "__main__":
    main()

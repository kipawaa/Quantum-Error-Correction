from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, random_statevector

from random import random

def get_encode_circuit():
    """
    returns a 9-qubit QuantumCircuit implementing the encoding circuit for
    Shor's code.
    """
    
    encode_circuit = QuantumCircuit(9)
    
    encode_circuit.cx(0, 3)
    encode_circuit.cx(0, 6)

    encode_circuit.h(0)
    encode_circuit.h(3)
    encode_circuit.h(6)

    encode_circuit.cx(0, 1)
    encode_circuit.cx(0, 2)
    
    encode_circuit.cx(3, 4)
    encode_circuit.cx(3, 5)

    encode_circuit.cx(6, 7)
    encode_circuit.cx(6, 8)
    
    return encode_circuit 


def get_channel_circuit():
    """
    returns a 9-qubit QuantumCircuit implementing a random channel with up to
    one error.
    """
    
    channel_circuit = QuantumCircuit(9)

    # apply a random error to a random qubit (or not)
    p = random()
    print(p)
    for i in range(9):
        if i / 9 <= p < (i + 1/3) / 9:
            channel_circuit.x(i)
        if (i + 1/3) / 9 <= p < (i + 2/3) / 9:
            channel_circuit.z(i)
        if (i + 2/3) / 9 <= p < (i + 1) / 9:
            channel_circuit.x(i)
            channel_circuit.z(i)

    return channel_circuit


def get_decode_circuit():
    """
    returns a 9-qubit QuantumCircuit implementing the decoding circuit for
    Shor's code.
    """
    
    decode_circuit = QuantumCircuit(9)

    decode_circuit.cx(0, 1)
    decode_circuit.cx(0, 2)
    decode_circuit.ccx(1, 2, 0)

    decode_circuit.cx(3, 4)
    decode_circuit.cx(3, 5)
    decode_circuit.ccx(4, 5, 3)

    decode_circuit.cx(6, 7)
    decode_circuit.cx(6, 8)
    decode_circuit.ccx(7, 8, 6)

    decode_circuit.h(0)
    decode_circuit.h(3)
    decode_circuit.h(6)

    decode_circuit.cx(0, 3)
    decode_circuit.cx(0, 6)
    decode_circuit.ccx(3, 6, 0)

    return decode_circuit


def main():
    # create the complete circuit from the components
    encode_circuit = get_encode_circuit()
    channel_circuit = get_channel_circuit()
    decode_circuit = get_decode_circuit()

    circuit = QuantumCircuit(9)
    circuit.compose(encode_circuit, inplace=True)
    circuit.barrier()
    circuit.compose(channel_circuit, inplace=True)
    circuit.barrier()
    circuit.compose(decode_circuit, inplace=True)

    print(circuit)
    
    # create a random initial state
    state = random_statevector(2) # get a random dimension 2 state vector
    zerozero = Statevector.from_label('00000000')
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

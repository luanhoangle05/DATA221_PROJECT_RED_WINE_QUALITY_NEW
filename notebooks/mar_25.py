import numpy as np

input_sequence = [1.0, 2.0, 3.0]

hidde_state = 0.0

for i in input_sequence:
    hidden_state = np.tanh(0.5
    * i + 0.8 * hidde_state)
    print("up hid seq:", hidde_state)

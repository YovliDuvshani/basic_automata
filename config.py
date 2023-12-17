AUTOMATA = {
    "A": ["B", "T0"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C", "E"],
    "E": ["D", "T1"],
}
INITIAL_NODE = "C"

NODE_EXPECTED_VALUES = {
    "A": 1 / 6,
    "B": 2 / 6,
    "C": 3 / 6,
    "D": 4 / 6,
    "E": 5 / 6,
}

INITIAL_V_VALUE = 0.5
NUMBER_OF_EPISODES = 10
ALPHA = 0.4
GAMMA = 1
N_STEP = 3

NUMBER_OF_SIMULATIONS = 3000

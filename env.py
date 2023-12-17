import random
from typing import Tuple

from config import AUTOMATA, INITIAL_NODE


class Env:
    def initial_state(self):
        return INITIAL_NODE

    def transition(self, state: str) -> Tuple[str, int, bool]:
        next_state = random.choice(AUTOMATA[state])
        if next_state == "T0":
            return next_state, 0, True
        elif next_state == "T1":
            return next_state, 1, True
        return next_state, 0, False

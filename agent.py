from typing import Tuple, List

from config import (
    AUTOMATA,
    INITIAL_V_VALUE,
    ALPHA,
    GAMMA,
)
from env import Env


class Agent:
    def __init__(self, env: Env, use_td_error: bool = False):
        self.env = env
        self.v = dict.fromkeys(list(AUTOMATA.keys()), INITIAL_V_VALUE)
        self.v["T0"] = 0
        self.v["T1"] = 0
        self.use_td_error = use_td_error

    def n_step_evaluate_policy(self, n: int, number_episodes: int):
        for _ in range(number_episodes):
            state = self.env.initial_state()
            loop = True
            t = 0
            encountered_states = []
            td_errors = []
            while loop:
                next_state, reward, terminal = self.env.transition(state)
                encountered_states += [(state, reward, terminal)]
                td_errors += [GAMMA * self.v[next_state] + reward - self.v[state]]
                state = next_state
                t += 1
                teta = t - n - 1
                if teta >= 0:
                    self.update_v(
                        teta=teta,
                        t=t,
                        n=n,
                        encountered_states=encountered_states,
                        use_n_next_state_value=True,
                        td_errors=td_errors,
                    )
                if terminal:
                    loop = False
            number_remaining_updates = min(len(encountered_states), n)
            for _ in range(number_remaining_updates):
                t += 1
                teta = t - number_remaining_updates - 1
                self.update_v(
                    teta=teta,
                    t=t,
                    n=n,
                    encountered_states=encountered_states,
                    use_n_next_state_value=False,
                    td_errors=td_errors,
                )

    def update_v(
        self,
        teta: int,
        t: int,
        n: int,
        encountered_states: List[Tuple[str, int, bool]],
        use_n_next_state_value: bool,
        td_errors: List[float],
    ):
        if self.use_td_error:
            self.v[encountered_states[teta][0]] += ALPHA * sum(
                [
                    GAMMA**k * td_error
                    for k, td_error in enumerate(td_errors[teta : t - 1])
                ]
            )
        else:
            sum_vn = sum(
                [
                    GAMMA**k * transition[1]
                    for k, transition in enumerate(encountered_states[teta : t - 1])
                ]
            )
            if use_n_next_state_value:
                sum_vn += GAMMA**n * self.v[encountered_states[t - 1][0]]
            self.v[encountered_states[teta][0]] += ALPHA * (
                sum_vn - self.v[encountered_states[teta][0]]
            )

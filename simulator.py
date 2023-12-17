from agent import Agent
from config import (
    NUMBER_OF_SIMULATIONS,
    AUTOMATA,
    NODE_EXPECTED_VALUES,
    NUMBER_OF_EPISODES,
    N_STEP,
)
from env import Env


class Simulator:
    def __init__(self, env: Env):
        self.env = env
        self.td_error_agent_errors_per_n_step = {}
        self.exact_agent_errors_per_n_step = {}

    def simulate(self):
        for step in range(NUMBER_OF_EPISODES):
            print(f"Starting with evaluating step={step}")
            exact_agent_errors = []
            td_agent_errors = []
            for _ in range(NUMBER_OF_SIMULATIONS):
                td_error_agent = Agent(self.env, use_td_error=True)
                td_error_agent.n_step_evaluate_policy(N_STEP, step)
                exact_agent = Agent(self.env, use_td_error=False)
                exact_agent.n_step_evaluate_policy(N_STEP, step)
                td_agent_errors.append(self._compute_l1_error(td_error_agent))
                exact_agent_errors.append(self._compute_l1_error(exact_agent))
            self.td_error_agent_errors_per_n_step[step] = (
                sum(td_agent_errors) / NUMBER_OF_SIMULATIONS
            )
            self.exact_agent_errors_per_n_step[step] = (
                sum(exact_agent_errors) / NUMBER_OF_SIMULATIONS
            )

    @staticmethod
    def _compute_l1_error(agent: Agent):
        errors = []
        states = AUTOMATA.keys()
        for state in states:
            errors.append(abs(agent.v[state] - NODE_EXPECTED_VALUES[state]))
        return sum(errors) / len(states)

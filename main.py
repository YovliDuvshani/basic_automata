from env import Env
from simulator import Simulator
import matplotlib.pyplot as plt

if __name__ == "__main__":
    env = Env()
    simulator = Simulator(env)
    simulator.simulate()

    plt.plot(
        list(simulator.exact_agent_errors_per_n_step.keys()),
        simulator.exact_agent_errors_per_n_step.values(),
        label="N_STEP_USING_EXACT_ERROR",
    )
    plt.plot(
        list(simulator.td_error_agent_errors_per_n_step.keys()),
        simulator.td_error_agent_errors_per_n_step.values(),
        label="N_STEP_USING_TD_ERRORS",
    )

    plt.legend()
    plt.xlabel("Step")
    plt.ylabel("ABS ERROR")

    plt.show()
    print()

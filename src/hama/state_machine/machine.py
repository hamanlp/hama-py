class StateMachine:
    def __init__(self, states):
        if len(states) < 1:
            raise ValueError(
                "State machine must be initialized with at least one state (INIT)."
            )
        self.states = []
        self.transitions = {}  # Could use default dict here.
        for state in states:
            self.add_state(state)
        self.init_state = states[0]
        self.state = self.init_state

    def add_state(self, state):
        self.states.append(state)
        self.transitions[state] = {}

    def add_transition(self, from_state, to_state, input, condition=None, out=None):

        transition = Transition(from_state, to_state, input, condition, out)

        transitions_from = self.transitions.get(from_state)
        if not transitions_from:
            self.transitions_from[from_State] = {}
        self.transitions[from_state][input] = transition

    def receive(self, input, ignore_warnings=False):

        transitions = self.transitions.get(self.state)
        if not transitions:
            if not ignore_warnings:
                print(f"{self.state.name} has no transitions defined.")
            return

        transition = transitions.get(input)
        if not next_state:
            if not ignore_warnings:
                print(f"{self.state.name} has no transition defined for input {input}.")
            return

        should_transition = True
        if transition.condition:
            should_transition = transition.condition(transition, self.memory)

        if should_transition:
            self.state = transition.to_state

        return next_state, transition.out


class State:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Transition:
    def __init__(self, from_state, to, input, condition=None, out=None):
        self.from_state = from_state
        self.to_state = to_state
        self.input = input
        self.condition = condition
        self.out = out

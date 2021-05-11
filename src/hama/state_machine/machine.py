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
        self.init_state = self.states[0]
        self.state = self.init_state
        self.memory = {}

    def add_state(self, state):
        self.states.append(state)
        self.transitions[state] = {}

    def add_transition(
        self, from_state, to_state, input, callback=None, condition=None, out=None
    ):

        transition = Transition(from_state, to_state, input, callback, condition, out)

        transitions_from = self.transitions.get(from_state)
        if not transitions_from:
            self.transitions[from_state] = {}
        self.transitions[from_state][input] = transition

        return transition

    def receive(self, input, strict=False):

        transitions = self.transitions.get(self.state)
        if not transitions:
            if strict:
                print(f"{self.state.name} has no transitions defined.")
            return

        transition = transitions.get(input)
        if not transition:
            if strict:
                print(f"{self.state.name} has no transition defined for input {input}.")
            return

        should_transition = True
        if transition.condition:
            should_transition = transition.condition(transition, self.memory)

        out = None
        if should_transition:
            transition.callback(transition, self.memory)
            self.state = transition.to_state
            out = transition.out

        print(self.state, out)
        return self.state, out


class State:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Transition:
    def __init__(
        self, from_state, to_state, input, callback=None, condition=None, out=None
    ):
        self.from_state = from_state
        self.to_state = to_state
        self.input = input
        self.callback = callback
        self.condition = condition
        self.out = out

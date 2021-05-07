import pytest

from hama import State, StateMachine, Transition


def test_state_init():
    s = State("INIT")
    assert s.name == "INIT"


def test_transition_init_basic():
    s0 = State("INIT")
    s1 = State("FIRST")
    t = Transition(s0, s1, 0)
    assert t.from_state == s0
    assert t.to_state == s1
    assert t.input == 0
    assert t.condition == None
    assert t.out == None


def test_transition_init_with_callback():
    s0 = State("INIT")
    s1 = State("FIRST")

    def callback(transition, memory):
        return True

    t = Transition(s0, s1, 0, callback)
    assert t.from_state == s0
    assert t.to_state == s1
    assert t.input == 0
    assert t.callback == callback
    assert t.condition == None
    assert t.out == None


def test_transition_init_with_condition():
    s0 = State("INIT")
    s1 = State("FIRST")

    def callback(transition, memory):
        return True

    def condition(transition, memory):
        return True

    t = Transition(s0, s1, 0, callback, condition)
    assert t.from_state == s0
    assert t.to_state == s1
    assert t.input == 0
    assert t.callback == callback
    assert t.condition == condition
    assert t.out == None


def test_transition_init_with_output():
    s0 = State("INIT")
    s1 = State("FIRST")

    def callback(transition, memory):
        return True

    def condition(transition, memory):
        return True

    t = Transition(s0, s1, 0, callback, condition, "OUT")
    assert t.from_state == s0
    assert t.to_state == s1
    assert t.input == 0
    assert t.callback == callback
    assert t.condition == condition
    assert t.out == "OUT"


def test_state_machine_empty_init():
    with pytest.raises(ValueError):
        fsm = StateMachine([])


def test_state_machine_init_single():

    s = State("INIT")

    fsm = StateMachine([s])
    assert fsm.states == [s]
    assert fsm.transitions[s] == {}
    assert fsm.init_state == s
    assert fsm.state == s
    assert fsm.memory == {}


def test_state_machine_init_multiple():

    s0 = State("INIT")
    s1 = State("FIRST")
    s2 = State("SECOND")
    s3 = State("THIRD")

    fsm = StateMachine([s0, s1, s2, s3])
    assert fsm.states == [s0, s1, s2, s3]
    assert fsm.transitions[s0] == {}
    assert fsm.transitions[s1] == {}
    assert fsm.transitions[s2] == {}
    assert fsm.transitions[s3] == {}
    assert fsm.init_state == s0
    assert fsm.state == s0
    assert fsm.memory == {}


def test_state_machine_add_transition():

    s0 = State("INIT")
    s1 = State("FIRST")

    def callback(transition, memory):
        return True

    def condition(transition, memory):
        return True

    fsm = StateMachine([s0, s1])
    transition = fsm.add_transition(s0, s1, 0, callback, condition, "OUT")
    assert fsm.states == [s0, s1]
    assert fsm.transitions[s0] == {0: transition}
    assert fsm.transitions[s1] == {}
    assert fsm.init_state == s0
    assert fsm.state == s0
    assert fsm.memory == {}


def test_state_machine_receive():

    s0 = State("INIT")
    s1 = State("FIRST")

    def callback(transition, memory):
        return True

    def condition(transition, memory):
        return True

    fsm = StateMachine([s0, s1])
    transition = fsm.add_transition(s0, s1, 0, callback, condition, "OUT")
    next_state, out = fsm.receive(0)
    assert next_state == s1
    assert out == "OUT"
    assert fsm.states == [s0, s1]
    assert fsm.transitions[s0] == {0: transition}
    assert fsm.transitions[s1] == {}
    assert fsm.init_state == s0
    assert fsm.state == s1
    assert fsm.memory == {}


def test_state_machine_receive_with_condition():

    s0 = State("INIT")
    s1 = State("FIRST")

    def callback(transition, memory):
        return True

    def condition(transition, memory):
        return False

    fsm = StateMachine([s0, s1])
    transition = fsm.add_transition(s0, s1, 0, callback, condition, "OUT")
    next_state, out = fsm.receive(0)
    assert next_state == s0
    assert out is None
    assert fsm.states == [s0, s1]
    assert fsm.transitions[s0] == {0: transition}
    assert fsm.transitions[s1] == {}
    assert fsm.init_state == s0
    assert fsm.state == s0
    assert fsm.memory == {}


def test_state_machine_receive_with_callback():

    s0 = State("INIT")
    s1 = State("FIRST")

    def callback(transition, memory):
        memory["temp"] = "Hello"

    def condition(transition, memory):
        return True

    fsm = StateMachine([s0, s1])
    transition = fsm.add_transition(s0, s1, 0, callback, condition, "OUT")
    next_state, out = fsm.receive(0)
    assert next_state == s1
    assert out == "OUT"
    assert fsm.states == [s0, s1]
    assert fsm.transitions[s0] == {0: transition}
    assert fsm.transitions[s1] == {}
    assert fsm.init_state == s0
    assert fsm.state == s1
    assert fsm.memory == {"temp": "Hello"}

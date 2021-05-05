import pytest

from hama import State, StateMachine, Transition


def test_state_init():
    s = State("INIT")
    assert s.name == "INIT"


def test_transition_init():
    s = State("INIT")
    assert s.name == "INIT"


def test_state_machine_empty_init():
    with pytest.raises(ValueError):
        fsm = StateMachine([])


def test_state_machine_single_init():

    s = State("INIT")

    fsm = StateMachine([s])
    assert fsm.states == [s]
    assert fsm.transitions[s] == {}
    assert fsm.init_state == s
    assert fsm.state == s


def test_state_machine_multiple_init():

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

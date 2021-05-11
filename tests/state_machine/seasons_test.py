import pytest

from hama import State, StateMachine, Transition


def test_seasons():

    spring = State("SPRING")
    summer = State("SUMMER")
    fall = State("FALL")
    winter = State("WINTER")

    states = [winter, spring, summer, fall]

    fsm = StateMachine(states=states)

    assert fsm.state == winter

    fsm.add_transition(winter, spring, 3, out="Switched to spring")
    fsm.add_transition(spring, summer, 6, out="Switched to summer")
    fsm.add_transition(summer, fall, 9, out="Switched to fall")
    fsm.add_transition(fall, winter, 12, out="Switched to winter")

    assert fsm.receive(1) == (winter, None)
    assert fsm.receive(2) == (winter, None)
    assert fsm.receive(3) == (spring, "Switched to spring")
    assert fsm.receive(4) == (spring, None)
    assert fsm.receive(5) == (spring, None)
    assert fsm.receive(6) == (summer, "Switched to summer")
    assert fsm.receive(7) == (summer, None)
    assert fsm.receive(8) == (summer, None)
    assert fsm.receive(9) == (fall, "Switched to fall")
    assert fsm.receive(10) == (fall, None)
    assert fsm.receive(11) == (fall, None)
    assert fsm.receive(12) == (winter, "Switched to winter")

import pytest
from hama import StateMachine

def test_state_machine_init():
    fsm = StateMachine()
    assert fsm.states == []
    assert fsm.transitions == []
    assert fsm.init_state = 0
    assert fsm.state = 0


    fsm = StateMachine([])

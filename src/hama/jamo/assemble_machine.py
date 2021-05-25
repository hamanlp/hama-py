from jamo import chosungs, jongsungs, joongsungs

from hama.state_machine import State, StateMachine


def store(transition, memory):
    memory["pending"].append(transition.input)
    return None


def flush_then_store(transition, memory):
    pending = memory["pending"]
    memory["pending"] = [transition.input]
    return pending


def store_then_flush(transition, memory):
    memory["pending"].append()
    pending = memory["pending"]
    memory["pending"] = []
    return pending


class AssembleMachine:
    def __init__(self):

        S0 = State("INIT")
        S1 = State("CHO")
        S2 = State("JOONG")
        S3 = State("CHO_JOONG")

        self.fsm = StateMachine(states=[S0, S1, S2, S3])

        for c in chosungs:
            self.fsm.add_transition(S0, S1, c, callback=store)
            self.fsm.add_transition(S1, S0, c, callback=flush_then_store)
            self.fsm.add_transition(S2, S0, c, callback=flush_then_store)
            self.fsm.add_transition(S3, S0, c, callback=flush_then_store)

        for c in joongsungs:
            self.fsm.add_transition(S0, S0, c, out=[c])
            self.fsm.add_transition(S1, S3, c, callback=store)
            self.fsm.add_transition(S2, S3, c, callback=flush_then_store)
            self.fsm.add_transition(S3, S0, c, callback=flush_then_store)

        for c in jongsungs:
            self.fsm.add_transition(S0, S0, c, out=[c])
            self.fsm.add_transition(S1, S0, c, callback=flush_then_store)
            self.fsm.add_transition(S2, S0, c, callback=flush_then_store)
            self.fsm.add_transition(S3, S0, c, callback=store_then_flush)

    def receive(self, sequence):
        for c in sequence: 
            _, out = self.fsm.receive(c)
            if out is not None:
                print('0', out)

AssembleMachine().receive(['ㅎ', 'ㅗ', 'ㅇ'])

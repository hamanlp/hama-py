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


store = "store"
flush_then_store = "flush_then_store"
store_then_flush = "store_then_flush"
flush_then_flush = "flush_then_flush"


class Assembler:
    def __init__(self):

        S0 = State("INIT")
        S1 = State("CHO")
        S2 = State("JOONG")
        S3 = State("CHO_JOONG")

        self.fsm = StateMachine(states=[S0, S1, S2, S3])
        self.unassembled_jamos = []

        for c in chosungs:
            self.fsm.add_transition(S0, S1, c, out=store)
            self.fsm.add_transition(S1, S0, c, out=flush_then_store)
            self.fsm.add_transition(S2, S0, c, out=flush_then_store)
            self.fsm.add_transition(S3, S0, c, out=flush_then_store)

        for c in joongsungs:
            self.fsm.add_transition(S0, S0, c, out=store)
            self.fsm.add_transition(S1, S3, c, out=store)
            self.fsm.add_transition(S2, S3, c, out=flush_then_store)
            self.fsm.add_transition(S3, S0, c, out=flush_then_store)

        for c in jongsungs:
            self.fsm.add_transition(S0, S0, c, out=store)
            self.fsm.add_transition(S1, S0, c, out=flush_then_store)
            self.fsm.add_transition(S2, S0, c, out=flush_then_store)
            self.fsm.add_transition(S3, S0, c, out=store_then_flush)

        self.fsm.add_wildcard_transition(S0, S0, out=flush_then_flush)
        self.fsm.add_wildcard_transition(S1, S0, out=flush_then_flush)
        self.fsm.add_wildcard_transition(S2, S0, out=flush_then_flush)
        self.fsm.add_wildcard_transition(S3, S0, out=flush_then_flush)

    def assemble(self, sequence):
        return "".join(self.assemble_character_by_character(sequence))

    def assemble_character_by_character(self, sequence):
        for c in sequence:
            _, out = self.fsm.receive(c)
            if out == store:
                self.unassembled_jamos.append(c)
            elif out == flush_then_store:
                if self.unassembled_jamos:
                    yield self.flush()
                self.unassembled_jamos = [c]
            elif out == store_then_flush:
                self.unassembled_jamos.append(c)
                yield self.flush()
            elif out == flush_then_flush:
                if self.unassembled_jamos:
                    yield self.flush()
                yield c

    def flush(self):

        chunk_length = len(self.unassembled_jamos)
        chosung = chosungs.index(chunk[0]) * 21 * 28 if chunk_length > 0 else 0
        joongsung = joongsungs.index(chunk[1]) * 28 if chunk_length > 1 else 0
        jongsung = jongsungs.index(chunk[2]) if chunk_length > 2 else 0

        assembled_code = chosung + joongsung + jongsung + 0xAC00
        return assembled_code


print(Assembler().assemble(["ㅎ", "ㅗ", "ㅇ"]))

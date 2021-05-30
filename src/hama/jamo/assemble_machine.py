from constants import (
    both_chosung_and_jongsung,
    chosungs,
    jongsungs,
    joongsungs,
    unique_to_chosungs,
    unique_to_jongsungs,
)

from hama.state_machine import State, StateMachine

store = "store"
flush_then_store = "flush_then_store"
store_then_flush = "store_then_flush"
flush_then_flush = "flush_then_flush"
take_then_flush = "take_then_flush"  # Flush all but stored jongsung.


class Assembler:
    def __init__(self):

        S0 = State("INIT")
        S1 = State("CHO")
        S2 = State("CHO_JOONG")
        S3 = State("CHO_JOONG_JONG")
        # In S3, we don't yet know if jongsung is part of next character.
        # Can't come to S3 with jongsung that can't be a chosung.

        self.fsm = StateMachine(states=[S0, S1, S2, S3])
        self.unassembled_jamos = []

        for c in unique_to_chosungs:
            self.fsm.add_transition(S0, S1, c, out=store)
            self.fsm.add_transition(S1, S1, c, out=flush_then_store)
            self.fsm.add_transition(S2, S1, c, out=flush_then_store)
            self.fsm.add_transition(S3, S1, c, out=flush_then_store)

        for c in joongsungs:
            self.fsm.add_transition(S0, S0, c, out=flush_then_flush)
            self.fsm.add_transition(S1, S2, c, out=store)
            self.fsm.add_transition(S2, S0, c, out=flush_then_flush)
            self.fsm.add_transition(S3, S2, c, out=take_then_flush)

        for c in unique_to_jongsungs:
            self.fsm.add_transition(S0, S0, c, out=flush_then_flush)
            self.fsm.add_transition(S1, S0, c, out=flush_then_flush)
            self.fsm.add_transition(S2, S0, c, out=store_then_flush)
            self.fsm.add_transition(S3, S0, c, out=flush_then_flush)

        for c in both_chosung_and_jongsung:
            self.fsm.add_transition(S0, S1, c, out=flush_then_store)
            self.fsm.add_transition(S1, S1, c, out=flush_then_store)
            self.fsm.add_transition(S2, S3, c, out=store)
            self.fsm.add_transition(S3, S1, c, out=flush_then_store)

        self.fsm.add_wildcard_transition(S0, S0, out=flush_then_flush)
        self.fsm.add_wildcard_transition(S1, S0, out=flush_then_flush)
        self.fsm.add_wildcard_transition(S2, S0, out=flush_then_flush)
        self.fsm.add_wildcard_transition(S3, S0, out=flush_then_flush)

    def assemble(self, sequence):
        assembled = self.assemble_character_by_character(sequence)
        return "".join(assembled)

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
            elif out == take_then_flush:
                if self.unassembled_jamos:
                    jong = self.unassembled_jamos[-1]
                    self.unassembled_jamos = self.unassembled_jamos[:-1]
                    if self.unassembled_jamos:
                        yield self.flush()
                    self.unassembled_jamos = [jong, c]
        yield self.flush()

    def flush(self):

        if not self.unassembled_jamos:
            return ""

        chunk = self.unassembled_jamos
        chunk_length = len(chunk)
        chosung = chosungs.index(chunk[0]) * 21 * 28 if chunk_length > 0 else 0
        joongsung = joongsungs.index(chunk[1]) * 28 if chunk_length > 1 else 0
        jongsung = jongsungs.index(chunk[2]) if chunk_length > 2 else 0

        assembled_code = chosung + joongsung + jongsung + 0xAC00

        self.unassembled_jamos = []

        return chr(assembled_code)


if __name__ == "__main__":
    print(Assembler().assemble(["ㅁ", "ㅝ", "ㄹ", "ㅏ", "ㄱ", "ㅗ", "ㅇ", "ㅛ", "?"]))

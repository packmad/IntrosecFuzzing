import random
from abc import ABC


class Mutator(ABC):
    def __init__(self, obj):
        self.obj = obj
        self.mut_functions = [m for m in dir(self.__class__) if m.startswith('mut_')]

    def mutate(self, times: int = 1) -> str:
        tmp_obj = self.obj
        for _ in range(times):
            tmp_obj = getattr(self, random.choice(self.mut_functions))(tmp_obj)
        return tmp_obj


class StringMutator(Mutator):
    def __init__(self, obj):
        assert isinstance(obj, str)
        super().__init__(obj)

    def mut_delete_random_character(self, s: str) -> str:
        """Returns s with a random character deleted"""
        if s == "":
            return s
        pos = random.randint(0, len(s) - 1)
        return s[:pos] + s[pos + 1:]

    def mut_insert_random_character(self, s: str) -> str:
        """Returns s with a random character inserted"""
        pos = random.randint(0, len(s))
        random_character = chr(random.randrange(32, 127))
        return s[:pos] + random_character + s[pos:]

    def mut_flip_random_character(self, s: str):
        """Returns s with a random bit flipped in a random position"""
        if s == "":
            return s
        pos = random.randint(0, len(s) - 1)
        c = s[pos]
        bit = 1 << random.randint(0, 6)
        new_c = chr(ord(c) ^ bit)
        return s[:pos] + new_c + s[pos + 1:]


class IntMutator(Mutator):
    def __init__(self, obj):
        assert isinstance(obj, int)
        super().__init__(obj)
        self.obj_bit_length = self.obj.bit_length()

    def mut_bitflip(self, i: int) -> int:
        return i ^ (1 << random.randint(0, i.bit_length()))

    def mut_shift_left(self, i: int):
        return i << random.randint(0, i.bit_length() * 2)

    def mut_shift_right(self, i: int):
        return i >> random.randint(0, i.bit_length())


if __name__ == '__main__':
    im = IntMutator(6)
    sm = StringMutator('ciao')
    for _ in range(0, 1000):
        print(im.mutate(4), sm.mutate())

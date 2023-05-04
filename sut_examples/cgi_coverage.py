from typing import Set, List, Callable, Tuple

from myfuzzer.Coverage import StatementCoverage, Location
from myfuzzer.Fuzzer import RandomFuzzer

"""Decode the CGI-encoded string `s`:
   * replace '+' by ' '
   * replace "%xx" by the character with hex number xx.
   Return the decoded string.  Raise `ValueError` for invalid inputs."""
def cgi_decode(s: str) -> str:
    hex_values = { # Mapping of hex digits to their integer values
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }

    t = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c == '+':
            t += ' '
        elif c == '%':
            digit_high, digit_low = s[i + 1], s[i + 2]
            i += 2
            if digit_high in hex_values and digit_low in hex_values:
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            else:
                raise ValueError("Invalid encoding")
        else:
            t += c
        i += 1
    return t


if __name__ == '__main__':
    trials = 100
    population = []
    rf = RandomFuzzer()
    for i in range(trials):
        population.append(rf.fuzz())

    cumulative_coverage: List[int] = []
    all_coverage: Set[Location] = set()
    input_crashes = set()
    for s in population:
        with StatementCoverage() as cov:
            try:
                cgi_decode(s)
            except:
                input_crashes.add(s)
                pass
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))

    import matplotlib.pyplot as plt
    plt.plot(cumulative_coverage)
    plt.title('Coverage of cgi_decode() with random inputs')
    plt.xlabel('# of inputs')
    plt.ylabel('Lines covered')
    #plt.savefig('cgi_decode_coverage.png')
    plt.show()


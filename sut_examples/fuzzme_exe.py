import os
import sys

from os.path import abspath, join, isfile
from myfuzzer.Runner import *
from myfuzzer.Timer import Timer

if __name__ == '__main__':
    fuzzme_exe_path = join(abspath(join(os.getcwd(), os.pardir)), 'fuzzme_exe', 'fuzzme.exe')
    assert isfile(fuzzme_exe_path)

    # Make the file executable
    os.chmod(fuzzme_exe_path, os.stat(fuzzme_exe_path).st_mode | 0o111)

    pr = ProgramRunner(fuzzme_exe_path)

    # TODO: we need a fuzzer!

    with Timer() as t:
        while True:
            cp, outcome = pr.run('1', '2', '3', 'xyz')
            if t.elapsed_time() > 3600.0:
                sys.exit('The CPU is ready to cook pasta')
            if outcome == Runner.PASS:
                print('You got the flag!', cp.stdout)
                break
            elif outcome == Runner.FAIL:
                print(cp)
                if cp.stdout == '':
                    sys.exit('This should not happen :(')
                coverage_level = int(cp.stdout.split('\n')[-2])  # Coverage feedback
                print(coverage_level)

                # TODO: mutate the arguments ( myfuzzer.Mutator class will help )

                # TODO: ... ?

            elif outcome == Runner.UNRESOLVED:
                print('Wrong usage: ', cp.stderr)

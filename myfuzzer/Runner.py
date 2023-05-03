from typing import Tuple, List, Any, Union, Callable, Set
import subprocess

from myfuzzer.Coverage import Coverage, Location, StatementCoverage
from abc import ABC, abstractmethod
Outcome = str


class Runner(ABC):
    """Base class for testing inputs."""

    # Test outcomes
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"

    @abstractmethod
    def run(self, *args) -> Any:
        pass


class PrintRunner(Runner):
    """Simple runner, printing the input."""

    def run(self, *args) -> Any:
        """Print the given input"""
        print(args)
        return args, Runner.UNRESOLVED


class FunctionRunner(Runner):
    def __init__(self, function: Callable) -> None:
        """Initialize.  `function` is a function to be executed"""
        self.function = function

    def run_function(self, args: Tuple) -> Any:
        return self.function(*args)

    def run(self, args: Tuple) -> Tuple[Any, str]:
        try:
            result = self.run_function(args)
            outcome = self.PASS
        except Exception as e:
            print(e)
            result = None
            outcome = self.FAIL

        return result, outcome


class FunctionCoverageRunner(FunctionRunner):

    def __init__(self, function: Callable, coverage_strategy: Callable) -> None:
        super().__init__(function)
        self._coverage_strategy = coverage_strategy

    def run_function(self, args: Tuple) -> Any:
        self._coverage = None
        with self._coverage_strategy() as cov:
            try:
                result = super().run_function(args)
            except Exception as exc:
                self._coverage = cov.coverage()
                raise exc
        self._coverage = cov.coverage()
        return result

    def coverage(self) -> Set[Location]:
        return self._coverage


class ProgramRunner(Runner):
    """Test a program with inputs."""

    def __init__(self, program: str) -> None:
        """`program` is the path to an executable file"""
        self.program = program

    def run_process(self, args: Tuple) -> subprocess.CompletedProcess:
        """Run the program with `inp` as input.
           Return result of `subprocess.run()`."""
        args = list(args)
        args.insert(0, self.program)
        return subprocess.run(args,
                              capture_output=True,
                              universal_newlines=True)

    def run(self, *args) -> Tuple[subprocess.CompletedProcess, Outcome]:
        """Run the program with `inp` as input.
           Return test outcome based on result of `subprocess.run()`."""
        result = self.run_process(args)

        if result.returncode == 0:
            outcome = self.PASS
        elif result.returncode == 1:
            outcome = self.FAIL
        else:
            outcome = self.UNRESOLVED
        return result, outcome

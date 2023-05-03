import inspect
import sys
from typing import Any, Optional, Callable, List, Type, Set, Tuple, Mapping
from types import FrameType, TracebackType
from abc import ABC, abstractmethod

Location = Tuple[str, int]


class Coverage(ABC):
    @abstractmethod
    def coverage(self) -> Set[Location]:
        pass


class StatementCoverage(Coverage):
    """Track coverage within a `with` block. Use as
    ```
    with Coverage() as cov:
        function_to_be_traced()
    c = cov.coverage()
    ```
    """

    def __init__(self) -> None:
        """Constructor"""
        self._trace: List[Location] = []
        self._fun_to_src: Mapping[str, Any] = dict()
        self._max_cov = None

    # Trace function
    def traceit(self, frame: FrameType, event: str, arg: Any) -> Optional[Callable]:
        """Tracing function. To be overloaded in subclasses."""
        if self.original_trace_function is not None:
            self.original_trace_function(frame, event, arg)
        if event == "line":
            function_name = frame.f_code.co_name
            if function_name != '__exit__':  # avoid tracing ourselves:
                self._trace.append((function_name, frame.f_lineno))
                if function_name not in self._fun_to_src:
                    self._fun_to_src[function_name] = inspect.getsourcelines(frame.f_code)
        return self.traceit

    def __enter__(self) -> Any:
        """Start of `with` block. Turn on tracing."""
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.traceit)
        return self

    def __exit__(self, exc_type: Type, exc_value: BaseException,
                 tb: TracebackType) -> Optional[bool]:
        """End of `with` block. Turn off tracing."""
        sys.settrace(self.original_trace_function)
        return None  # Propagate exceptions

    def trace(self) -> List[Location]:
        """The list of executed lines, as (function_name, line_number) pairs"""
        return self._trace

    def coverage(self) -> Set[Location]:
        """The set of executed lines, as (function_name, line_number) pairs"""
        return set(self.trace())

    def max_coverage(self) -> Set[Location]:
        if self._max_cov is not None:
            return self._max_cov
        self._max_cov = set()
        for function_name, v in self._fun_to_src.items():
            source_lines, start_line_number = v
            for lineno in range(start_line_number, start_line_number + len(source_lines)):
                self._max_cov.add((function_name, lineno))
        return self._max_cov

    def function_names(self) -> Set[str]:
        """The set of function names seen"""
        return set(function_name for (function_name, line_number) in self.coverage())

    def __repr__(self) -> str:
        """Return a string representation of this object.
           Show covered (and uncovered) program code"""
        t = ""
        for function_name in self.function_names():
            if function_name not in self._fun_to_src:
                continue
            source_lines, start_line_number = self._fun_to_src[function_name]
            for lineno in range(start_line_number, start_line_number + len(source_lines)):
                if (function_name, lineno) in self.trace():
                    t += "# "
                else:
                    t += "  "
                t += "%2d  " % lineno
                t += source_lines[lineno - start_line_number]
        return t


if __name__ == '__main__':  # Usage example

    def gt2le8(x: int) -> bool:
        if x > 2:
            print('x > 2')
            if x < 8:
                print('x < 8')
                return True
        return False

    with StatementCoverage() as cov:
        try:
            gt2le8(99)
        except:
            pass
    print('Trace: ', cov.trace())
    print('>>>')
    print(cov)
    print('<<<')



import sys


class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return self

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print(self.reverse_write('ZeroDivisionError'))
            return True  # The exception is suppressed


if __name__ == "__main__":
    with LookingGlass() as lg:
        print('Hi, my name is Alice')
        x = 42 / 0
        print('Unreachable')
    print("That's All Folks!")

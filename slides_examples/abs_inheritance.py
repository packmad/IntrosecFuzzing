from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    def __init__(self, scientific_name: str):
        self.scientific_name = scientific_name

    @abstractmethod
    def print_sound(self) -> None:
        pass


class Dog(Animal):
    def __init__(self):
        super().__init__('Canis familiaris')

    def print_sound(self) -> None:
        print(f'Bau! I am a {self.scientific_name}')


class Cat(Animal):
    def __init__(self):
        super().__init__('Felis catus')

    def print_sound(self) -> None:
        print(f'Miao! I am a {self.scientific_name}')


if __name__ == "__main__":
    try:
        a = Animal()
    except TypeError as e:
        print(e)  # Can't instantiate abstract class Animal with abstract method print_sound
    animals: List[Animal] = [Dog(), Cat()]
    for animal in animals:
        animal.print_sound()

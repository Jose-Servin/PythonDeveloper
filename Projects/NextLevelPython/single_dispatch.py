# type: ignore
# NOTE: In Python, explicit type arguments for generics like List[T] (where T is the type of list elements) are more about providing detailed information to static type checkers and less about affecting runtime behavior.
# Since singledispatch function is designed to work with any type of list, using just list as the type annotation is appropriate here.
# However, pylance will think that the typing is incorrect or not fullfilled.
from functools import singledispatch
from typing import Any


@singledispatch
def add(x: Any, y: Any) -> Any:
    raise NotImplementedError("Unsupported type")


@add.register
def _(x: int, y: int) -> int:
    return x + y


@add.register
def _(x: float, y: float) -> float:
    return x + y


@add.register
def _(x: str, y: str) -> str:
    return f"{x} {y}"


@add.register
def _(x: list, y: list) -> list:
    return x + y


@add.register
def _(x: tuple, y: tuple) -> tuple:
    return x + y


@add.register
def _(x: dict, y: dict) -> dict:
    return {**x, **y}


def main() -> None:
    print(add(1, 2))                          # Integers
    print(add("Hello", "World"))              # Strings
    print(add(3.5, 4.5))                      # Floats
    print(add([1, 2], [3, 4]))                # Lists
    print(add((1, 2), (3, 4)))                # Tuples
    print(add({'a': 1}, {'b': 2}))            # Dictionaries


if __name__ == "__main__":
    main()

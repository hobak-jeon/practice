"""Module providing asterisk examples."""

from functools import reduce
from typing import Any

# 0. Multiplication and power operations.
MUL = 2 * 3  # 6
POWER = 2**3  # 8


# 1. Repeatedly extending the list-type containers.
zeros_list: list[int] = [0] * 5
zeros_tuple: tuple[int] = (0,) * 5
vector_list: list[list[int]] = [[1, 2, 3]]

for idx, value in enumerate(vector_list * 3):
    print([(idx + 1) * e for e in value])


# 2. Using the variadic arguments. (so-called “packing”)
# *args (positional arguments): tuple
# **kwargs (keyword arguments): dict
# * (keyword-only arguments): dict


def positional_arguments(i: int, j: int, *args: tuple[int]) -> None:
    """2.1. Function providing an example for positional arguments (*args)."""
    print(i, j)  # 1 2
    print(args)  # (3, 4, 5)


def keyword_arguments(q: int, r: int, **kwargs: dict[str, int]) -> None:
    """2.2. Function providing an example for keyword arguments (**kwargs)."""
    print(q, r)
    print(kwargs)


def keyword_only_arguments(m: int, n: int, *, o: int, p: int = 10) -> None:
    """2.3. Function providing an example for keyword-only arguments (*)."""
    # Arguments must be passed as keyword arguments after "*".
    print(m, n, o, p)


positional_arguments(1, 2, 3, 4, 5)  # Deliver a tuple (*args = (3, 4, 5)) to function.

keyword_arguments(
    7, 8, x=100, y=200
)  # Deliver a dictionary ({'x': 100, 'y': 200}) to function.

keyword_only_arguments(1, 2, o=3)  # 1 2 3 10
keyword_only_arguments(3, 4, o=5, p=11)  # 3 4 5 11
# list.sort(*, key=None, reverse=False)


# 3. Unpacking the containers.
def product(*numbers: tuple[int]) -> int:
    """_Function providing multiplication_

    Args:
        numbers (_tuple[int]_): _Unpacking tuple_

    Returns:
        _type_: _int_
    """
    return reduce(lambda x, y: x * y, numbers)


primes: list[int] = [2, 3, 5, 7, 11, 13]
print(product(*primes))  # Returns 30030 <- (2, 3, 5, 7, 11, 13)
print(product(primes))  # An only argument ([2, 3, 5, 7, 11, 13])


def pre_process(**headers: dict[str, Any]) -> None:
    """_preprocess headers_

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
    """
    text_type: str = headers["Accept"]
    content_length: int = int(headers["Content-Length"])
    host: str = headers["Host"]

    if "https" not in host:
        raise ValueError("You must use SSL for http communication.")

    if text_type != "text/plain":
        raise ValueError("Text type is plain only.")

    if content_length > 500:
        raise ValueError("length should be less than 500.")


headers_dict: dict[str, Any] = {
    "Accept": "text/plain",
    "Content-Length": 348,
    "Host": "https://mingrammer.com",
}
pre_process(**headers_dict)


integers: list[int] = [1, 2, 3, 4, 5, 6]

# left side should be a tuple or a list.
(*a,) = integers  # a = [1, 2, 3, 4, 5, 6]
*a, b = integers  # a = [1, 2, 3, 4, 5],  b = 6
(
    a,
    *b,
) = integers  # a = 1, b = [2, 3, 4, 5, 6]
a, *b, c = integers  # a = 1, b = [2, 3, 4, 5], c = 6

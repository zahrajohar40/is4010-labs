def make_greeting(name: str) -> str:
    """Return exactly 'Hello, NAME!' using the supplied name."""
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    """Return True when number is even and False otherwise."""
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Return the number of a, e, i, o, and u characters in text."""
    return sum(character in "aeiou" for character in text.lower())
    
import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    story = (
        f"Once upon a time, there was a {adjective} {noun} who loved to {verb} "
        f"every single day. Everyone in town agreed the {noun} was the most "
        f"{adjective} creature they had ever seen, especially when it would "
        f"{verb} across the fields at sunset."
    )
    return story


def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You guessed it!")
            break
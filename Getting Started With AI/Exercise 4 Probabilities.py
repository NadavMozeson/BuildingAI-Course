import random

def main():

    favourite = "dogs"  # change this

    val = random.random()

    if 0.8 < val <= 0.9:
        favourite = "cats"

    if 0.9 < val <= 1:
        favourite = "bats"

    print("I love " + favourite)


main()

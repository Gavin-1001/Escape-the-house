import sys
import time

def terminal_typing_effect(text, speed):
    # https://stackoverflow.com/questions/20302331/typing-effect-in-python
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


def two_choices(prompt, opt1, opt2, path1, path2):
    """
    Allows for the input(prompt) of an option(opt1/op2)
    with two outcomes(path1,path2).
    When a user enters a correct option the loop is passed
    and the given path is executed.
    """
    while True:
        choice = input(prompt)
        if choice == opt1:
            path1()
            break
        elif choice == opt2:
            path2()
            break
        else:
            print()
            print(f"Please enter a valid option! ({opt1} or {opt2})\n")
            continue

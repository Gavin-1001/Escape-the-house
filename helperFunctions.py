import sys
import time

def terminal_typing_effect(text, time):

    for chars in text:
        sys.stdout.write(chars)
        sys.stdin.flush()
        time.sleep(time)

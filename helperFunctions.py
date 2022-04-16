import sys
import time

def terminal_typing_effect(text, time):
#https://stackoverflow.com/questions/20302331/typing-effect-in-python
    for chars in text:
        sys.stdout.write(chars)
        sys.stdin.flush()
        time.sleep(time)

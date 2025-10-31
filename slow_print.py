from time import sleep
import sys

def sp(text = "PLACEHOLDER", speed = 0.1):
    for char in text:
        sys.stdout.write(char)
        sleep(speed)
        sys.stdout.flush()
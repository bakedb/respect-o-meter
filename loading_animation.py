import random, sys
from time import sleep

def loading(loading_text = "Loading...", sleep_time = 0.5):
    loop = 0
    loops = random.randint(5, 20)
    retain_loop = True
    while retain_loop == True:
        if loop == 0:
            loading_animation = "|"
            loop = 1
        elif loop == 1:
            loading_animation = "/"
            loop = 2
        elif loop == 2:
            loading_animation = "-"
            loop = 3
        elif loop == 3:
            loading_animation = "\\"
            loop = 0
        print(f"{loading_text} {loading_animation}")
        sleep(sleep_time)
        sys.stdout.write("\033[F") # move cursor up
        sys.stdout.write("\033[K") # clear line
        sys.stdout.flush()

        loops -= 1
        if loops <= 0:
            retain_loop = False
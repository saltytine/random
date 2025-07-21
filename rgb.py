import random
import time
while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    print(f"\033[38;2;{r};{g};{b}m1337mode\033[0m", end="\r")
    time.sleep(0.05)

import time, math, random, os
from dotenv import load_dotenv


load_dotenv()

SPEED = float(os.getenv("SPEED", 1))


def sleep(seconds):
    """
    Sleep for a random amount of time, with a sinusoidal variation.
    using non linear sleep time to avoid detection of the bot
    """
    random_factor = random.uniform(0.5, 1.5)
    sinusoidal_seconds = seconds * (1 + 0.5 * math.sin(random_factor * math.pi))
    time.sleep(sinusoidal_seconds / SPEED)

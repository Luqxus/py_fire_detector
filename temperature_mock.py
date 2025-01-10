import random
import time
from network import send_temperature

def simulate_temperature():
    # Simulate a temperature reading between 20 and 30 degrees Celsius
    while True:
        temp = round(random.uniform(20.0, 30.0), 2)

        print('simulated temperature : {}'.format(temp))
        send_temperature(int(temp))
        time.sleep(30)
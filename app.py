import threading

from fire_detector import fire_detector
from temperature_mock import simulate_temperature



if __name__ == '__main__':
    threading.Thread(target=simulate_temperature, group=None).start()
    threading.Thread(target=fire_detector, group=None).start()
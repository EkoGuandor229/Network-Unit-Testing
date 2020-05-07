import logging
import os
import sys

from nuts import network_test_controller


def _init_logger():
    log_path = os.path.join(os.path.join(os.path.abspath(__file__)), '..',  'nuts.log')
    file_handler = logging.FileHandler(filename=log_path)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter('%(message)s'))

    logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])


if __name__ == "__main__":
    _init_logger()
    network_test_controller.run()

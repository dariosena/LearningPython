
import logging

import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def add(num1, num2):
    """Add Function"""
    return num1 + num2


def subtract(num1, num2):
    """Subtract Function"""
    return num1 - num2


def multiply(num1, num2):
    """Multiply Function"""
    return num1 * num2


def divide(num1, num2):
    """Divide Function"""
    try:
        result = num1 / num2
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero.')
    else:
        return result


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

add_result = subtract(num_1, num_2)
logger.debug('Subtract: {} - {} = {}'.format(num_1, num_2, add_result))

add_result = multiply(num_1, num_2)
logger.debug('Multiply: {} * {} = {}'.format(num_1, num_2, add_result))

add_result = divide(num_1, num_2)
logger.debug('Divide: {} / {} = {}'.format(num_1, num_2, add_result))

add_result = divide(num_1, 0)
logger.debug('Divide: {} / {} = {}'.format(num_1, num_2, add_result))

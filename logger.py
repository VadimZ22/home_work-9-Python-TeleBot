from datetime import datetime as dt
from time import time

def log(operation, data):
    time = dt.now().strftime('%D,%H,%M')
    with open('logs.txt', 'a', encoding='utf-8') as file:
        file.write('{}, {}, {}\n'.format(time, operation, data))
    return

# def log_out(operation, format, data):
#     time = dt.now().strftime('%D,%H,%M')
#     with open('logs.txt', 'a', encoding='utf-8') as file:
#         file.write('{}, {}, {}, {}\n'.format(time, operation, data, format))
#     return
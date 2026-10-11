
'''
Run three tasks concurrently using ThreadPoolExecutor.
Wait for their results and display a completion message.
'''

from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    print(f'Task name: {name} started')
    time.sleep(2)
    print(f'Task name: {name} completed')
    return f'Task name: {name} finished'


with ThreadPoolExecutor(max_workers=3) as executor:
    f1 = executor.submit(task, 'Task-1')
    f2 = executor.submit(task, 'Task-2')
    f3 = executor.submit(task, 'Task-3')

    print(f1.result())
    print(f2.result())
    print(f3.result())

print('All tasks are completed')
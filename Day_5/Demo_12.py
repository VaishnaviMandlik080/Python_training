'''
Run three tasks sequentially.
Each task pauses for two seconds.
Measure and display the total execution time.
'''

import time


def task(name):
    print(f'Task name: {name} started')
    time.sleep(2)
    print(f'Task name: {name} completed')


start = time.perf_counter()

task('Task - 1')
task('Task - 2')
task('Task - 3')

end = time.perf_counter()

print(f"Total execution time: {end - start:.2f} secs")
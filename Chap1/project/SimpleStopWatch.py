# This script helps to build a simple stopwatch application using Python's time module

import time

print('Press ENETER to begin, Press Ctrl + c to stop')
while True:
    try:
        input() #for ENETER
        starttime = time.time()
        print('Started: ')
    except KeyboardInterrupt:
        print('Stopped')
        endtime = time.time()
        # round 数字精确到两位
        print('Total time:', round(endtime-starttime, 2), 'secs')
        break

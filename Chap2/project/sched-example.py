#!/usr/bin/env python

import os
import sys
import time
import sched


def jumpoff(arg=None):
    print("[]%f] It's the jumpoff! (%s)" % (time.time(), str(arg)))
    return


def sleep(units):
    if units == 0:
        print("Yielding...")
        return

    print("[%f] We are going to sleep for %f units" % (time.time(), units))
    time.sleep(units)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    s = sched.scheduler(time.time, sleep)
    s.enter(10, None, jumpoff, argument=(1, ))

    print("Queue\n=====")
    print(s.queue)

    s.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())

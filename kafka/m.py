#!/usr/bin/env python3
from multiprocessing import Process
from consumer import main
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    groupid = args[0]
    consumers_to_run = int(args[1])

    process_list = []

    for _ in range(consumers_to_run):
        process = Process(target=main, args=(groupid,))
        process_list.append(process)

    for process in process_list:
        process.start()
        print(f"Started process with PID: {process.pid}")

    print(f'Spawned {consumers_to_run} processes')

    for process in process_list:
        process.join()

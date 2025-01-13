from multiprocessing import Queue, Process
from multiprocessing import current_process
import time

tasks = [i for i in range(10)]
tasks_to_accomplish = Queue()
tasks_that_are_done = Queue()
processes = []

def processing(tasks_to_accomplish) :
    try :
        num = tasks_to_accomplish.get_nowait()
    except :
        print('finish')
    print(f"Task no {num}")
    time.sleep(0.5)
    tasks_that_are_done.put(num)
    print(f"Task no 0 is done by {current_process().name}")

def main() :

    for task in tasks :
        tasks_to_accomplish.put(task)

    for i in range(4) :
        proc = Process(name = f'Process {i}', target = processing, args = (tasks_to_accomplish,))
        proc.start()
        processes.append(proc)

    for proc in processes :
        proc.join()

if __name__ == "__main__" :
    main()


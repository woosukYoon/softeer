from multiprocessing import Pool
import time

def work_log(work):

    name, duration = work
    start = int(time.time())
    print(f'process {name} waiting {duration} seconds')
    time.sleep(duration)
    print(f'process {name} finished')

def main() :
    work = [('A', 5), ('B', 2), ('C', 1), ('D', 3)]
    pool = Pool(2)
    pool.map(work_log, work)

if __name__ == "__main__":
    main()
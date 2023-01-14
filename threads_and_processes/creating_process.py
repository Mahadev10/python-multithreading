from multiprocessing import Process
import multiprocessing
def func(val):
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work",val)

if __name__=='__main__':
    multiprocessing.set_start_method('spawn')
    for i in range(5):
        p = Process(target=func,args=(i,))
        p.start()
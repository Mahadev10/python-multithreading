from threading import Thread

def func(val):
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work",val)

for i in range(5):
    th = Thread(target=func,args=(i,))
    th.start()
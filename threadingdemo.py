#process=program under execution
#thread=lightweight program , part of a program
#cycle of thread : create , runnable , runnings , dead/ runnable

#from threading import Thread
# def dsp():
#     for i in range(1,5):
#         print("child thread")
# t=Thread(target=dsp)
# t.start()
# for i in range(1,5):
#     print("Main thread started")

# from threading import Thread
# import time
# #s=time.time()
# def dsp():
#     for i in range(1,11):
#         time.sleep(1)
#         print(2**i)
# def spd():
#     for i in range(1,11):
# #        time.time(1)
#         print(5**i)
# btime=time.time()
# t1=Thread(target=dsp)
# t2=Thread(target=spd)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Total time is :",time.time()-btime)

#Lock and R-lock are synchroization tools but can be applied for only 1 thread
#if more threads then use semaphores

from threading import *
import time
l=Semaphore(2)
def wish(name):
    l.acquire()
    for i in range(5):
        print("Good Morning ",name,end="")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=("Rahul ",))
t2=Thread(target=wish,args=("Steve ",))
t3=Thread(target=wish,args=("TechHub ",))
t4=Thread(target=wish,args=("Odia ",))
t5=Thread(target=wish,args=("Barik ",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
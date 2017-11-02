# def fib(n):
#     if(n<=1):
#         return n
#     else:
#         return (fib(n-1)+fib(n-2))
# nterms=10
# for i in range(nterms):
#     print(fib(i))
# def fibc(n):
#     a,b=0,1
#     for i in range(n-1):
#         a=b
#         b=a+b
#     return a
# print(fibc(5))
#fibonacci
# a,b=0,1
# for i in range(10):
#     c=a+b
#     a=b
#     b=c
#     print(c,' ',end='')

import threading


class PrintNumbers(threading.Thread):
    def __init__(self, start_number, end_number, step, set_event, clear_event):
        threading.Thread.__init__(self)
        self.start_number = start_number
        self.end_number = end_number
        self.step = step
        self.set_event = set_event
        self.clear_event = clear_event

    def run(self):
        for i in range(self.start_number, self.end_number, self.step):
            print(i)
            self.set_event.set()
            self.clear_event.clear()
            self.clear_event.wait()
        self.set_event.set()


threading_event1 = threading.Event()
threading_event2 = threading.Event()

t1 = PrintNumbers(0, 10, 2, threading_event1, threading_event2)
t2 = PrintNumbers(1, 10, 2, threading_event2, threading_event1)

t1.start()
t2.start()

t1.join()
t2.join()
    
    
    
   

    

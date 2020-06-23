import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.size = self.n+1
        self.e = threading.Lock()
        self.o = threading.Lock()
        self.z = threading.Lock()
        self.e.acquire()
        self.o.acquire()
        
           
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        is_even = False
        for v in range(1,self.size):
            self.z.acquire()
            printNumber(0)
            if is_even == True:
                self.e.release()
                is_even = False
            else: # is_even = False
                self.o.release()
                is_even = True
        
          
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for v in range(1,self.size):
            if v % 2 == 0:
                self.e.acquire()
                printNumber(v)
                self.z.release()
        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for v in range(1,self.size):
            if v % 2 == 1:
                self.o.acquire()
                printNumber(v)
                self.z.release()
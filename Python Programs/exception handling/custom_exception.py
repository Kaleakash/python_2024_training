import sys;
class MyException(Exception):           # sub class of exception 
    def __init__(self,msg):
        super().__init__(msg);              # we set the message to super class constructor 
a=10;
b=50;
try:
    if a > b:
        raise ValueError("a value must be > b");
    else: 
        raise MyException("b value must be > a");   # passing msg to constructor 
except:
    print(sys.exc_info());
import sys;
try:
    result = 100/0;
    print("Result ",result);
finally:
    print("Finally block excecute");
    print(sys.exc_info());
print("Normal Statement");
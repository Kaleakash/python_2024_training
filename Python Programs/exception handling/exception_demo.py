# try :
#     print(fname);
# except:
#     print("I Take Care!")
import sys;
a=10;
b=0;
try:
    result = a/b;
    print("Result is ",result);
except ZeroDivisionError:
    print("exception generated");
    print(sys.exc_info()[0]);
    print(sys.exc_info()[1]);
except TypeError:
     print("Generic Exception")
     print(sys.exc_info()[0]);
     print(sys.exc_info()[1]);
except :
    print("Generic Exeption");
    print(sys.exc_info()[0]);
    print(sys.exc_info()[1]);

print("hello");
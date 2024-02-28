'''def info():   # no passing parameter and no return type 
    print("Welcome to user defined function");
info();
info();
info();'''
'''def add_number(a,b):   # passing parameter but no return type 
    sum = a+b;
    print("Sum of two number is ",sum);
add_number(10,20);
add_number(100,200);'''
'''
def check_user_details(emailid,password):       #passing parameter and return value 
    if emailid=="akash@gmail.com" and password=="123":
        return "success";
    else:
        return "failure";
result1 = check_user_details("akash@gmail.com","123");
result2 = check_user_details("lex@gmail.com","123");
print(result1);
print(result2);'''
#name="akash";
#print(f'{name}');
'''def emp_info(id,name,salary,*tech):
    print("Employee details");
    print("id is ",id);
    print("name is ",name);
    print("salary is ",salary);
    print("technology",len(tech));
    print(tech);
emp_info(1,"Ravi",15000);
emp_info(2,"Steven",25000,"Python","ReactJS");
emp_info(3,"Lex",35000,"Java");'''

'''def sayHello():
    print("Normal function");
sayHello();

sayHi = lambda:print("This is simple lambda expression function");
sayHi();

def add_number1(a,b):
    sum = a+b;
    return sum;
print(add_number1(100,200));
# lambda keyword, number of parameter and third expression no return keyword by default return 
add_number2=lambda a,b:a+b;
print(add_number2(100,200));'''
'''result = (lambda a,b:a+b)(100,200)
print(result);'''
list1 = [1,2,3,4,5,6,7,8,9,10];
evennumber = list(filter(lambda n:n%2==0,list1));
oddnumber = list(filter(lambda n:n%2!=0,list1));
print(list1);
print(evennumber);
print(oddnumber);
result = list(map(lambda n:pow(n,2),list1));
print(result);



























    


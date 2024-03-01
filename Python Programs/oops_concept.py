# empty Car class blue print ready
'''class Car:
    pass;
'''
# Car with behaviour
'''class Car:
    def start(self):
        print("Car Started");
    def stop(self):
        print("Car Stop");
#start();
#stop();
innova = Car(); #innova reference name of Car class
innova.start(); # objectname.functionName();
innova.stop();'''
# Car class with property and behaviour
'''class Car:
    wheel=4;            # instance variable 
    colour="Gray";
    price=2000000;
    def displayCarInfo(self):
        print("Car Details");
        print("Wheel for the car ",self.wheel);
        print("Colour for the car ",self.colour);
        print("Price for the car ",self.price);
innova = Car();         # we are calling function using object name ie innova
santro=Car();
print("wheel is ",innova.wheel);
print("colour is ",innova.colour);
print("price is ",innova.price);
innova.displayCarInfo();
santro.displayCarInfo();'''
'''class Car:
    wheel=None 
    colour=None
    price=None
    def set_value(self,wheel,colour,price):
        self.wheel=wheel;
        self.colour=colour;
        self.price=price;
    def displayCarInfo(self,msg):
        print("Car Details ",msg);
        print("Wheel for the car ",self.wheel);
        print("Colour for the car ",self.colour);
        print("Price for the car ",self.price);
innova = Car();         
santro=Car();
innova.set_value(4,"White",2000000);
santro.set_value(4,"Gray",1200000);
innova.displayCarInfo("Innova Car");
santro.displayCarInfo("Santro Car");'''
'''class Employee:
    def display(self):
        print("hello");
Employee();     # heap memory created..
print(Employee());
print(Employee());
Employee().display();
Employee().display();
Employee().display();
emp1 = Employee();
emp1.display();
emp1.display();
emp1.display();'''
# empty constructor using __init__ function
'''class Employee:
    def __init__(self):
        print("object created");
    def display(self):
        print("employee function");
Employee();
Employee().display();
Employee().display();
emp1 = Employee();
emp1.display()
emp1.display();
emp1.display();'''
# parameterized constructor 
'''class Employee:
    def __init__(self,eid,name,salary):
        self.eid=eid;
        self.name=name;
        self.salary=salary;
    def display_info(self):
        print("Employee details ");
        print(f'Id is {self.eid} name is {self.name} salary is {self.salary}');
emp1=Employee(100,"Ravi",12000);
emp1.display_info();
emp2=Employee(101,"Raj",14000);
emp2.display_info();'''
# construtor using __init__ with different parameter 
'''class Employee:
    def __init__(self,eid=0,name=None,salary=8000):
        self.eid=eid;
        self.name=name;
        self.salary=salary;
    def display_info(self):
        print("Employee details ");
        print(f'Id is {self.eid} name is {self.name} salary is {self.salary}');
emp1=Employee(100,"Ravi",12000);
emp1.display_info();
emp2=Employee(101,"Raj");
emp2.display_info();
emp3=Employee(102);
emp3.display_info();
emp4=Employee();
emp4.display_info();'''
# python with pre destructor
'''class Employee:
    def __init__(self):
        print("memory created");
    def display(self):
        print("business function");
    def __del__(self):
        print("pre destructor clean the resources");
emp1=Employee();
emp1.display();
emp1.display();
del emp1;
print("done!");'''
'''class Employee:
    def __init__(self,eid,name,__salary):
        self.eid=eid;
        self.name=name;
        self.__salary=__salary;
    def display(self):
        print(f'id is {self.eid}name is {self.name} salary is {self.__salary}');
emp1 = Employee(100,"Ravi",12000);
emp1.salary=-15000;
#print(emp1.__salary);  # private property 
emp1.display();'''
'''class A :                   #super class 
    def a_fun(self):
        print("A class function");
class B(A) :            # sub class 
    def b_fun(self):
        print("B class function");
obj1=A();
obj2=B();
obj1.a_fun();
obj2.b_fun();
obj2.a_fun();'''

# single inheritance 
'''class Employee:
    eid=0;
    name="";
    salary=0;
    def read_emp(self):
        self.eid = int(input("Enter the id "));
        self.name =   input("Enter the name ");
        self.salary = float(input("Enter the salary "));
    def cal_salary(self):
        self.salary = float(self.salary)+5000;
    def dis_emp(self):
        print(f'Id is {self.eid} name is {self.name} salary is {self.salary}');

class Manager(Employee):
    numberofemp=0;
    def read_mgr(self):
        self.read_emp();
        self.numberofemp=int(input("Enter the number of employee working under him"));
    def dis_mgr(self):
        self.dis_emp();
        print(f'Number of employee working under him{self.numberofemp}');
emp1 = Employee();
emp1.read_emp();
emp1.cal_salary();
emp1.dis_emp();
mgr1 = Manager();
#mgr1.read_emp();
mgr1.read_mgr();
mgr1.cal_salary();
#mgr1.dis_emp();
mgr1.dis_mgr();'''

# mutliple inheritance : more than one super class and one sub class
'''
class A:
    def a_fun(self):
        print("A class function");
    def dis(self):
        print("A class dis function");
class B :
    def b_fun(self):
        print("B class function");
    def dis(self):
        print("B class dis function");
class C(B,A):
    def c_fun(self):
        print("C class function");
obj1 =C();
obj1.a_fun();
obj1.b_fun();
obj1.c_fun();
obj1.dis();'''
'''
class Operation :
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c;
        elif a!=None and b!=None and c==None:
            return a+b;
        elif a!=None and b==None and c==None:
            return a;
        else:
            0;
op1 = Operation();
print(op1.add(10,20,30));
print(op1.add(10,20));
print(op1.add(10));
print(op1.add());'''
# function overriding example
'''class Bike:
    def speed(self):
        print("speed 60km/hr");
class Honda(Bike):
    def color(self):
        print("Color :Black");
class Pulsar(Bike):
    def color(self):
        print("Color :Gray");
    def speed(self):            # pulsar class speed overriding Bike class speed function 
        print("speed 90km/hr");
class Tvs(Bike):
    def color(self):
        print("Color :Red");
    def speed(self):
        super().speed();            # merge both speed function calling super class speed.
        print("20km/hr");
pu=Pulsar();
hh=Honda();
pu.color();
pu.speed();
hh.color();
hh.speed();
tv = Tvs();
tv.color();
tv.speed();'''
'''
class A :
    def __init__(self):
        print("A class object created");
class B(A):
    def __init__(self):
        super().__init__();
        print("B class object created");
b = B();'''

# abstrat method concept 
'''
class Bike:
    def speed(self):            #abstract method sub class need to provide the body 
        raise "Provide the body for speed function";
class Honda(Bike):
    def color(self):
        print("Color :Black");
    def speed(self):            # pulsar class speed overriding Bike class speed function 
        print("speed 40km/hr");
class Pulsar(Bike):
    def color(self):
        print("Color :Gray");
    def speed(self):            # pulsar class speed overriding Bike class speed function 
        print("speed 90km/hr");
hh=Honda();
pu=Pulsar();
hh.speed();
pu.speed();'''

# abstract method with @abtractmethod decorator
#from abc import abstractmethod;
'''class Bike:
    #@abstractmethod
    def speed(self):
        raise "need to provide body";
class Honda(Bike):
    def color(self):
        print("Color :Black");
    def speed(self):
        print("speed 40km/hr");
class Pulsar(Bike):
    def color(self):
        print("Color :Gray");
    def speed(self):            # pulsar class speed overriding Bike class speed function 
        print("speed 90km/hr");
hh=Honda();
pu=Pulsar();
hh.speed();
pu.speed();'''

class Sample:
    id=100;
    def fun1(self):         #instance function
        self.name="Akash";
        print("Instance function",self.id);
        print("name is ",self.name);
    @staticmethod
    def fun2():
        print("static function",Sample.id);     # only one copy of the memory
        #print("name is ",Sample.name);
    @classmethod
    def fun3(cls):
        cls.name="Vikash";
        print("class function",cls.id);
        print("class variable",cls.name);
obj1=Sample();      #instance memory 
obj2=Sample();      #instance memory 
obj1.id=200;
obj2.id=300;
obj1.fun1();
obj2.fun1();
obj1.fun2();            # only one copy of that value 
obj2.fun2();            # only one copy of that value
Sample.id=1111;
Sample.fun2();      # if my function is static we can class with help of class name 

obj1.fun3();
obj2.fun3();
Sample.fun3();









        



        








        




























            





























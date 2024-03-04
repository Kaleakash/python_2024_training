from operation import add,sub,mul,div;

import bank.sbi as obj1;
import hsbc as obj2;
print("Welcome to user defined modules");
print(add(10,20));
print(sub(100,50));
print(mul(100,20));
print(div(100,20));
print(obj1.withdraw());
print(obj2.withdraw())
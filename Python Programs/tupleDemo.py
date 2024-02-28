tuple1 = ();
tuple2 = tuple();
print(type(tuple1));
print(type(tuple2));
tuple3 = (100,200,300,400);
print(tuple3);
print(tuple3[0]);
print(len(tuple3));
'''a=tuple3[0];
b=tuple3[1];
c=tuple3[2];
d=tuple3[3];
print(a,b,c,d);'''
a,b,c,d=tuple3;
print(a,b,c,d);
print(dir(tuple1));




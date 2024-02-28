set1 = set();
print(set1);
print(type(set1));
set2 = {10,3,6,2,8,10,5,8,"A",True};
print(set2);
set2.add(100);
set2.add(200);
print(set2);
set2.update([111,222,333,444]);
print(set2);
set2.remove(222);   # if element present it remove that element else generate error or exception 
print(set2);
set2.discard(2222); # if element present it remove else no error generate 
print(set2);





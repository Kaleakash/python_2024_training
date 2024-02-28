list1=[];
print(list1);
print(len(list1));
print(type(list1));

list2=[2,4,7,1,9,6,4,7,10];
print(list2);  # display all elements  
print(len(list2));  # check the size of the list 
print(type(list2)); # check the type of reference 
print(list2[0]);#access the element using index position 
print(list2[1]);
print(list2[8]);
list2.append(11);   # added the element at last 
list2.append(12);
print(list2);
list2.remove(4); # remove using value 
print(list2);
list2.insert(4,100);    # 1st parameter index and 2nd parameter value
print(list2);
list2.pop();        # remove last elements from list
print(list2);
list2.sort();   # sort by asc
print(list2);
list2.reverse();
print(list2); #sort by desc
print(dir(list2));











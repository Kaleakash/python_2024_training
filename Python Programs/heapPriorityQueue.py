import heapq;
list=[];
heapq.heappush(list,(6,"6th Task"));
heapq.heappush(list,(3,"3rd Task"));
heapq.heappush(list,(2,"2nd Task"));
heapq.heappush(list,(4,"4th Task"));
first_element = heapq.heappop(list);
print(first_element);
print(dir(heapq));

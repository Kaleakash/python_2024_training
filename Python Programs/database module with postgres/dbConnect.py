import psycopg2;
import sys;
try:
    con = psycopg2.connect(
        database="my_db_info",
        host="localhost",
        user="postgres",
        password="postgres",
        port="5432"
    );
    print("database connected....");
    cursor = con.cursor();
    # retrieve query 
    #cursor.execute("select * from product");
    #cursor.execute("select * from product where price > 50000");
    # retrieve first record from the product table 
    # print(cursor.fetchone());
    # retrieve all the records from database 
    # print(cursor.fetchall());
    # retrieve all records using loop 
    # for product in cursor.fetchall():
    #     #print(product);
    #     print("Pid is ",product[0],"Product Name ",product[1]," Price ",product[2]);
    
    # insert query DML 
    # cursor.execute("insert into product values(5,'Computer',4500)");
    # if cursor.rowcount > 0:
    #     print("Record inserted successfully");    
    # con.commit(); 
    
    # delete query 
    # cursor.execute("delete from product where pid=1");
    # if cursor.rowcount > 0:
    #     print("Record deleted successfully");    
    # else:
    #     print("Record not present");
    
    # con.commit();    
    
    # update query 
    cursor.execute("update product set price = 50000 where pid = 100");
    if cursor.rowcount > 0:
        print("Record updated successfully");    
    else:
        print("Record not present");
    con.commit();    
except:
    print(sys.exc_info()[0]);
    print(sys.exc_info()[1]);
print("done!")


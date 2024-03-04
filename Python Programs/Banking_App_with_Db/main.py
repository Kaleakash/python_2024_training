import psycopg2;
import sys;
def connect_db():
    global con;
    global cursor;
    try:
        con = psycopg2.connect(
            database="my_db_info",
            host="localhost",
            user="postgres",
            password="postgres",
            port="5432"
        );
        cursor= con.cursor();
    except:
        print(sys.exc_info());

connect_db();

con2="yes";
def customer_info(emailid):
    global con2;
    global temp_account;
    cursor.execute("select * from account where emailid=%s",[emailid]);
    print("Account number in customer info function");
    #print(cursor.fetchone());  
    temp_account= cursor.fetchone()[0];
    print("your account number is ",temp_account) 
    while con2=="yes":     
        print("2 : Check Balance, 3 :Withdraw 4:Deposite");   
        choice = int(input("Enter your choice")); 
        # if choice==1:
        #     accno = int(input("Enter the account number"));
        #     name = input("Enter the name");
        #     amount = float(input("Enter the amount"));
        #     cursor.execute("insert into account values(%s,%s,%s)",(accno,name,amount));
        
        #     if cursor.rowcount > 0:
        #         print("account created successfully");
        #     else :
        #         print("Account didn't create");
        #     con.commit();
        
        if choice==2:
            #accno = int(input("Enter the account number"));
            cursor.execute("select * from account where accno=%s",[temp_account]);
            if cursor.statusmessage=='SELECT 1':
                 print(cursor.fetchone());
            else:
                print("Invalid accno");    
            
        if choice==3:
            #accno = int(input("Enter the account number"));
            amount = float(input("Enter the amount"));
            cursor.execute("update account set amount = amount - %s where accno=%s",(amount,temp_account));
        
            if cursor.rowcount > 0:
                print("amount withdrawn successfully");
            else :
                print("Account is invalid");
            con.commit();
            
        if choice==4:
            #accno = int(input("Enter the account number"));
            amount = float(input("Enter the amount"));
            cursor.execute("update account set amount = amount + %s where accno=%s",(amount,temp_account));
        
            if cursor.rowcount > 0:
                print("amount deposite successfully");
            else :
                print("Account is invalid");
            con.commit();
        
        con2=input("Cutomer Menu Option continue?(yes/no)")    
    
    
def manager_info():
    print("1:Check All Customer Details");
    cursor.execute("select * from account");
    for customer in cursor.fetchall():
        print(customer);  
        
con1 = "yes";
while con1 == "yes":
    print("1:SignIn 2 :SignUp");   
    choice = int(input("Enter your choice"));
    if choice ==1:
        emailid = input("Enter your emailid");
        password = input("Enter your password");
        typeofuser = input("type of user");
        cursor.execute("select * from login where emailid=%s and password=%s and typeofuser=%s",(emailid,password,typeofuser));
        if cursor.statusmessage=='SELECT 1':
            print("successfully login")
            if typeofuser=="manager":
                manager_info();
            else:
                #print(cursor.fetchone()[0])
                customer_info(cursor.fetchone()[0]);
        else:
            print("Failure try once again")
    if choice ==2:
        emailid = input("Enter your emailid");
        password = input("Enter your password");
        typeofuser = input("type of user");
        cursor.execute("insert into login values(%s,%s,%s)",(emailid,password,typeofuser));
        
        if cursor.rowcount > 0:
            print("Account created succesfully");
            if typeofuser=="customer":
                camount = 1000; 
                cursor.execute("insert into account(emailid,amount) values(%s,%s)",(emailid,camount));
        else:
            print("Emailid must be unique");
        
    
    con.commit();
    con1 = input("do you want to continue(yes/no)");
    
    
print("Done!")



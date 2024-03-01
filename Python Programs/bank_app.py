listofaccout=[];
def createAccount():
    flag=0;
    accno=int(input("Enter the account number "));
    name=input("Enter the name ");
    amount=float(input("Enter the amount "));
    account={"accno":accno,"name":name,"amount":amount};
    for accountinfo in listofaccout:
        if accountinfo.get("accno")==accno:
                flag=1;
                break;
    
    if flag==1:
        print("Account id must unique");
    else:
         listofaccout.append(account);
         print("Account created successfully");

def displayAccountDetails():
     for accountinfo in listofaccout:
         print(f'account number {accountinfo.get("accno")} name {accountinfo.get("name")} amount {accountinfo.get("amount")}');

def checkBalance():
    flag=0;
    accno=int(input("Enter the account number "));
    for accountinfo in listofaccout:
        if accountinfo.get("accno")==accno:
                print(f'your balance amount is {accountinfo.get("amount")}');
                flag=1;
                break;
    if flag==0:
        print("Account not present");
        flag=0;

def withdraw():
    flag=0;
    accno=int(input("Enter the account number "));
    newamount=float(input("Enter the amount with withdrawn "));
    for accountinfo in listofaccout:
        if accountinfo.get("accno")==accno:
                oldamount= accountinfo.get("amount");
                oldamount = oldamount -newamount;
                accountinfo.update({"amount":oldamount})
                print("Amount withdrawn successfully");
                flag=1;
                break;
    if flag==0:
        print("Account not present");
        flag=0;
def desposite():
    flag=0;
    accno=int(input("Enter the account number "));
    newamount=float(input("Enter the amount with desposite "));
    for accountinfo in listofaccout:
        if accountinfo.get("accno")==accno:
                oldamount= accountinfo.get("amount");
                oldamount = oldamount + newamount;
                accountinfo.update({"amount":oldamount})
                print("Amount desposite successfully");
                flag=1;
                break;
    if flag==0:
        print("Account not present");
        flag=0;         
option = "yes";
while option=="yes":
    print("1:Create Account 2 :Display all account details 3:check the balance 4:withdrawn5:desposite");
    choice = int(input("Enter your choice"));
    if choice == 1:
      createAccount();
    elif choice== 2:
        displayAccountDetails();
    elif choice == 3:
        checkBalance();
    elif choice==4:
        withdraw();
    elif choice == 5:
        desposite();
    else:
        print("wrong choice");
    option = input("do you want to continue(yes/no)");
print("Thank you!");




    





               
    

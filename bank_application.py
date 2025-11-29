import random
class bank:
    accounts=[]
    def create_account(self):
        details={}
        details['Holder_name']=input("Enter the account holder name:").lower()
        details['Phone_number']=int(input("Enter the phone number:"))
        details['Aadhar_number']=int(input("Enter the aadhar number:"))
        details['IFSC_code']='SBIN000123'
        details['Account_number']=random.randint(100000000000,999999999999)
        print('''
              For savings account minium deposit amount is 500
              For current account minimum depoit amount is 1000
              ''')
        details['Account_type']=input("Enter the account type(savings/current):").lower()
        while True:
            if details['Account_type']=='savings':
                deposit_amount=int(input("Enter the deposit amount:"))
                if deposit_amount>=500:
                    details['Balance']=deposit_amount
                    break
                else:
                    print("Deposit amount is less than minimum required amount for savings account.")
            elif details['Account_type']=='current':
                deposit_amount=int(input("Enter the deposit amount:"))
                if deposit_amount>=1000:
                    details['Balance']=deposit_amount
                    break
                else:
                    print("Deposit amount is less than minimum required amount for current account.")
            else:
                print("Invalid account type. Please enter either 'savings' or 'current'.")
                details['Account_type']=input("Enter the account type(savings/current):").lower()
        bank.accounts.append(details)
        print("Account created successfully. Your account number is:",details['Account_number'])
    def Deposit(self):
        while True:
            name=input("Enter the account holder name:").lower()
            acc_num=int(input("Enter the account number:"))
            for i in bank.accounts:
                if i['Holder_name']==name and i['Account_number']==acc_num:
                    deposit_amount=int(input("Enter the amount to be deposited:"))
                    i['Balance']+=deposit_amount
                    print("Amount deposited successfully. New balance is:",i['Balance'])
                    break
            else:
                print("Account not found.Try again")
                continue
            break
    def Withdraw(self):
        while True:
            name=input("Enter the account holder name:").lower()
            acc_num=int(input("Enter the account number:"))
            for i in bank.accounts:
                if i['Holder_name']==name and i['Account_number']==acc_num:
                    withdraw_amount=int(input("Enter the amount to be withdrawn:"))
                    if i['Balance']>=withdraw_amount:
                        i['Balance']-=withdraw_amount
                        print("Amount withdrawn successfully. New balance is:",i['Balance'])
                    else:
                        print("Insufficient balance.")
                    break
            else:
                print("Account not found.Try again")
                continue
            break
    def check_balance(self):
        while True:
            name=input("Enter the account holder name:").lower()
            acc_num=int(input("Enter the account number:"))
            for i in bank.accounts:
                if i['Holder_name']==name and i['Account_number']==acc_num:
                    print("The current balance is:",i['Balance'])
                    break
            else:
                print("Account not found.Try again")
                continue
            break
    def account_details(self):
        name=input("Enter the account holder name:").lower()
        ph_no=int(input("Enter the phone number:"))
        for i in bank.accounts:
            if i['Holder_name'].lower()==name and i['Phone_number']==ph_no :
                print(i)
                break
        else:
            print("Account not found or incorrect details")
obj=bank()
while True:
    print('''
          1.Create Account
          2.Deposit
          3.Withdraw
          4.Check Balance
          5.Account details
          6.Exit
          ''')
    choice=int(input("Enter your choice:"))
    if choice==1:
        obj.create_account()
    elif choice==2:
        obj.Deposit()
    elif choice==3:
        obj.Withdraw()
    elif choice==4:
        obj.check_balance()
    elif choice==5:
        obj.account_details()
    elif choice==6:
        print("Thank you for using the banking application.")
        break
    else:
        print("Invalid choice. Please try again.")







from datetime import datetime
def deposit():
    dep=float(input("enter the deposit amount: "))
    print("your amount has been deposited") 
    if dep<0:
        print("amount can't be negative!")
    else:
        return dep
def withdraw(dep):
    wd=float(input("enter your withdrawing amount: "))
    if wd>dep:
        print("negative balance can't withdraw")
    else:
        return wd
def balance(bal):
    print("your balance: ",bal)
def main():
    bal=0
    dep=0
    wd=0
    while True:
        print("\nbanking program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit\n")

        choice=int(input("enter your choice(1-4): "))
        if choice<5 and choice>0:
            if choice==1:
                bal=(dep-wd)
                balance(bal)
            elif choice==2:
                dep+=deposit()
                print('\nDate: ',datetime.now().strftime('%D'))
                print('Time: ',datetime.now().strftime('%I:%M:%S %p'))
            elif choice==3:
                wd+=withdraw(dep)
                print('\nDate: ',datetime.now().strftime('%m %D %Y'))
                print('Time: ',datetime.now().strftime('%I:%M:%S %p'))
            else:
                print("thank you!")
                break
        else:
            print("enter a valid number between 1 to 4")
if __name__=='__main__':
    main()
    
        

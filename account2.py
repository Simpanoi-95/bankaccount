class BankAccount:
    from datetime import datetime
  
  def __init__(self,first_name,last_name,bank,phonenumber):
        self.first_name=first_name
        self.last_name=last_name
        self.bank=bank
        self.phonenumber=phonenumber
        self.balance=0
        self.deposit=0
        self.withdrawal=0
        self.loans=0
 
 #method1   
def account_name(self):
      name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
      return name
 
 #method2   
def deposit(self,amount):
     try:
        amount+1
     except TypeError:
        print("you must enter amount in figures")
        return

    if amount <= 0:
      print("you cannot deposit zero or negative")
    else:

      time=datetime.now()
      formatted_time=time.strftime("%b,%d,%y,%H:%M:%S")
      def deposit={
           "time":"time","amount":"amount"
       }
      self .balance+=amount
      self.deposits.append(amount)
      print("Dear {} you have deposited {} to your account".format(amount ,self.account_name(),formatted_time))

  #method3    
def withdraw(self,amount):
    try:
        amount+1
     except TypeError:
        print("you must enter amount in figures")
        return

    if amount <= o:
      print("you cannot withdraw zero or negative")
    elif amount > self.balance :
       print("you dont have enough balance ")
    else:
        time=datetime.now()
      formatted_time=time.strftime("%b,%d,%y,%H:%M:%S")
      def withdraw={
           "time":"time","amount":"amount"
       }
      self.balance-=amount
      self.withdrawals.append(amount)
      print("You have withdrawn {} from your account".format(amount,self.account_name()))
 
 
 
 #method4
def get_balance(self):
    return("The balance for {} is {} ".format(self.account_name(),self.balance))
  
  #method5
def show_deposit_statement(self):
    for deposit in self.deposits:
    formatted_time=time.strf("%A,%drd,%B,%Y,%H:%M:%p")
    print("{} deposited {}".format(deposit,formatted_time))
    return

#method6
def show_withdraw_statement(self):
    for withdrawal in self.withdrawals:
    formatted_time=time.strf("%A,%drd,%B,%Y,%H:%M:%p")
    print("{} withdrawn  {}".format(withdraw,formatted_time))
    return

#method7   
def request_loan(self,amount):
    try:
        amount+1
     except TypeError:
        print("you must enter amount in figures")
        return
    if amount<=0:
      print("you cannot request a loan of that amount")
    else:
      self.loan=amount
      print("You have received a loan amount of Ksh {}:".format(amount))
      
#method8
def repay_loan(self,amount):
     try:
        amount+1
     except TypeError:
        print("you must enter amount in figures")
        return
    if amount <=0:
        print("you cannot repay with that amount")
    elif self.loan:
       print("you dont have a loan at the moment") 
    elif amount >self.loan:    
        print("You loan is {}, please enter an amount that is less or equal".format(self.loan))
    else:
        self.loan-=amount
        print("Your have repaid your loan with {},your loan balance is {}".format(amount,self.loan))

acc1=BankAccount(first_name="sheila",last_name="lesarge",bank="kcb",phonenumber="0724532326")
acc2=BankAccount(first_name="lucia",last_name="akai",bank="gt",phonenumber="0725998015")


acc1.deposit(400)
acc2.deposit(400)

acc1.withdrawal(500)
acc2.withdrawal(500)

acc1.get_balance()
acc2.get_balance()
print(acc1.get_balance())
print(acc2.get_balance())

acc1.show_deposit_statement()
acc2.show_deposit_statement()

acc1.show_withdraw_statement()
acc2.show_withdraw_statement()

acc1.request_loan(1000)
acc2.request_loan(2000)

acc1.repay_loan(100)
acc2.repay_loan(500)

print(acc1.account_name())
print(acc2.account_name())

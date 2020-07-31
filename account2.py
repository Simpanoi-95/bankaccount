class Account:
    from datetime import datetime
  
  def __init__(self,first_name,last_name,phonenumber):
        self.first_name=first_name
        self.last_name=last_name
        self.phonenumber=phonenumber
        self.balance=0
        self.deposit=[]
        self.withdrawal=[]
        self.loans=0
        self.repay_loan=0
 
 #method1   
def account_name(self):
      name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
      return name
 
 #method2   
def deposit(self,amount):
    
    if amount <= 0:
      print("you cannot deposit zero or negative")
    else:
      self .balance+=amount
      self.deposits.append(amount)
      print("Dear {} you have deposited {} to your account".format(amount ,self.account_name(),formatted_time))

  #method3    
def withdraw(self,amount):
    

    if amount <= o:
      print("you cannot withdraw zero or negative")
    elif amount > self.balance :
       print("you dont have enough balance ")
    else:  
      self.balance-=amount
      self.withdrawals.append(amount)
      print("You have withdrawn {} from your account".format(amount,self.account_name()))
 
 
 
 #method4
def get_balance(self):
    return("The balance for {} is {} ".format(self.account_name(),self.balance))

#method5
def get_formatted_time(self,time):
   return time.strftime("%A, %drd %B % Y ,%H:%M %p")



  #method6
def show_deposit_statement(self):
    for deposit in self.deposits:
    time=deposit("time")
    formatted_time=self.get_formatted_time.(time)
    amount=deposit("amount")
    statement="you have deposited {} on {}".format(amount,formatted_time))
    print(statement)

#method7
def show_withdraw_statement(self):
    for withdrawal in self.withdrawals:
    time=withdraw("time")
    formatted_time=self.get_formatted_time.(time)
    amount=withdraw("amount")
    statement="you have withdrawn {} on {}".format(amount,formatted_time))
    print(statement)
#method8
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
      
#method9
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

def loan_repayment_statement(self):
         for repayment in self.loan_repayments:
        time = repayment["time"]
        amount = repayment['amount']
        formatted_time= self.get_formatted_time(time)
        statement="You repaid {} on {}".format,formatted_time(time)
        print(statement)









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

#class inheritance         #baseclass

class BankAccount(Account):
    def __init__(self, first_name, last_name, phone_number, bank):
        self.bank = bank
        super().__init__(first_name, last_name, phone_number)


#derived class

 class MobileMoneyAccount(Account):
    def __init__(self, first_name, last_name, phone_number, service_provider):
        self.service_provider = service_provider
        super().__init__(self, first_name, last_name, phone_number)      

  def buy_airtime(self,amount):
        try:
            amount=1
        except TypeError:
            print("PLease enter the amount in figures")
            return
        if amount=self.balance
        print("You do not have enough balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time= date.now()
            airtime={
                "time"=time,
                "airtime"=amount
            }
            self.airtime.append(airtime)
            print("You have bought airtime worth {} on {}".format(amount,self.get_formatted_time(time)))    




  def pay-bill(self,amount):
        try:
            amount=1
        except TypeError:
            print("PLease enter the amount in figures")
            return
        if amount=self.balance
        print("You do not have enough balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time= date.now()
            airtime={
                "time"=time,
                "airtime"=amount
            }
            self.bill.append(bill)
            print("You have paid {} on {}".format(amount,self.get_formatted_time(time)))
     

     def send_money(self,amount):
        try:
            amount=1
        except TypeError:
            print("PLease enter the amount in figures")
            return
        if amount=self.balance
        print("You do not have enough balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time= date.now()
            airtime={
                "time"=time,
                "airtime"=amount
            }
            self.send_money.append(send_money)
            print("You have sent kshs{} on {}".format(amount,self.get_formatted_time(time)))

    def receive_money(self,amount):
        try:
            amount=1
        except TypeError:
            print("PLease enter the amount in figures")
            return
        if amount=self.balance
        print("You do not have enough balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time= date.now()
            airtime={
                "time"=time,
                "airtime"=amount
            }
            self.receive_money.append(receive_money)
            print("You have received kshs {} on {}".format(amount,self.get_formatted_time(time)))
        

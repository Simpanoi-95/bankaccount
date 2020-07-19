class BankAccount:
  
  
  def __init__(self,first_name,last_name,bank,phonenumber:0
    self.first_name=first_name
    self.last_name=last_name
    self.bank=bank
    self.phonenumber=phonenumber
    self.balance=0
    self.loan=0
    
    
 #method1   
  def account_name(self):
    name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
    return name
 
 #method2   
  def deposit(self, amount):
    self .balance+=amount
      print("You have deposited {} to your account".format(amount))
 
 #method3 
  def get_balance(self):
    return("The balance for {} is {} ".format(self.account_name(),self.balance))
  
  #method4
  def withdraw(self,amount):
      print("You have withdrawn {} from your account".format(amount))
    
      
  def giveloan(self,amount):
      print("You have received a loan amount of Ksh {}:".format(amount))
      self.balance= self.loans + amount

  def repay(self,amount):
  
          self.repay=self.loans-amount
          print("You have repayed Ksh {}".format(amount))
          print("Your loan balance is: {}".format(self.repay))

acc1=BankAccount(first_name="sheila",last_name="lesarge")

acc1=withdraw(1000)
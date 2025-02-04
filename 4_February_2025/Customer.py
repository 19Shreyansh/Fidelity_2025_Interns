'''On github'''
class customer:
    transaction=int(input("Enter the transaction amount : "))
    '''Transaction amount is taken as input.'''
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        '''Name and Balance are being sent.'''
    def deposit(self):
        '''Balance is being updater after deposit.'''
        self.balance=self.balance+self.transaction
        print("After Deposit , New Balance is : ",self.balance)
    def withdraw(self):
        '''Condition of sufficient funds is being checked.'''
        if self.transaction > self.balance:
            print("Not enough funds to withdraw")
        else:
            '''Balance is updated after withdraw.'''
            print("After Withdrawl , New Balance is : ",self.balance-self.transaction)
c=customer("FIL",100)
c.deposit()
#c.withdraw()
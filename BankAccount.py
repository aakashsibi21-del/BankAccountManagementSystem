# Create an abstract class named BankAccount. 
# ○ Include an abstract method named calculate_interest(). 
# ○ Include a method named display_balance().

from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self, Account_Balance, ):
        self.__Account_Balance = Account_Balance
        # self.Interest_Amount = Interest_Amount
 # this method will be inherite from the child class. 
    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print('Total Balance is : ',self.__Account_Balance)

    def Deposite(self,deposite):
        if deposite <= 0:
            raise 'Deposite value cannot be Zero or negative value'
        self.__Account_Balance = self.__Account_Balance + deposite
        print('Deposited Succesfully.')

    def Withdrawal(self,withdraw):
        if withdraw >= self.__Account_Balance:
            raise 'Insufficient Balance'
        elif withdraw<=0:
            raise 'Withdarawal amount cannot be negative values'
        else:
            self.__Account_Balance = self.__Account_Balance - withdraw
            print('Withdrawal Succesfully Completed.')

    @property
    def Account_Balance(self):
        return self.__Account_Balance
    
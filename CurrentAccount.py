from BankAccount import BankAccount

class CurrentAccount(BankAccount):

    def dummey(self):
        print('HE HE HE HE HE')

    
    def calculate_interest(self,interest_rate):
            if interest_rate <0:
                print('Intrest cannot be Negative')
            elif interest_rate == 0:
                print('There is no Interest')
            else:
                interest = self.Account_Balance * (interest_rate/100)
                print('Interest Amount : ',interest)

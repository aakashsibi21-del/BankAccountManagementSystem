from SimpleAccount import SimpleAccount
from BankAccount import BankAccount
from CurrentAccount import CurrentAccount
# creating object of class simple
sim = SimpleAccount()
sim.method1()

# bank = BankAccount()


#We cannot create an onject of an abstract class.
# bank.Deposite(500)

current = CurrentAccount(0)
current.dummey()
current.Deposite(5000)
# cannot be done this process because this varible is protected.
# print(f'balance amount is : {cu.__Account_Balance}')
current.display_balance()         
current.Deposite(1000)
current.display_balance()

current.Withdrawal(200)
current.display_balance()
current.calculate_interest(0)

print('\n************************************************\n')



from SavingsAccount import SavingsAccount

saving = SavingsAccount(0)

saving.display_balance()
saving.Deposite(4000)
saving.display_balance()
saving.Withdrawal(300)
saving.display_balance()
saving.calculate_interest(5)

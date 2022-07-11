class Bank:
    balance = 310

    def __init__(self, name):
        self.name = name

    def credit(self):
        credit_amt = int(input('Enter amount\t'))
        Bank.balance = Bank.balance + credit_amt

    def debit(self):
        if Bank.balance > 0:
            debit_amt = int(input('Enter amount\t'))
            if Bank.balance >= debit_amt:
                Bank.balance = Bank.balance - debit_amt
            else:
                print("Debit amount is greater then available balance")
        else:
            print("You have 0 rupees in your account")
    
    def show_balance(self):
        print(Bank.balance)
    

obj = Bank('Musab')
while True:
    op = input('Select 1 for credit Select 2 for balance enquiry Select 3 for debit Select 4 to quite\n')
    if op == '1':
        obj.credit()
    elif op == '2':
        obj.show_balance()
    elif op == '3':
        obj.debit()
    elif op == '4':
        break

class bank():
    branch='marathahalli'
    IFSC='sbi0000s'
    def __init__(self,name,accountno,mob,bal,pin):
        self.name=name
        self.accountno=accountno
        self.mob=mob
        self.bal=bal
        self.pin=pin
    def details(self):
        print(self.name)
        print(self.accountno)
        print(self.mob)
        print(self.bal)
        print(self.pin)
    def withdraw(self):
        if self.checkpin()==self.pin:
            amount=int(input('enter the amount:'))
            if 0<amount<20000:
                if amount<=self.bal:
                    self.bal-=amount
                    print('amount debited successfully')
                    print(f'remaing balance {self.bal}')
                else:
                    print('insufficent balance')
            else:
                print('that much amount not taken')
        else:
            print('pin is invalid')
    def bal(self):
        print(f'vailable in your balance:{self.bal}')
    def deposite(self):
        if self.checkpin()==self.pin:
            amount=int(input('enter the amount'))
            if 100<amount<=50000:
                self.bal+=amount
                print(f'amount succesfully credited={self.bal}')
            else:
                print('be your the limits')
        else:
            print('invalid pin')
    @staticmethod
    def checkpin():
        password=int(input('enter the values:'))
        return password
    @classmethod
    def changebranch(cls):
        cls.branch='palamaner'
cust1=bank('hareesh',1111111111,1234567891,2000,1122)
cust2=bank('suresh',2222222222,1234567892,30000,1133)
cust3=bank('hari',3333333333,1234567893,40000,1144)
cust1.details()
cust2.details()
cust3.details()
bank.withdraw(cust1)
bank.bal(cust1)
cust1.deposite()
cust2.deposite()
cust1.changebranch()
print(cust1.branch)


from Accountinfo import Accountinfo

class BankAccount(Accountinfo):

    def __init__(self,name,accountnumber,balance,addbalance):
        super().__init__(name= name, accountnumber= accountnumber,balance= balance)
        self.__addbalance = addbalance

    def getaddbalanceammount(self):
        balance = self.getbalance()
        return self.__addbalance+balance

    def __str__(self):
        return "Name : {}\nAccount Number : {}\nTotal Balance : {}".format(self.getname(),self.accountnumber,self.getbalance())
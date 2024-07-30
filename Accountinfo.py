from Account import Account

class Accountinfo(Account):
    __balance = 0.0
    __name = ''
    __accountnumber = ''

    def __init__(self,name,accountnumber,balance):
        self.__name = name
        self.accountnumber = accountnumber
        self.__balance = balance

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name = name

    def getaccountnumber(self):
        return self.accountnumber

    def setaccountnumber(self,accountnumber):
        self.accountnumber = accountnumber

    def getbalance(self):
        return self.__balance

    def setbalance(self,balance):
        self.__balance = balance






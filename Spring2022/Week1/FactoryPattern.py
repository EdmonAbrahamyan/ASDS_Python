from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def create_account(self):
        pass


class PersonalAccount(BankAccount):
    def create_account(self):
        print('Personal Account')


class BusinessAccount(BankAccount):
    def create_account(self):
        print('Business Account')


class BankAccountFactory:
    accounts = {
        'personal': PersonalAccount,
        'business': BusinessAccount
    }

    @staticmethod
    def build(account):
        return BankAccountFactory.accounts[account]()


class Client:

    @staticmethod
    def create_account(account):
        factory = BankAccountFactory().build(account)

        return factory.create_account()


client = Client()
client.create_account('personal')


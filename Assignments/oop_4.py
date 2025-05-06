#  Create a class Bank with a class variable bank_name.
#  Add a class method change_bank_name(cls, name) that allows changing the bank name.
#  Show that it affects all instances.

class Bank:
    bank_name = "National Bank"
    
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

customer1 = Bank
customer2 = Bank
print("Before Change")
print("Customer1:", customer1.bank_name)
print("Customer2:", customer2.bank_name)

Bank.change_bank_name("International Bank")
print("\nAfter Change")
print("Customer1:", customer1.bank_name)
print("Customer2:", customer2.bank_name)

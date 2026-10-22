class Payment:
    def pay(self, amount):
        print("Making payment")
class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")
class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")
class CashPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Cash")
p1 = CreditCardPayment()
p1.pay(1000)
p2 = UPIPayment()
p2.pay(500)
p3 = CashPayment()
p3.pay(200)


class Employee:
    def __init__(self, fname, lname, salary, super, paymentS, paymentL):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.super = super
        self.paymentS = paymentS
        self.paymentL = paymentL

    def fullname(self):
        print(f"Name: {self.fname} {self.lname}")
    
    def payperiod(self):
        print(f"Pay Period: {self.paymentS} - {self.paymentL}")

    def grossincome(self):
        income = int(self.salary)
        x = income / 12
        print(f"Gross Income: {round(x)}")
        return x

    def incometax(self):
        i = int(self.salary)
        if i <= 18200:
            i = 0
            print(f'Income Tax: {round(i)}') 
        elif i >= 18201 and i <= 37000:
            i = ((i - 18200) * 0.19)/12
            print(f'Income Tax: {round(i)}') 
        elif i >= 37001 and i <= 87000:
            i = (3572 + (i - 37000) * 0.325)/12
            print(f'Income Tax: {round(i)}') 
        elif i >= 87001 and i <= 180000:
            i = (19822 + (i - 87000) * 0.37)/12
            print(f'Income Tax: {round(i)}') 
        elif i >= 180001:
            i = (54232 + (i - 180000) * 0.45)/12
            print(f'Income Tax: {round(i)}') 
        return round(i)


    def netincome(self, grossincome, tax):
        x = (grossincome - tax)
        print(f"Net Income: {round(x)}")

    def superrate(self, grossincome):
        y = int(self.super) / 100
        x = (grossincome * y)
        print(f"Super: {round(x)}")
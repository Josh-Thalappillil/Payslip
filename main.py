# Generate a payslip from input values
# Print Welcome to payslip generator
# Get the inputs from user
# Methods to generate desired outputs

print("Welcome to the payslip generator")

print("Please input your name: ")
fname = input() 

print("Please input your surname: ")
lname = input()

print("Please enter your annual salary: ")
salary = input()

print("Please enter your super rate: ")
super = input()

print("Please enter your payment start date: ")
paystart = input()


print("Please enter your payment end date: ")
payend = input()

print("Your payslip has been generated:")


def fullname(fname, lname):
    print(f"Name: {fname} {lname}")


def payperiod(paystart, payend):
    print(f"Pay Period: {paystart} - {payend}")

def grossincome(salary):
    income = int(salary)
    x = income / 12
    print(f"Gross Income: {round(x)}")
    return x

def incometax(salary):
        i = int(salary)
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


def netincome(gincome, tax):
    x = (gincome - tax)
    print(f"Net Income: {round(x)}")

def superrate(gincome, super):
    y = int(super) / 100
    x = (gincome * y)
    print(f"Super: {round(x)}")



fullname(fname, lname)
payperiod(paystart, payend)
gross = grossincome(salary)
income = incometax(salary)
netincome(gross, income)
superrate(gross, super)

     



# method to join fname input and lname input 

# method for pay period join start and end date inputs

# method calulate gross income from annual salary /12months

# method calculate net income gross income - income tax

# method calculate super by gross income multiplied by super rate

# Round all calculations to the whole dollar, round up if 50c or greater
 


# Generate a payslip from input values
# Print Welcome to payslip generator
# Get the inputs from user
# Methods to generate desired outputs
from employee import Employee
from dialog import Dialogue

Dialogue.getwelcomemsg()
fname = Dialogue.getfname()
lname = Dialogue.getlname()
salary = Dialogue.getsalary()
super = Dialogue.getsuper()
paymentS = Dialogue.getpaymentS()
paymentL = Dialogue.getpaymentL()
Dialogue.getendmsg()

josh = Employee(fname, lname, salary, super, paymentS, paymentL)
josh.fullname()
josh.payperiod()
gross = josh.grossincome()
tax = josh.incometax()
josh.netincome(gross, tax)
josh.superrate(gross)
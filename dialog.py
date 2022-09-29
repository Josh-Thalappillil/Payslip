class Dialogue:
    def getwelcomemsg():
        print("Welcome to the payslip generator")
    
    def getfname():
        print("Please input your name: ")
        fname = input() 
        return fname

    def getlname():
        print("Please input your surname: ")
        lname = input()
        return lname
    
    def getsalary():
        print("Please enter your annual salary: ")
        salary = input()
        return salary
    
    def getsuper():
        print("Please enter your super rate: ")
        super = input()
        return super

    def getpaymentS():    
        print("Please enter your payment start date: ")
        paymentS = input()
        return paymentS

    def getpaymentL():
        print("Please enter your payment end date: ")
        paymentL = input()
        return paymentL
    def getendmsg():
        print("Your payslip has been generated:")
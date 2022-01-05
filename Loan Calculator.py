loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

def fn ():
    
    p = float(input('Enter the loan principal:'))
    a = float(input('Enter the monthly payment:'))
    i = float(input('Enter the loan interest:'))
    
    i = i / (12 * 100)
    n = math.ceil(math.log((a/(a-i*p)),(1+i)))
    years = math.floor(n / 12)
    months = n - years * 12
    
    if years == 0:
        if months == 1:
            print("It will take ",months," month!") 
        else:
            print("It will take ", months, " months!")            
    elif months == 0:
        if years == 1:
            print("It will take " ,years, " year!")
        else:    
            print("It will take " ,years, " years!")        
    if years == 1 and months !=0:
        if months == 1:
            print("It will take " ,years, " year and " , months, " month to repay this loan!")
        else:
            print("It will take " ,years, " year and " , months, " months to repay this loan!")   
    if  years != 1 and months == 1:     
        print("It will take " ,years, " years and " , months, " month to repay this loan!")    
    if years != 1 and months != 1 and years != 0 and months != 0: 
        print("It will take " ,years, " years and " , months, " months to repay this loan!")
             
def fa ():
    p = float(input('Enter the loan principal:'))
    n  = float(input('Enter the number of periods:'))
    i = float(input('Enter the loan interest:'))
    
    i = i / (12 * 100)
    a = p * ((i* math.pow((1 + i),n)) / (math.pow((1 + i),n) - 1))
    
    print(f'Your monthly payment = {math.ceil(a)}!')
 
def fp ():

    a = float(input('Enter the annuity payment:'))
    n  = float(input('Enter the number of periods:'))
    ins = float(input('Enter the loan interest:'))
    
    i = ins / (12 * 100)
    ins = a / ((i * math.pow((1 + i),n)) / (math.pow((1 + i),n) - 1))
    
    print(f'Your loan principal = {round(ins)}!')

# write your code here
import math  

answer = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")

if answer == 'n':
    fn()
elif answer == 'a':
    fa()  
elif answer == 'p':    
    fp()
    



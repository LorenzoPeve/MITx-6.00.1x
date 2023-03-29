def remBalance(balance,  annualInterestRate, monthlyPaymentRate):

    mon_rate = annualInterestRate / 12
    for i in range(1,12+1):
        balance -= balance * monthlyPaymentRate
        balance = balance + mon_rate*balance
       
        print('Month ', i, ' Remaining balance: ' , round(balance,2))

    return round(balance,2)


def remBalanceFixed2(balance,  annualInterestRate, monthlyPayment, months):
    mon_rate = annualInterestRate / 12
    for i in range(1,months+1):
        balance -= monthlyPayment
        balance = balance + mon_rate*balance
        print('Month ', i, ' Remaining balance: ' , round(balance,2))
    return round(balance,2)

def fixedAmount_m10(balance, annualInterestRate, months = 12):
    payment = 0
    remBal = 100
    while remBal >= 0: 
        payment += 10
        remBal = remBalanceFixed2(balance, annualInterestRate, payment, months)

    print('Lowest Payment:',payment)




def remBalanceFixed(balance,  annualInterestRate, monthlyPayment):
    mon_rate = annualInterestRate / 12
    for i in range(1,12+1):
        balance -= monthlyPayment
        balance = balance + mon_rate*balance
        
    return round(balance,2)

def fixedAmount(balance, annualInterestRate,):
    mon_rate = annualInterestRate / 12
    low = balance /12 
    upper = (balance * (1 + mon_rate)**12) / 12.0
    midpoint = (low + upper) / 2
    remBal = 100
    count = 0
    while remBal != 0.00: 
        remBal = remBalanceFixed(balance, annualInterestRate, midpoint)
        
        # You are paying less than you should
        if remBal > 0:
            low = midpoint
            midpoint = (low + upper) / 2
        if remBal < 0:
            upper = midpoint
            midpoint = (low + upper) / 2

        
    print('Lowest Payment:',round(midpoint,2))

fixedAmount(320000, 0.2)
fixedAmount(999999, 0.18)
    

nums = [1,2,3,4]

def square(a_list):
    for i in range(len(a_list)):
        a_list[i] = a_list[i]**2

    return

def square2(a_list):
    return [item**2 for item in a_list]

print(nums)
square(nums)
print(nums)

nums = [1,2,3,4]
print(nums)
print(square2(nums))
print(nums)
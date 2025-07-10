bill_total = 205
discount1 = 10
discount2 = 30

if bill_total > 100 and bill_total <= 200:
    print('Bill is greater than $100')
    bill_total = bill_total - discount1
elif bill_total > 200:
    bill_total = bill_total - discount2
    print('you get a discount of $30 because your bill is greater than $200')
else:
    print('Bill is less than $100, no discount applied')

print ('Your total bill is $', bill_total)


a = isinstance(str, "aa")

print(a)  


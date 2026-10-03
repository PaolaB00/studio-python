hrs = input("Enter Hours: ")
rate = input('Enter Rate: ')
try:
    h = float(hrs) 
    r = float(rate)
except:
    h = -1
    r = 1

ival = h*r

if ival>0:
    
    print('OK')
else:
    print('Error: Insert a number')
    quit()

if h<=40:
    pay = h*r
else:
    extra_h = h - 40
    pay = 40 *r + extra_h*1.5*r

print(pay)
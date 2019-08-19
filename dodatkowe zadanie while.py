number = 20730906
tmpnumber = number
sumOfDigits = 0
while tmpnumber > 0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is', sumOfDigits)

'''
        1. Enter the date of birth
        2. find the length of the string
        3. iterate and add the digits. If sum is greater than or equal to 10, then break up and add (N-10)
        4. Print the lucky number
'''

dob = input('Enter your date of birth in any format(numbers only). Seperate date, month and year of birth by some non-numerical seperator: ')
len = len(dob)
sum = 0
for i in range(len) :
    if dob[i].isdigit() :
        sum = sum + int(dob[i])
        if sum >= 10 :
            num = sum - 10
            sum = num + 1
print('Your lucky number is ', sum)
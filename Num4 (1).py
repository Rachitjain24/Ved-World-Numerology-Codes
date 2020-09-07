'''
        1. Enter the date of birth
        2. find the length of the string
        3. iterate and add the digits. If sum is greater than or equal to 10, then break up and add (N-10)
        4. Print the lucky number
'''
def dict_filler(dob) :
    length = len(dob)
    dob_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for i in range(length) :
        if (dob[i].isdigit()) and (dob[i] != '0'):
            dob_dict[dob[i]] = dob_dict[dob[i]] + 1 
    return dob_dict


dob = input('Enter your date of birth in DD:MM:YYYY format ONLY. Seperate date, month and year of birth by some non-numerical seperator: ')
dob_dict = dict_filler(dob) 
present = list()
absent = list()
driverno = str(int(dob[0]) + int(dob[1]))
for key, value in dob_dict.items() :
    if value == 0 :
        absent.append(key)
    else :
        present.append(key)

print("List of numbers not present in your date of birth is given below: ")
for i in absent :
    print(i, end = ', ')

print("\n\nList of numbers present in your date of birth with their significance is given below: ")
for i in present :
    if i == '1': print(i + ': Power')
    if i == '2': print(i + ': Mind/Peace')
    if i == '3': print(i + ': Health/Family')
    if i == '4': print(i + ': Wealth/Income')
    if i == '5': print(i + ': Energy/Communication')
    if i == '6': print(i + ': Friends/Pleasure')
    if i == '7': print(i + ': Fertility/Kids')
    if i == '8': print(i + ': Education/Knowledge')
    if i == '9': print(i + ': Fame/Success')

print('Your driver number is ', driverno, end = '')
'Hello RACHIT BHOSDIWALAY!!! ADD WHATEVER YO WANT TO ADD HERE!!!!!'
if driverno== '1': print(': Power')
if driverno== '2': print(': Mind/Peace')
if driverno== '3': print(': Health/Family')
if driverno== '4': print(': Wealth/Income')
if driverno== '5': print(': Energy/Communication')
if driverno== '6': print(': Friends/Pleasure')
if driverno== '7': print(': Fertility/Kids')
if driverno== '8': print(': Education/Knowledge')
if driverno== '9': print(': Fame/Success')

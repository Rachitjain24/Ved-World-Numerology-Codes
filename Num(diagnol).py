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
if driverno== '1': print(': Sun/Suraj')
if driverno== '2': print(': Moon/Chandrama')
if driverno== '3': print(': Guru/Jupiter')
if driverno== '4': print(': Rahu/Dragon head')
if driverno== '5': print(': Budh/Mercury')
if driverno== '6': print(': Shukra/Venus')
if driverno== '7': print(': Ketu/Dragon tail')
if driverno== '8': print(': Shani/Saturn')
if driverno== '9': print(': Mangal/Mars')

value = dob_dict[driverno]
if value == 0 :
    present.append(driverno)
else :
    present.append(driverno)
present.sort()

diagonal = 0
row = 0
if ('4' in present) and ('9' in present) and ('2' in present) : row = row + 1
if ('3' in present) and ('5' in present) and ('7' in present) : row = row + 1
if ('8' in present) and ('1' in present) and ('6' in present) : row = row + 1
if ('4' in present) and ('5' in present) and ('6' in present) : diagonal = diagonal + 1
if ('8' in present) and ('5' in present) and ('2' in present) : diagonal = diagonal + 1

print("Luck by row = ", end = '')
if diagonal == 2 : print("75%")
elif diagonal == 1 and row == 0 : print("60%")
elif diagonal == 1 and row == 1 : print("50%")
elif row == 2 : print("25%")
elif diagonal == 0 and row == 0 : print("0%")


column= 0
if ('4' in present) and ('3' in present) and ('8' in present) : column= column + 1
if ('9' in present) and ('5' in present) and ('1' in present) : column= column + 1
if ('2' in present) and ('7' in present) and ('6' in present) : column= column + 1
print("Luck by column = ", end = '')
if diagonal == 2 : print("75%")
elif diagonal == 1 and column == 0 : print("60%")
elif diagonal == 1 and column == 1 : print("50%")
elif column == 2 : print("25%")
elif diagonal == 0 and column == 0 : print("0%")
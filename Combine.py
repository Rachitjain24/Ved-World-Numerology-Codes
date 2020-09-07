'''
        1. Enter the alpha-numeric string
        2. find the length of the string
        3. iterate, if letter convert to lower case and obtain the corresponding digit and add the stringofied digit and add the digits. If sum is greater than or equal to 10, then break up and add (N-10)
        4. Print the lucky number
'''
def lnum_generator(string) :
    length = len(string)
    sum = 0
    for i in range(length) :
        if string[i].isdigit() :
            sum = sum + int(string[i])
            if sum >= 10 :
                num = sum - 10
                sum = num + 1
    return sum

def from_name(string) :
    mapping = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 
               'j' : 1, 'k' : 2, 'l' : 3, 'm' : 4, 'n' : 5, 'o' : 6, 'p' : 7, 'q' : 8, 'r' : 9, 
               's' : 1, 't' : 2, 'u' : 3, 'v' : 4, 'w' : 5, 'x' : 6, 'y' : 7, 'z' : 8}
    if not string.isalnum() :
        if string.find(' ') == -1 :
            print('Non alphanumeric character detected!!')
            quit()
    string = string.lower()
    length = len(string)
    string2 = str()
    for i in range(length) :
        if string[i].isalpha() :
            string2 = string2 + str(mapping.get(string[i]))
        else :
            string2 = string2 + str(string[i])
    return lnum_generator(string2)

dob = input('Enter your date of birth in any format(numbers only). Seperate date, month and year of birth by some non-numerical seperator: ')
num_dob = lnum_generator(dob)
string = input('Enter an alphanumeric string: ')
num_name = from_name(string)
print('The lucky number generated from your date of birth is ' + str(num_dob) + '. \nThe lucky number generated from the string you entered is ' + str(num_name) + '.')
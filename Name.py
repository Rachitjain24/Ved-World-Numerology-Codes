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
    print('Your lucky number is ', sum)

string1 = input('Enter an alphanumeric string: ')
mapping = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 
           'j' : 1, 'k' : 2, 'l' : 3, 'm' : 4, 'n' : 5, 'o' : 6, 'p' : 7, 'q' : 8, 'r' : 9, 
           's' : 1, 't' : 2, 'u' : 3, 'v' : 4, 'w' : 5, 'x' : 6, 'y' : 7, 'z' : 8}
if not string1.isalnum() :
    print('Non alphanumeric character detected!!')
    quit()
string1 = string1.lower()
length = len(string1)
string2 = str()
for i in range(length) :
    if string1[i].isalpha() :
        string2 = string2 + str(mapping.get(string1[i]))
    else :
        string2 = string2 + str(string1[i])
lnum_generator(string2)
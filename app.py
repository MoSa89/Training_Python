#print('Mo Sadeghi')
#print('o----')
#print(' ||||')
#print('*' * 10)
#price = 10
#price = 4.5
#name = 'Mo'
#is_published = False
#print(price)
#name = input('Please enter your name ')
#color = input('your favorite color is ')
# print('yur name is  ' + name + 'Your favorite color is ' + color)

#birth_year = int(input('What is your birthday? '))
#age = 2023 - birth_year
#print(age)
#print(type(age))

#Name = input('What is your name? ')
#Weight_KG = input('What is  your weight in kilogram? ')
#Weight_G = int(Weight_KG) * 1000
#print('Weight of ' + Name + ' in Gram is ' + str(Weight_G))

#course = "Python's course for beginners"
#print(course)

#course = '"Pythons course for beginners"'
#print(course)

#course = '''
#Hi,
#'
#It is my first try to learning the python
#I am going to keep the learning
#to be a professional Python programmer

#'''
#print(course)

#course = ('Hello world')
#print(course[0:3])
#print(course[2:])
#print(course[:5])
#print(course[1:-1])

#first = 'Mo'
#last = 'Sa'

#message = first + ' [' + last + '] ' + 'is a coder'
#print(message)

#msg = f'{first} [{last}] is a coder'
#print(msg)

#course = 'Pythone for you'
#print(len(course))
#print(course.upper())
#print(course.lower())
#print(course.find('f'))
#print(course.replace('Python','Jython'))
#print('p' in course)

#print(10 // 4)
#x = 10
#x +=4
#print(x)
#x = 10 + 3 * 2 ** 2
#print(x)


#x = 2.9

#print(round(x))
#print(abs(-2.9))

#import math
#print(math.ceil(2.9))
#print(math.floor(2.9))

#is_hot = False
#is_cold = False
#if is_hot:
#    print("it's a hot day")
#elif is_cold:
#    print("it's cold")
#else:
#    print("It's a moderate day")

#print("enjoy your day")

#price = 1000000
#ans = input("Do you have a good credit? Y/N   ")
#AnswerY = 'Y' is ans
#AnswerN = 'N' is ans
#    print("You should put down " + str(20*price/100))
#elif AnswerN:
#    print("You should put down " + str(10*price/100))
#else:
#    print('you entered wrong answer')
#print(type(AnswerY))

#has_good_credit = True
#has_high_income = True
#if has_good_credit and not has_high_income:
#    print("eligible for loan")
#else:
#    print("not eligible for loan")

#temp = int(input("Temperature?  "))
#if temp > 30:
#    print("it's a hot day")
#elif temp < 10:
#    print("it's a cold day")
#elif not temp < 10 and not temp > 30:
#    print("it's neither hot nor cold")
#print("have a good day")

#name = input("Enter Your Name? ")
#Name_Len = len(name)
#if Name_Len < 3:
#    print("Name should be more long")
#elif Name_Len > 50:
#    print("name can be maximum 50 characters")
#else:
#    print("name looks good!")
#weight = int(input("Please let me know your weight"))
#unit = input("unit is in Kilo(K) or lb(L)?")
#if unit.upper() == 'K':
#    print(f'"your weight is " {weight}  {unit} and {weight * 0.45} lb ')
#elif unit.upper() == 'L':
#    print(f'"your weight is " {weight}  {unit} and {weight / 2} KG ')
#else:
#    print("You entered wrong units")
#i = 1
#while i <= 5:
#    print('*' * i)
#    i +=1
#print("Done")

#secret_number = 9
#guess_count = 1
#Guess_limit = 3
#while guess_count <= Guess_limit:
#    Guess = int(input("Guess = "))
#   guess_count +=1
#    if Guess == secret_number:
#        print("Guess was '9'")
#        break
#else:
#    print("you failed")
#command = ""
#start_count = 0
#stop_count = 0
#while True:
#    command = input(">").lower()
#    if command == "help":
#        print('''
#start   - to start the car
#stop    - to stop the car
#quit    - to exit
#''')
#    elif command == "start":
#        if start_count == 0:
 #           print("Car started...Ready to go")
  #      else:
   #         print("Car started already")
    #    start_count += 1
#    elif command == "stop":
#        if stop_count == 0:
 #           print("Car stopped")
  #      else:
#            print("Car stopped already")
#        stop_count += 1
#    elif command == "quit":
#        print("QUIT!")
#        break
#    else:
#        print("I don't understand that")
#        break

#for item in 'python':
#    print(item)

#for item in [1, 2, 3, 4]:
#    print(item)

#for item in range(5, 10, 2):
#    print(item)

#prices = [10, 20, 30]
#total = 0
#for price in prices:
#    total += price
#print(f"total price's equal to {total}")

#for x in range(4):
#    for y in range(3):
#        print(f'({x},{y})')

#numbers = [5, 2, 5, 2, 2]

#for number in numbers:
#    star = ''
#    for counter in range(number):
#        star += '*'
#    print(star)

#names = ['mo', 'aa', ]
#print(names[1])

#numbers = [3, 62, 8,4,10]
#max = numbers[0]
#for item in numbers:
#    print(item)
#    if max < item:
#        max = item
#print(max)


#matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]
#
#matrix[0][1] = 20
#print(matrix[0][1])

 #matrix = [
 #   [1, 2, 3],
 #   [4, 5, 6],
 #   [7, 8, 9]
#]
#
#for x in matrix:
#    for item in x:
#        print(item)

#course = "Python vor beginners"
#Status = 'P' in course
# print(Status)

#numbers = [1, 2, 3, 4, 4, 5, 5 ]
#numbers2 = numbers.copy()
#numbers.sort()
#numbers.reverse()
#print(numbers2)



#mylist = [1, 3, 6,9,10,6,45646,7,3,6,98,4,4,5 ,3,2,7,4,23,345,67,4,6,8,9]

#for item in mylist:
#    reap = mylist.count(item)
#    if reap > 1:
#        while reap > 1:
#            mylist.remove(item)
#            reap -= 1
#mylist.sort()
#print(mylist)

#import socket
#s = socket.socket()
#print('Socket succesfully created')
#port = 5678
#s.bind(('', port))
#print(f'socket binded to port{port}')
#s.listen(5)
#print('Socket is listening')
#while True:
#    c, addr = s.accept()
#    print('Got connection from', addr)
#    message = ('Thank you for connecting')
#    c.send(message.encode())
#    c.close()



#numbers = [2, 2, 4, 6, 3, 4, 6, 1]

#uniques = []
#for item in numbers:
#    if item not in uniques:
#        uniques.append(item)
#
#uniques.sort()
#print(uniques)

#numbers = (1, 2, 3,)
#numbers[0] = 10
#print(numbers[0])

"""
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)
"""
"""
coordinates = [1, 2, 3]
x, y, z = coordinates
print(x)
"""

""" 
Customer = {
    "name" : "John Smith",
    "age" : 32,
    "is_verified" : True

}

Customer["name"] = "Jack Smith"
Customer["Birthdate"] = "1980"
print(Customer.get("birthdate","Nothing"))

"""
"""
Numbers = {
    "1": "one",
    "2":"two",
    "3":"three",
    "4":"four",
}


Number = input("Please Enter the Phone Number ")
Phone = ""
for item in Number:
    Phone += Numbers.get(item, "!") + " "
print(Phone)

"""
"""
message = input("> ")
words = message.split(' ')
Emojis = {
    ":)":   "😊",
    ":(":   "🙁"
}
output = ""
for word in words:
    output += Emojis.get(word, word) + ' '
print(output)
"""

"""
def great_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')


print("Start")
great_user(last_name = "Smith",  first_name = "John")
print("Finish")
"""

"""def square(number):
    return number * number


print(square(3))"""


"""
def square(number):
    print(number * number)


print(square(3))"""


"""
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "🙁"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input(">")
print(emoji_converter(message))
"""

"""

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid Value') 
"""
print("sfsdfsd")

print("sa")
print("aaaaa")

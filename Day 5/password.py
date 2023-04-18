#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = 1 + int(input("How many letters would you like in your password?\n"))
nr_symbols = 1 + int(input(f"How many symbols would you like?\n"))
nr_numbers = 1 + int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ''
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for num in range(1, nr_letters):
    password += random.choice(letters)

for num in range(1, nr_symbols):
    password += random.choice(symbols)

for num in range(1, nr_numbers):
    password += random.choice(numbers)

print(f"Base: {password}")

password = ''.join(random.sample(password, len(password)))

print(f"Scrambled: {password}")


def turn_right():
    turn_left()
    turn_left()
    turn_left()


num = 0
while at_goal() == False:
    if wall_on_right() == True and front_is_clear() == True:
        move()
    elif wall_on_right() == True and front_is_clear() == False:
        turn_left()
    elif right_is_clear() == True:
        turn_right()
        move()
        num += 1
        if num >= 4:
            move()
            num = 0
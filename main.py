#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
import random
nr_letters_int = int(nr_letters)
nr_symbols_int = int(nr_symbols)
nr_numbers_int = int(nr_numbers)
random_letter = ''.join(random.sample(letters,nr_letters_int))
random_symbol = ''.join(random.sample(symbols,nr_symbols_int))
random_number = ''.join(random.sample(numbers,nr_numbers_int))
#print(random_letter+random_symbol+random_number)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
nr_letters_int1 = int(nr_letters)
nr_symbols_int1 = int(nr_symbols)
nr_numbers_int1 = int(nr_numbers)
random_letter1 = random.sample(letters,nr_letters_int1)
random_symbol1 = random.sample(symbols,nr_symbols_int1)
random_number1 = random.sample(numbers,nr_numbers_int1)
random_list = random_letter1+random_symbol1+random_number1
random_list_shuffle = random.sample(random_list, len(random_list))
print(''.join(random_list_shuffle))

password = ''

for items in range(1, nr_letters_int1 + 1):
  password += random.choice(letters)

for items in range(1, nr_symbols_int1 + 1):
  password += random.choice(symbols)

for items in range(1, nr_numbers_int + 1):
  password += random.choice(numbers)

#print(password)

password_list = []

for items in range(1, nr_letters_int1 + 1):
  password_list.append(random.choice(letters))

for items in range(1, nr_symbols_int1 + 1):
  password_list.append(random.choice(symbols))

for items in range(1, nr_numbers_int + 1):
  password_list.append(random.choice(numbers))

password_shuffle = random.sample(password_list, len(password_list))
#print(password_list)
print(''.join(password_shuffle))

# random.shuffle(password_list)
# print(''.join(password_list))


  

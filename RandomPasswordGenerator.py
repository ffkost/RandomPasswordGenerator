import random

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

signs = ['(', ')', '*', '&', '#', '@', '%', '$', '!', '?']

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_pw = []

mali_bukvi = int(input("Enter the number of lowercase letters you want in the password: "))
golemi_bukvi = int(input("Enter the number of uppercase letters you want in the password: "))
znaci = int(input("Enter the number of symbols you want in the password: "))

for i in range(mali_bukvi):
    lista_pw.append(lowercase_letters[random.randint(0, len(lowercase_letters) - 1)])

for i in range(golemi_bukvi):
    lista_pw.append(uppercase_letters[random.randint(0, len(uppercase_letters) - 1)])

for i in range(znaci):
    lista_pw.append(signs[random.randint(0, len(signs) - 1)])

#print(lista_pw) #

random.shuffle(lista_pw)
#print(lista_pw) #1

# password_text = ""
# for i in lista_pw:
#     password_text = password_text + i  # vtor nacin 2

#print(password_text)

password_text = "".join(lista_pw)
print(password_text)


#  lista_pw.append(random.choice(mali_bukvi))
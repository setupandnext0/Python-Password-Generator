import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./*-_!'

passwordNumber = input('Kaç tane şifre grubu oluşturulacak? :\t')
passwordNumber = int(passwordNumber)

passwordLength = input('Şifrenizin uzunluğu :\t')
passwordLength = int(passwordLength)

for c in range(passwordNumber):
    password = ''

    for p in range(passwordLength):
        password += random.choice(characters)
        print(password)


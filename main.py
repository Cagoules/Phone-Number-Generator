import random

import phonenumbers
from phonenumbers import carrier


def gen_validate_num():
    start = 0
    number_of_num = int(input("Combien de numéros voulez-vous ? "))
    file = open(f'{number_of_num} numero.txt', 'a')
    while start != number_of_num:
    #Génère un numéro français aléatoire (06 ou 07)
        numlist = []
        numlist.append('+33')
        numlist.append(random.randint(6, 7))
        for i in range(1, 9):
            numlist.append(random.randint(0, 9))
        strings = [str(integer) for integer in numlist]
        num_string = "".join(strings)
        numero = str(num_string)
        my_number = phonenumbers.parse(numero)
        #Vérifie si le numéro est valide (attention, les numéros peuvent être valide mais non attribués)
        if phonenumbers.is_valid_number(my_number) == True:
            print(numero)
            print(phonenumbers.is_valid_number(my_number))
            print(carrier.name_for_number(my_number, "fr"))
            file.write(f'{numero}\n')
        start += 1


gen_validate_num()



    


















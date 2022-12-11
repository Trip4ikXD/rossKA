

bilet = int(input('Введите количество билетов ')) # Пункт 1
vozrast = int(input('Введите свой возраст '))
a = 0
b = 990
c = 1390
if vozrast < 18 :
    print("Вам беслпатный билет")
elif  18 <= vozrast <= 25:
    print("Ваш билет стоит", b, "рублей ")
else:
    print("Ваш билет стоит", c, "рублей.") # Пункт 2 закочен.
    #Начинается пункт 3.
if bilet > 3 and 18 <= vozrast <= 25:
    summa = (bilet * b)*0.9
    print('Ваш/ваши билет(ы) стоит',summa)
elif bilet > 3 and vozrast > 25:
    summa = (bilet * c) * 0.9
    print('Ваш/ваши билет(ы) стоит',summa)
else:
    summa = 0
    print("Ваш/ваши билет(ы) стоит ", summa)










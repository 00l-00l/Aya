print ("Привет я Ая")

time = int(input("Сколько у вас сейчас времени ?"))

if 6 <= time <= 11:
    print("Доброе утро")

elif 12 <= time <= 17:
    print("добрый день")

elif 18 <= time  <= 22:
    print("добрый вечер")

else: 
    print("Ты не спишь?")

name=input("Как я к вам могу обращаться ?")

print (f"Запомнила {name}. Чем могу помочь?")

command = input("Введите команду:")


while command != "выход":
     print("Я тебя слышу")
     command = input("Введите команду:")

print("До свидания")
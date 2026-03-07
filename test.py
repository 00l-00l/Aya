age = int(input("Сколько тебе лет? "))

if age < 18:
    print("Ты несовершеннолетний")
elif age < 65:
    print("Ты взрослый")
else:
    print("Ты пенсионер")
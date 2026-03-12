import os

def show_task():
    with open("tasks.txt", "r", encoding="utf-8") as file1:
        for index, line in enumerate(file1, 1):
            print(index, line.strip())

def add_task():
    with open("tasks.txt", "a", encoding="utf-8") as file:
        task = input("Введите задачу: ")
        file.write(task + "\n")
        print(f"Записала {task}")

def del_task():
    with open("tasks.txt", "r", encoding="utf-8") as file1:
        tasks = file1.readlines()
    for index, line in enumerate(tasks, 1):
        print(index, line.strip())
    number = int(input("Какую задачу удалить? "))
    del tasks[number - 1]
    with open("tasks.txt", "w", encoding="utf-8") as file2:
        file2.writelines(tasks)

if os.path.exists("memory.txt"):
    with open("memory.txt", "r", encoding="utf-8") as file:
        name = file.read()
    print(f"С возвращением, {name}!")
else:
    name = input("Как вас зовут? ")
    with open("memory.txt", "w", encoding="utf-8") as file:
        file.write(name)
    print(f"Приятно познакомиться, {name}!")

print("Я — АЯ. Готова к работе.")

answer = input("Какое время суток сейчас у вас? ").lower()
if answer == "утро":
    print(f"Доброе утро, {name}! Пора кодить.")
elif answer == "день":
    print(f"Добрый день, {name}! Как успехи?")
else:
    print(f"Добрый вечер, {name}! Подводим итоги дня.")

while True:
    list = input("Что хотите сделать? ").lower()
    if list == "добавить":
        add_task()
    elif list == "список":
        show_task()
    elif list == "удалить":
        del_task()
    elif list == "выход":
        print("До свидания!")
        break
       

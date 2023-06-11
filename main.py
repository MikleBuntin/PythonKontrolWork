
import controller.Controller

print("Добрый день!")
command = 0

while command != "Q":
    print("Доступные операции:\n"
        "1 - Просмотреть все заметки; \n" +
        "2 - Добавить заметку \n" +
        "3 - Удалить заметку \n" +
        "4 - Исправить заметку \n" +
        "Q - выйти")
    command = input("Введите команду")
    if command == "1":
        controller.Controller.viewAll()
    elif command == "2":
        controller.Controller.add()
    elif command == "3":
        controller.Controller.delete();
    elif command == "4":
        controller.Controller.change();



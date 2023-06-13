
import controller.Controller

print("Добрый день!")
try:
    file = open('NoteList.csv', 'r')
    print('NoteList.csv opened')
except OSError:
    file = open('NoteList.csv', 'w')
    print('New file NoteList.csv created')

command = 0

while command != "Q":
    print("Доступные операции:\n"
        "1 - Просмотреть все заметки; \n" +
        "2 - Добавить заметку \n" +
        "3 - Удалить заметку \n" +
        "4 - Исправить заметку \n" +
        "5 - Просмотреть одну заметку \n" +
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
    elif command == "5":
        controller.Controller.view();



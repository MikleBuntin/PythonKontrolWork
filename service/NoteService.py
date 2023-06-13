from datetime import datetime
import model
from repository import Repository


def add():
    id = Repository.getNewID()
    date1 = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    date2 = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    name = input("Введите название заметки")
    note = input("Введите текст заметки")
    newNote = model.Note(id, date1, date2, name, note)
    Repository.add(newNote)


def delete():
    id = int(input("Введите ID"))
    Repository.delete(id)


def change(line):
    model.Note.printNote(line)
    newNote = input("Введите новую заметку: ")
    return line[: line.find('date2=') + 6] + \
           datetime.now().strftime('%Y-%m-%d %H.%M.%S') + \
           line[line.find(';name='): line.find(';note=') + 6] + \
           newNote + ";;\n"


def view():
    id = input("Введите ID")
    Repository.view(id)
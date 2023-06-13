from datetime import datetime
from model import Note
from repository import Repository


def add():
    id = Repository.getNewID()
    date1 = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    date2 = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    name = input("Введите название заметки")
    text = input("Введите текст заметки")
    newNote = Note.Note(id, date1, date2, name, text)
    Repository.add(newNote)


def delete():
    id = int(input("Введите ID"))
    Repository.delete(id)


def change(line):
    Note.printNote(line)
    newNote = input("Введите новую заметку: ")
    return line[: line.find('date2=') + 6] + \
           datetime.now().strftime('%Y-%m-%d %H.%M.%S') + \
           line[line.find(';name='): line.find(';text=') + 6] + \
           newNote + ";;\n"


def view():
    id = input("Введите ID")
    Repository.view(id)
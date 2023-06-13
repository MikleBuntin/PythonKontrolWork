from datetime import datetime
from model.Note import Note
from repository import Repository


def add():
    id = Repository.getNewID()
    date1 = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    date2 = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    name = input("Введите название заметки")
    note = input("Введите текст заметки")
    newNote = Note(id, date1, date2, name, note)
    Repository.add(newNote)

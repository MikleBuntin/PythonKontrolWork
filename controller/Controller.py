from repository import Repository
from service import NoteService


def viewAll():
    Repository.viewAll()

def add():
    NoteService.add()


def delete():
    NoteService.delete()


def view():
    NoteService.view()

def change():
    Repository.change()
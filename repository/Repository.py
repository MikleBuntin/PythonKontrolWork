from model import Note
import service

def viewAll():

    with open('NoteList.csv', 'r', encoding="cp1251") as noteList:
        print("All notes: \n")
        for line in noteList:
            Note.printNote(line)


def add(note):
    with open('NoteList.csv', 'a', encoding="cp1251") as noteList:

        noteList.write(note.toString())

def getNewID():
    with open('NoteList.csv', 'r') as noteList:
        max_id = 0
        for line in noteList:
            if line != '':
                id = int(line[line.find('ID=') + 3: line.find(';')])
                if id > max_id:
                    max_id = id
    return max_id + 1

def delete(delID):
    notes = []
    with open('NoteList.csv', 'r') as noteList:
         for line in noteList:
             if line != '':
                 id = int(line[line.find('ID=') + 3: line.find(';date1')])
                 if id != int(delID):
                     notes.append(line)
                 else:
                     print("Note ID: " + id + " DELETED")


    open('NoteList.csv', 'w').close()
    with open('NoteList.csv', 'a') as noteList:
        for line in notes:
            noteList.write(line)

def change():
    changeID = int(input("Введите ID"))
    notes = []
    with open('NoteList.csv', 'r') as noteList:
         for line in noteList:
             if line != '':
                 id = int(line[line.find('ID=') + 3: line.find(';date1')])
                 if id != int(changeID):
                     notes.append(line)
                 else:
                     notes.append(service.NoteService.change(line))
                     print("Note ID: " + str(id) + " Changed")


    open('NoteList.csv', 'w').close()
    with open('NoteList.csv', 'a') as noteList:
        for line in notes:
            noteList.write(line)

def view(viewID):
    with open('NoteList.csv', 'r') as noteList:
        for line in noteList:
            if line != '':
                id = int(line[line.find('ID=') + 3: line.find(';date1')])
                if id == int(viewID):
                    Note.printNote(line)



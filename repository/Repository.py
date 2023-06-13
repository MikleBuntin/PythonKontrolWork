import model

def viewAll():

    with open('NoteList.csv', 'r', encoding="cp1251") as noteList:
        print("All notes: \n")
        for line in noteList:
            model.Note.printNote(line)


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
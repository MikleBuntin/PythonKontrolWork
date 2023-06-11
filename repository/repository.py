import model

def viewAll():

    with open('NoteList.csv', 'r', encoding="cp1251") as noteList:
        print("All notes: \n")
        for line in noteList:
            model.Note.printNote(line)



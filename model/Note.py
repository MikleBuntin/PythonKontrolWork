
class Note:
    def __new__(cls, id, date1, date2, name, note):
        return super().__new__(cls)

    def __init__(self, id, date1, date2, name, note):
        self.id = id
        self.date1 = date1
        self.date2 = date2
        self.name = name
        self.note = note

    def toString(self):
        return "ID=" + str(self.id) + \
               ";date1=" + str(self.date1) + \
               ";date2=" + str(self.date2) + \
               ";name=" + self.name + \
               ";note=" + self.note + ";;\n"


def printNote(line):
    id = int(line[line.find('ID=') + 3: line.find(';')])
    date1 = line[line.find('date1=') + 6: line.find(';date2=')]
    date2 = line[line.find('date2=') + 6: line.find(';name=')]
    name = line[line.find('name=') + 5: line.find(';note=')]
    note = line[line.find('note=') + 5: line.find(';;')]
    print("Created date:" + date1 + "\n" +
          "Saved date:" + date2 + "\n" +
          "'" + name + "'" + ": \n" +
          note + "\n")

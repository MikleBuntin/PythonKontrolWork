class Note:
    def __new__(cls, id, date, name, note):
        return super().__new__(cls)

    def __init__(self, id, date, name, note):
        self.id = id
        self.date = date
        self.name = name
        self.note = note

    def toString(self):
        return "ID=" + str(self.id) + ";date=" + self.date + ";name=" + self.name + ";note=" + self.note + ";\n"


def printNote(line):
    id = int(line[line.find('ID=') + 3: line.find(';')])
    date =
    name = line[line.find('name=') + 6: line.find(';')]
    note = line[line.find('note=') + 6: line.find(';')]
    print("Date:" + date + "\n" +
          "'" + name + "'" + ": \n" +
          note)

class Note:
    def __new__(cls, id, date1, date2, name, text):
        return super().__new__(cls)

    def __init__(self, id, date1, date2, name, text):
        self.id = id
        self.date1 = date1
        self.date2 = date2
        self.name = name
        self.text = text

    def toString(self):
        return "ID=" + str(self.id) + \
               ";date1=" + str(self.date1) + \
               ";date2=" + str(self.date2) + \
               ";name=" + self.name + \
               ";text=" + self.text + ";;\n"


def printNote(line):
    id = int(line[line.find('ID=') + 3: line.find(';')])
    date1 = line[line.find('date1=') + 6: line.find(';date2=')]
    date2 = line[line.find('date2=') + 6: line.find(';name=')]
    name = line[line.find('name=') + 5: line.find(';text=')]
    text = line[line.find('text=') + 5: line.find(';;')]
    print("ID: " + str(id) + "\n" +
          "Created date:" + str(date1) + "\n" +
          "Saved date:" + str(date2) + "\n" +
          "'" + name + "'" + ": \n" +
          text + "\n")

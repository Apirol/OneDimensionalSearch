class InitReport:
    def __init__(self, filename):
        self.filename = filename
        self.handle = open(filename, "w")
        self.handle.write("\t{}\t\t\t{}\t\t\t""{}\t\t\t{}\t\t\t""{}\t\t\t{}\t""{}\t{}\n".format
                     ("X1", "X2", "F1", "F2", "Current A", "Current B", "Current lenght",
                      "Previous lenght  / (Current lenght"))

    def get_handle(self):
        return self.handle

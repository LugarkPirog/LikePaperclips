
class StatTracer:
    def __init__(self):
        self.struct = dict()

    def log(self, name):
        if name in self.struct:
            self.struct[name] += 1
        else:
            self.struct[name] = 1

    def __repr__(self):
        return str(self.struct)

    def __str__(self):
        return str(self.struct)

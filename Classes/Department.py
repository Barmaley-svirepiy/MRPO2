class Department():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.vacansy = []

    def __eq__(self, other):
        if isinstance(other, Department):
            return (
                    self.id == other.id and
                    self.name == other.name and
                    self.vacansy == other.vacansy
            )
        return False

    def Add_vacancy(self, vac):
        self.vacansy.append(vac)

    def Delete_vacancy(self, vac):
        self.vacansy.remove(vac)

class Organization():
    def __init__(self, id, name, addr):
        self.id = id
        self.name = name
        self.addr = addr
        self.departments = []

    def __eq__(self, other):
        if isinstance(other, Organization):
            return (
                        self.id == other.id and
                        self.name == other.name and
                        self.addr == other.addr and
                        self.departments == other.departments)
        return False


    def NoOneDep(self, dep):
        return True if dep not in self.departments else False


    def Add_dep(self, dep):
        if self.NoOneDep(dep):
            self.departments.append(dep)
        else:
            print('такой уже есть')


    def Delete_dep(self, dep):
        self.departments.remove(dep)
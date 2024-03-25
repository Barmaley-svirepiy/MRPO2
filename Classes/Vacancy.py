class Vacancy():
    def __init__(self, id,  name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        self.dutes = []
        self.skills = []
        self.seekers = []


    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return (
                        self.id == other.id and
                        self.name == other.name and
                        self.salary == other.salary and
                        self.dutes == other.dutes and
                        self.skills == other.skills and
                        self.seekers == other.seekers)
        return False
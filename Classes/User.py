class User():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.skills = []

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.id == other.id and
                    self.name == other.name and
                    self.age == other.age and
                    self.skills == other.skills)
        return False

    def NoOneSkill(self, skill):
        return True if skill not in self.skills else False

    def Add_skill(self, skill):
        if self.NoOneSkill(skill):
            self.skills.append(skill)
        else:
            print("Такой уже есть")

    def Delete_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
        else:
            print('Такого навыка нет')

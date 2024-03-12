class Vacancy_repository():
    def __init__(self):
        self.vacancys = []


    def save_vacancy(self, vacancy):
        self.vacancys.append(vacancy)


    def find_vacancy_by_id(self, vacancy_id):
        for vac in self.vacancys:
            if vac.id == vacancy_id:
                return vac
        return None
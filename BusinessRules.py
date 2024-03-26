class BusinessRules():
    def __init__(self, vac_rep):
        self.vacs = vac_rep

#функция поиска вакансии по зарплате
    def filter_vacancy(self, min_salary, max_salary):
        suitable_vac = []
        for i in self.vacs:
            if min_salary <= i.salary <= max_salary:
                suitable_vac.append(i)
        return suitable_vac


#функция проверки того что пользователь не подал 2 заявки на 1 вакансию
    def NotOnOneVacancy(self, user, vac):
        return False if user in vac.seekers else True

# функция проверки подходит ли пользователь на вакансию по навыкам
    def SuitableUser(self, user, vacancy):
        return set(vacancy.skills).issubset(set(user.skills))

#функция вывода самых популярных вакансий
    def popular_vacancy(self):
        vacancy_count = {}
        for vacancy in self.vacs:
            for user in vacancy.seekers:
                if vacancy.name in vacancy_count:
                    vacancy_count[vacancy.name] += 1
                else:
                    vacancy_count[vacancy.name] = 1
        popular_vacancies = sorted(vacancy_count.items(), key=lambda x: x[1], reverse=True)
        return popular_vacancies

#Функция отклика на вакансию
    def Otklick(self, user, vac):
        if vac in self.vacs:
            if self.SuitableUser(user, vac):
                if self.NotOnOneVacancy(user, vac):
                    vac.seekers.append(user)
                    return 1
                else:
                    print("Уже подавали")
                    return -1
            else:
                print("Вы к сожалению не подходите")
                return -1

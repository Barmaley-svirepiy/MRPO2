import unittest
from Classes.Skills import Skills
from Classes.User import User
from Classes.Vacancy import Vacancy
from BusinessRules import BusinessRules

class TestBusinessRules(unittest.TestCase):

    def test_filter_vacancy(self):
        vac_rep = [Vacancy(1, "Software Engineer", 50000), Vacancy(2, "Data Analyst", 45000)]
        business_rules = BusinessRules(vac_rep)

        # Тестирование, что вакансии фильтруются корректно по зарплате
        self.assertEqual(business_rules.filter_vacancy(40000, 55000), vac_rep)
        self.assertEqual(business_rules.filter_vacancy(46000, 55000), [Vacancy(1, "Software Engineer", 50000)])
        self.assertEqual(business_rules.filter_vacancy(40000, 47000), [Vacancy(2, "Data Analyst", 45000)])

    def test_NotOnOneVacancy(self):
        user = User(1, "John", 25)
        vac = Vacancy(1, "Software Engineer", 50000)
        vac.seekers.append(user)

        business_rules = BusinessRules([])

        # Пользователь уже подал заявку на вакансию
        self.assertFalse(business_rules.NotOnOneVacancy(user, vac))

        # Пользователь ещё не подавал заявку на вакансию
        self.assertTrue(business_rules.NotOnOneVacancy(User(2, "Alice", 30), vac))

    def test_SuitableUser(self):
        user = User(1, "John", 25)
        user.skills = [Skills(1, "Python"), Skills(2, "Data Analysis"), Skills(3, "Machine Learning")]

        vacancy = Vacancy(1, "Software Engineer", 50000)
        vacancy.skills = [Skills(1, "Python"), Skills(3, "Machine Learning")]

        business_rules = BusinessRules([])

        # Проверка, что пользователь подходит на вакансию по навыкам
        self.assertTrue(business_rules.SuitableUser(user, vacancy))

        # Проверка, что пользователь не подходит на вакансию по навыкам
        vacancy.skills.append(Skills(4, "Java"))
        self.assertFalse(business_rules.SuitableUser(user, vacancy))

    def test_popular_vacancy(self):
        vac_rep = [Vacancy(1, "Software Engineer", 50000), Vacancy(2, "Data Analyst", 45000)]
        user1 = User(1, "John", 25)
        user2 = User(2, "Alice", 30)
        user3 = User(3, "Bob", 28)

        vac_rep[0].seekers.extend([user1, user2])
        vac_rep[1].seekers.extend([user1, user3])

        business_rules = BusinessRules(vac_rep)

        # Проверка, что вакансии упорядочены в порядке популярности
        self.assertEqual(business_rules.popular_vacancy(), [("Software Engineer", 2), ("Data Analyst", 2)])


if __name__ == '__main__':
    unittest.main()
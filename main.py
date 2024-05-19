from Classes.Organization import Organization
from Classes.User import User
from Repositories.XMLRepos import XMLRepository
from Repositories.sqlRepos import SQLAlchemyRepository
from BusinessRules import BusinessRules
from db_setup import UserModel, SkillModel, VacancyModel, session
from Classes.Vacancy import Vacancy
import os


def main():
    user_repo = SQLAlchemyRepository(session)

    # Создаем экземпляры
    user = UserModel(id=1, name="Pasha", age=31)
    skill = SkillModel(id=1, name="Python")
    user.skills.append(skill)

    vacancy = VacancyModel(id=1, name="Developer", salary=120000.0)
    vacancy.skills.append(skill)

    user_repo.save(user)
    user_repo.save(skill)
    user_repo.save(vacancy)

    bus = BusinessRules(session)
    result = bus.Otklick(user_id=1, vac_id=1)
    print(result)  # Вывод: 1 если успешно


if __name__ == "__main__":
    main()

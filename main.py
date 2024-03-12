from Department import Department
from Department_repository import Department_repository
from Dutes_repository import Dutes_repository
from Dutes import Dutes
from org_repository import Org_repository
from Organization import Organization
from Skills import Skills
from skills_repository import Skills_repository
from User import User
from user_repository import User_repository
from Vacancy import Vacancy
from Vacancy_repository import Vacancy_repository


dep_rep = Department_repository()
dutes_rep = Dutes_repository()
org_rep = Org_repository()
skill_rep = Skills_repository()
user_rep = User_repository()
vac_rep = Vacancy_repository()


dute1 = Dutes(1, 'asdqwe')
dutes_rep.save_dute(dute1)


vac1 = Vacancy(1 , 123)
vac1.dutes.append(dute1)
vac_rep.save_vacancy(vac1)

dep1 = Department(1, 'dep1')
dep1.needDutes.append(dute1)
dep1.vacansy.append(vac1)
dep_rep.save_department(dep1)


org1 = Organization(1, 'org1', 'qweewq')
org1.departments.append(dep1)
org_rep.save_org(org1)

skill1 = Skills(1 , 'skill1')
skill_rep.save_skills(skill1)

user1 = User(1, 'user1', 12)
user1.skills.append(skill1)
user_rep.save_user(user1)


user_data = user_rep.find_user_by_id(1)
dep_data = dep_rep.find_department_by_id(1)

print(f'User: {user_data.name}')
print(f'Department: {dep_data.name}')
print(f'Открытые вакансии:')
for i in dep_data.vacansy:
    print(i.name)
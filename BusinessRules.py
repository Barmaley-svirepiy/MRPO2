from db_setup import UserModel, VacancyModel, SeekerModel

class BusinessRules:
    def __init__(self, session):
        self.session = session
        self.vacs = session.query(VacancyModel).all()

    def Otklick(self, user_id, vac_id):
        user = self.session.query(UserModel).filter_by(id=user_id).one()
        vac = self.session.query(VacancyModel).filter_by(id=vac_id).one()

        if vac in self.vacs:
            if self.SuitableUser(user, vac):
                if self.NotOnOneVacancy(user, vac):
                    seeker = SeekerModel(user_id=user.id, vacancy_id=vac.id)
                    self.session.add(seeker)
                    self.session.commit()
                    return 1
                else:
                    print("Уже подавали")
                    return -1
            else:
                print("Вы к сожалению не подходите")
                return -1

    def NotOnOneVacancy(self, user, vac):
        return not self.session.query(SeekerModel).filter_by(user_id=user.id, vacancy_id=vac.id).count() > 0

    def SuitableUser(self, user, vacancy):
        user_skills = set(skill.id for skill in user.skills)
        vac_skills = set(skill.id for skill in vacancy.skills)
        return vac_skills.issubset(user_skills)

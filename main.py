from Repositories import JSONRepos
from Classes.User import User
from Classes.Vacancy import Vacancy
from Repositories import JSONRepos


def find_user_by_name(name1):
    def query(obj):
        if isinstance(obj, User):
            return obj.name == name1
        return False

    return query


def find_service_by_name(name):
    def query(obj):
        if isinstance(obj, Vacancy):
            return obj.name == name
        return False

    return query


json_rep = JSONRepos.JsonRepository('data')
user = User(1, 'john doe', 12)
user.skills.append("Java")

vac = Vacancy(1, "Job", 1200)
vac.skills.append("Java")
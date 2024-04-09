from Classes.Organization import Organization
from Classes.User import User
from Repositories.XMLRepos import XMLRepository


def save_to_xml(user_data):
    repository = XMLRepository("base.xml")
    repository.save(user_data)


def find_users_by_age(name):
    user_repository = XMLRepository("user.xml")
    query = f"//item[name='{name}']"
    users = user_repository.find()
    return users


if __name__ == "__main__":
    user_data = {
        'id': 1,
        'name': "Pasha",
        'age': 31,
    }
    user = User(**user_data)  # Создаем экземпляр класса User из словаря user_data
    save_to_xml(user)
    user_data = {
        'id': 2,
        'name': "Pasha",
        'age': 31,
    }
    user = User(**user_data)  # Создаем экземпляр класса User из словаря user_data
    save_to_xml(user)
    user = User(3, 'qwe', 30)
    save_to_xml(user)

    org_data = {
        'id': 2,
        'name': 'Golden Apple',
        'addr': 'Kolotushkina house.'
    }
    org = Organization(**org_data)
    save_to_xml(org)
    org_data = {
        'id': 1,
        'name': 'Golden Apple',
        'addr': 'Kolotushkina house.'
    }
    org = Organization(**org_data)
    save_to_xml(org)

    print('')
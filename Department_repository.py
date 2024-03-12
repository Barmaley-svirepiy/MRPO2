class Department_repository():
    def __init__(self):
        self.departmens = []


    def save_department(self, dep):
        self.departmens.append(dep)


    def find_department_by_id(self, dep_id):
        for dep in self.departmens:
            if dep.id == dep_id:
                return dep
        return None
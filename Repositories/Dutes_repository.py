class Dutes_repository():
    def __init__(self):
        self.dutes = []


    def save_dute(self, dute):
        self.dutes.append(dute)


    def find_dute_by_id(self, dute_id):
        for dute in self.dutes:
            if dute.id == dute_id:
                return dute
        return None
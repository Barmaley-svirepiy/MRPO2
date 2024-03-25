class Org_repository():
    def __init__(self):
        self.orgs = []


    def save_org(self, organization):
        self.orgs.append(organization)


    def find_org_by_id(self, organization_id):
        for org in self.orgs:
            if org.id == organization_id:
                return org
        return None
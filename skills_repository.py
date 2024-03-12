class Skills_repository():
    def __init__(self):
        self.skills = []


    def save_skills(self, skill):
        self.skills.append((skill))


    def find_skill_by_id(self, skill_id):
        for skill in self.skills:
            if skill.id == skill_id:
                return skill
        return None
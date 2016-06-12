class CommunityDO(object):
    def __init__(self, id):
        self.id = id
        self.users = []
        self.impact_score = 1
        self.sentiment = 0

    def add_user(self, user):
        self.users.append(user)


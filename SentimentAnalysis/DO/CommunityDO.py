class CommunityDO(object):
    def __init__(self, id):
        self.id = id
        self.users = []
        self.impact_score = 1

    def add_user(self, user):
        self.users.append(user)

    def get_sentiment(self):
        # TODO implement this method
        return 1

class UserDO(object):
    def __init__(self, id):
        self.id = id
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_sentiment(self):
        # TODO implement this method
        return 1

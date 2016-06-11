class PostDO(object):
    def __init__(self, id):
        self.id = id
        self.comments = []
        self.descriptionText = ''

    def add_comment(self, comment):
        self.comments.append(comment)

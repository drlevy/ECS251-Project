class PostDO(object):
    def __init__(self, id):
        self.id = id
        # TODO include comments
        self.comments = []
        self.message = ''
        self.sentiment = 0

    def __repr__(self):
        comment_str = ''
        first = True
        for comment in self.comments:
            if first:
                first = False
            else:
                comment_str += ', '
            comment_str += str(comment)

        return \
            'PostDO(' \
            '\'id\':{0}, ' \
            '\'comments\':[{1}], ' \
            '\'message\':{2}, ' \
            '\'sentiment\':{3}'.format(
                self.id,
                comment_str,
                self.message,
                self.sentiment) + ')'

    def add_comment(self, comment):
        self.comments.append(comment)

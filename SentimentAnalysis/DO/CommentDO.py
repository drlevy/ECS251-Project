class CommentDO(object):
    def __init__(self, id):
        self.id = id
        self.post_id = 0
        self.message = ''
        self.sentiment = 0

    def __repr__(self):
        return \
            'CommentDO(' \
            '\'id\':{0}, ' \
            '\'message\':{1}, ' \
            '\'sentiment\':{2})'.format(
                self.id,
                self.message,
                self.sentiment)

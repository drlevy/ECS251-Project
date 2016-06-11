from SentimentAnalysis.DO.CommentDO import CommentDO


class CommentDAO(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def find_comment_by_id(self, id):
        comment = CommentDO(id)
        # TODO implement this method
        return comment





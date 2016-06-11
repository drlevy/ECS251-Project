from SentimentAnalysis.DO.PostDO import PostDO


class PostDAO(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def find_post_by_id(self, id):
        post = PostDO(id)
        # TODO implement this method
        return post






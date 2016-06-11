from SentimentAnalysis.DO.UserDO import UserDO


class UserDAO(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def find_user_by_id(self, id):
        user = UserDO(id)
        # TODO implement this method
        return user

    def update_user(self, id, user):
        # TODO implement this method
        return




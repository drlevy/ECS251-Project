import configparser
from SentimentAnalysis.Utility.Singleton import Singleton
from SentimentAnalysis.DAO.PostDAO import PostDAO
from SentimentAnalysis.DAO.UserDAO import UserDAO
from SentimentAnalysis.DAO.CommunityDAO import CommunityDAO
from SentimentAnalysis.DO.SqlDO import SqlDO


class DomainController(object, metaclass=Singleton):
    def __init__(self):
        # TODO should config dependency be injected (or moved to BaseDAO)?
        self._config_file_path = 'Files/config.ini'

        config = configparser.ConfigParser()
        config.read(self._config_file_path)

        self._post_keywords = config['sentiment']['keywords'].strip().split(',')

        self._sql = SqlDO(
            config['mysql']['usr'],
            config['mysql']['passwd'],
            config['mysql']['host'],
            config['mysql']['db'])

        self._user_file_path = config['files']['user_file_path']
        self._community_file_path = config['files']['community_file_path']

        self._post_dao = PostDAO(self._sql)
        self._user_dao = UserDAO(self._user_file_path, self._sql)
        self._community_dao = CommunityDAO(self._community_file_path)

        self._posts = None
        self._users = None
        self._communities = None

        self.aggregate_sentiment = 0

    def get_posts(self):
        if self._posts is None:
            self._posts = self._post_dao.get_posts_for_keywords(self._post_keywords)
        return self._posts

    def get_users(self):
        if self._users is None:
            self._users = self._user_dao.get_users_for_keywords(self._post_keywords)
        return self._users

    def get_communities(self, users):
        if self._communities is None:
            self._communities = self._community_dao.get_communities(users)
        return self._communities

    def update_users(self, users):
        # TODO implement this method
        return 1

    def update_communities(self, users):
        # TODO implement this method
        return 1

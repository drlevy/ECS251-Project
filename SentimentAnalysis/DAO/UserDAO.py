from SentimentAnalysis.DAO.BaseDAO import BaseDAO
from SentimentAnalysis.DO.UserDO import UserDO
from SentimentAnalysis.DO.CommentDO import CommentDO


# TODO this DAO has a lot of side-effects and responsibilities - refactor?
class UserDAO(BaseDAO):
    def __init__(self, user_data_file_path, sql):
        super(UserDAO, self).__init__(user_data_file_path, sql)

    def get_users_for_keywords(self, keywords):
        users = {}

        user_community_data = self._delimited_file_helper.get_rows_by_id()

        # build user filter criteria for sql query
        user_sql_criteria = ''
        first = True
        for user_id in user_community_data:
            user = UserDO(user_id)
            user.community_id = user_community_data[user_id][1]
            users[user_id] = user
            if first:
                first = False
            else:
                user_sql_criteria += ' or '
            user_sql_criteria += 'comment.fb_id = \'{0}\''.format(user_id)

        # build post filter criteria for sql query
        post_sql_criteria = ''
        first = True
        for keyword in keywords:
            if first:
                first = False
            else:
                post_sql_criteria += ' or '
            post_sql_criteria += 'post.message like \'%{0}%\''.format(keyword)

        # fetch comments
        comment_sql_query =\
            'select comment.id, comment.fb_id, comment.message, comment.post_id from {0}.comment '.format(self._sql_db) +\
            'where comment.post_id in (' +\
            'select comment.fb_id from {0}.comment, {0}.post '.format(self._sql_db) +\
            'where ' + post_sql_criteria + ') ' +\
            'and ' + user_sql_criteria

        cursor = self._sql_cnx.cursor()
        cursor.execute(comment_sql_query)

        # add comments to users
        for row in cursor:
            comment = CommentDO(row[0])
            comment.message = row[2]
            comment.post_id = row[3]
            users[str(row[1])].add_comment(comment)

        return users

    def update_users(self, users):
        # TODO implement this method
        return




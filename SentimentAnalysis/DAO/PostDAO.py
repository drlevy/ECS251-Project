from SentimentAnalysis.DAO.BaseDAO import BaseDAO
from SentimentAnalysis.DO.PostDO import PostDO


class PostDAO(BaseDAO):
    def __init__(self, sql):
        super(PostDAO, self).__init__(sql=sql)

    def get_posts_for_keywords(self, keywords):
        posts = {}

        # build post filter criteria for sql query
        post_sql_criteria = ''
        first = True
        for keyword in keywords:
            if first:
                first = False
            else:
                post_sql_criteria += ' or '
            post_sql_criteria += 'post.message like \'%{0}%\''.format(keyword)

        # TODO would it be useful to have the matching keywords in each PostDO?

        # fetch posts
        posts_sql_query =\
            'select post.id, post.message from {0}.post '.format(self._sql_db) +\
            'where ' + post_sql_criteria

        cursor = self._sql_cnx.cursor()
        cursor.execute(posts_sql_query)

        # create posts
        for row in cursor:
            post = PostDO(row[0])
            post.message = row[1]
            posts[row[0]] = post

        return posts

    def update_posts(self, users):
        # TODO implement this method
        return




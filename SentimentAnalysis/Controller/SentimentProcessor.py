from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import numpy as np
from SentimentAnalysis.Utility.Singleton import Singleton
from SentimentAnalysis.Controller.DomainController import DomainController


class SentimentProcessor(object, metaclass=Singleton):
    def __init__(self):
        self._domain_controller = DomainController()

    def analyze_and_set_sentiments(self):
        communities = \
            self._domain_controller.get_communities(
                self._domain_controller.get_users())
        community_sentiments = []
        for community_id in communities:
            community = communities[community_id]
            self.analyze_and_set_sentiment_for_community(community)
            # use impact score to weigh sentiment
            community_sentiments.append(community.sentiment*community.impact_score)
        self._domain_controller.aggregate_sentiment = np.mean(community_sentiments)

    def analyze_and_set_sentiment_for_community(self, community):
        user_sentiments = []
        for user in community.users:
            self.analyze_and_set_sentiment_for_user(user)
            user_sentiments.append(user.sentiment)
        community.sentiment = np.mean(user_sentiments)

    def analyze_and_set_sentiment_for_user(self, user):
        # find sentiment for each user comment
        posts = self._domain_controller.get_posts()
        comment_sentiments = []
        for comment in user.comments:
            post = posts[comment.post_id]
            self.analyze_and_set_sentiment_for_post(post)
            self.analyze_and_set_sentiment_for_comment(comment)
            # scale comment sentiment by post sentiment
            comment_sentiments.append(comment.sentiment*post.sentiment)
        # aggregate user sentiment
        user.sentiment = np.mean(comment_sentiments)

    def analyze_and_set_sentiment_for_post(self, post):
        post.sentiment = self.avg_message_sentiment_helper(post.message)

    def analyze_and_set_sentiment_for_comment(self, comment):
        comment.sentiment = self.avg_message_sentiment_helper(comment.message)

    def avg_message_sentiment_helper(self, message):
        sentences = tokenize.sent_tokenize(message)
        sid = SentimentIntensityAnalyzer()
        sentence_sentiments = []
        for sentence in sentences:
            ss = sid.polarity_scores(sentence)
            sentence_sentiments.append(ss['compound'])
        return np.mean(sentence_sentiments)

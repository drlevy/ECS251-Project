from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import numpy as np
from SentimentAnalysis.Utility.Singleton import Singleton
from SentimentAnalysis.Controller.DomainController import DomainController


class SentimentProcessor(object, metaclass=Singleton):
    def __init__(self):
        self._domain_controller = DomainController()

    # TODO process sentiment for topic

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
        comment_sentiments = []
        for comment in user.comments:
            sentences = tokenize.sent_tokenize(comment.message)
            sid = SentimentIntensityAnalyzer()
            sentence_sentiments = []
            for sentence in sentences:
                ss = sid.polarity_scores(sentence)
                sentence_sentiments.append(ss['compound'])
            comment.sentiment = np.mean(sentence_sentiments)
            comment_sentiments.append(comment.sentiment)
        # aggregate user sentiment
        user.sentiment = np.mean(comment_sentiments)


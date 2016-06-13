from SentimentAnalysis.Utility.Singleton import Singleton
from SentimentAnalysis.Controller.DomainController import DomainController


class StatisticsGenerator(object, metaclass=Singleton):
    def print_sentiments(self):
        dc = DomainController()

        print('user sentiment scores')
        users = dc.get_users()
        sorted_user_ids = sorted(users)
        for user_id in sorted_user_ids:
            print(
                'user_id: {0}, '
                'community_id: {1}, '
                'sentiment_score: {2}'
                .format(
                    users[user_id].id,
                    users[user_id].community_id,
                    users[user_id].sentiment))

        print('\ncommunity sentiment scores')
        communities = dc.get_communities(users)
        sorted_community_ids = sorted(communities)
        for community_ids in sorted_community_ids:
            print(
                'community_id: {0}, '
                'sentiment_score: {1}'
                .format(
                    communities[community_ids].id,
                    communities[community_ids].sentiment))

        print('\naggregate sentiment score')
        aggregate_sentiment = dc.aggregate_sentiment
        print(aggregate_sentiment)


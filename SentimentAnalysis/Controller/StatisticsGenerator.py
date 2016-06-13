from SentimentAnalysis.Utility.Singleton import Singleton
from SentimentAnalysis.Controller.DomainController import DomainController


class StatisticsGenerator(object, metaclass=Singleton):
    def print_sentiments(self):
        dc = DomainController()

        print('user sentiment scores scaled by post sentiment')
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

        print('\ncommunity sentiment scores not scaled by impact score')
        communities = dc.get_communities(users)
        sorted_community_ids = sorted(communities)
        for community_ids in sorted_community_ids:
            print(
                'community_id: {0}, '
                'sentiment_score: {1}'
                .format(
                    communities[community_ids].id,
                    communities[community_ids].sentiment))

        print('\naggregate sentiment score without impact scaling')
        raw_aggregate_sentiment = dc.raw_aggregate_sentiment
        print('raw: {0}, scaled: {1}'.format(raw_aggregate_sentiment, (raw_aggregate_sentiment+1)/2))

        print('\naggregate sentiment score with impact scaling')
        aggregate_sentiment = dc.aggregate_sentiment
        print('raw: {0}, scaled: {1}'.format(aggregate_sentiment, (aggregate_sentiment+1)/2))

        print('\nsimplified user percentage popular vote scaled by post sentiment')
        user_sentiment_sum = 0
        for user_id in users:
            user_sentiment_sum += users[user_id].sentiment
        print('raw: {0}, scaled: {1}'.format(user_sentiment_sum/len(users), ((user_sentiment_sum/len(users)) + 1) / 2))

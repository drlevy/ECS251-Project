import networkx as nx
from SentimentAnalysis.Utility.Singleton import Singleton
from SentimentAnalysis.Controller.DomainController import DomainController


class GraphGenerator(object, metaclass=Singleton):
    def generate_graph(self):
        dc = DomainController()

        # average sentiment
        aggregate_sentiment = dc.aggregate_sentiment

        # dictionary containing UserDOs indexed by user id
        users = dc.get_users()

        # dictionary containing CommunityDOs indexed by community id
        communities = dc.get_communities(users)

        # TODO use networkx to write out 'community_graph.gexf'
        # nx.cool_stuff.doit()

        return

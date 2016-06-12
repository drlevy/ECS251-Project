import sys
from SentimentAnalysis.Controller.SentimentProcessor import SentimentProcessor
from SentimentAnalysis.Controller.GraphGenerator import GraphGenerator
from SentimentAnalysis.Controller.DomainController import DomainController


def main(args):
    dc = DomainController()
    sp = SentimentProcessor()
    gg = GraphGenerator()

    sp.analyze_and_set_sentiments()
    print('aggregate sentiment score: ' + str(dc.aggregate_sentiment))

    gg.generate_graph()
    print('graph generated ...')

    sys.exit(0)

main(sys.argv)

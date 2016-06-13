import sys
from SentimentAnalysis.Controller.SentimentProcessor import SentimentProcessor
from SentimentAnalysis.Controller.GraphGenerator import GraphGenerator
from SentimentAnalysis.Controller.DomainController import DomainController
from SentimentAnalysis.Controller.StatisticsGenerator import StatisticsGenerator


def main(args):
    dc = DomainController()
    sp = SentimentProcessor()
    gg = GraphGenerator()
    sg = StatisticsGenerator()

    sp.analyze_and_set_sentiments()

    sg.print_sentiments()

    sys.exit(0)

main(sys.argv)

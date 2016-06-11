from SentimentAnalysis.DO.CommunityDO import CommunityDO


class CommunityDAO(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def find_community_by_id(self, id):
        community = CommunityDO(id)
        # TODO implement this method
        return community

    def update_community(self, id, community):
        # TODO implement this method
        return




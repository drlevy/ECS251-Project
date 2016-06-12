from SentimentAnalysis.DAO.BaseDAO import BaseDAO
from SentimentAnalysis.DO.CommunityDO import CommunityDO


class CommunityDAO(BaseDAO):
    def __init__(self, community_data_file_path):
        super(CommunityDAO, self).__init__(community_data_file_path)

    def get_communities(self, users):
        communities = {}

        community_data = self._delimited_file_helper.get_rows_by_id()
        for community_id in community_data:
            community = CommunityDO(community_id)
            community.impact_score = float(community_data[community_id][1])
            for userId in users:
                if users[userId].community_id == community_id:
                    community.add_user(users[userId])
            communities[community_id] = community

        return communities

    def update_communities(self, communities):
        # TODO implement this method
        return




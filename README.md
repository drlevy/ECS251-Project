# ECS251-Project
Objective: Provide a simple and useful measure of users’ sentiment on a specific topic (e.g. case study: Snowden)
using database of all posts, comments, and likes from NYT facebook page in 2013. 
(See powerpoint presentation "FinalProject.pptx" for more details)

Contacts:
lounguyen@ucdavis.edu
drlevy@ucdavis.edu

Scripts:
Clustering is done with "preprocessor.py" 
 Output: 
  - Clusters_  text file with <fb_id> <community_id>
  - ComImpactScore_  text file <community_id> <impact ranking>

"Modularity_on_single_post.py"
Input:
  - Facebook New York Times postid
Output:
  - A gexf graph file with communities information, and centrality information
  
  *Both accesses a database on localhost hosting ECS251 data dump
  
"Sentiment Analysis"
.... to be updated


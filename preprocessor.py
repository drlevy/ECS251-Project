import configparser
import mysql.connector
import sys
import time
from collections import defaultdict
import community
import networkx as nx

config = configparser.ConfigParser()
config.read('config.ini')

cnx = mysql.connector.connect(
    user=config['mysql']['usr'],
    password=config['mysql']['passwd'],
    host=config['mysql']['host'],
    database=config['mysql']['db']
)

if cnx.is_connected():
    print('Connected to MySQL database')
else:
    print('Could not connect to db')
    sys.exit()

cursor = cnx.cursor()
cursor.execute("SELECT * FROM nyt.likedby WHERE likedby.fb_id"
               + " IN (SELECT comment.fb_id FROM nyt.comment, nyt.post"
               + " WHERE (post.message LIKE '%Snowden%') "
               + " AND (post.id = comment.post_id)) AND (likedby.comment_id=0)")

row = cursor.fetchone()
postid_likesgroup_map = defaultdict(list)
nodeid_fbid_map= dict()
fbid_nodeid_map = dict()

k = 0
while row is not None:
    ## fb_id
    fbid = row[3]

    if fbid not in fbid_nodeid_map:
        fbid_nodeid_map[fbid]= k
        nodeid_fbid_map[k] = fbid
        nodeid = k
        k = k + 1
    else:
        nodeid = fbid_nodeid_map[fbid]
        
    postid_likesgroup_map[row[1]].append(nodeid)
    row = cursor.fetchone()

#  postid_likesgroup_map is a dictionary of lists of people
#  that liked the same posts


mat_size = k
d_likes = dict()
# building up adjacency matrix
for post, users in postid_likesgroup_map.items():
    for i in users:
        for j in users:
            if i==j:
                continue
            idx = i*mat_size +j
            if ( idx not in d_likes):
                d_likes[idx] = 1;
            else:
                d_likes[idx] += 1;


# Building up undirected weighted graph
G = nx.Graph()
for key,value in nodeid_fbid_map.items():
    G.add_node(key, Label=str(value))

for key, value in d_likes.items():
    j = key % mat_size
    i = key / mat_size
    if i < j:  #symmetric
        G.add_edge( i, j, weight=value)

# Community Detection
parts = community.best_partition(G)
nx.set_node_attributes(G, "Modularity Class", parts);
#nx.set_node_attributes(G, "Label", nodeid_fbid_map);

# output graph file
    
#os.chdir('GraphIII')
timestr = time.strftime("%Y%m%d-%H%M%S")
output =  "t_" + timestr
nx.write_gexf(G,output + ".gexf")

# output fbid to community id
fout = open("Clusters_" + output + ".txt",'w');
for key, value in fbid_nodeid_map.items():
    fout.write(str(key) + ' ' + str(parts[value])+'\n')
fout.close()

# output community ranking
fout2 = open("ComImpactScore_" + output + ".txt",'w');
com_ranks = dict()
for key, value in parts.items():
    if value not in com_ranks:
        com_ranks[value] = 1
    else:
        com_ranks[value] += 1
for key, value in com_ranks.items():
    fout2.write(str(key) + ' ' + str(value)+'\n')
fout2.close()


#output statistics of run
#fstats = open

cursor.close()
cnx.close()

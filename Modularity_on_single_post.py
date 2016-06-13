import configparser
import mysql.connector
import os
import sys
import community
import networkx as nx
import matplotlib.pyplot as plt
import time
import csv

#############
# This script is used to study network structure within individual FB post
#
#

postid = raw_input("Enter post_id: ");
mySQLquery = "SELECT likedby.fb_id,likedby.comment_id,comment.fb_id,comment.message FROM nyt.likedby, nyt.comment"+ " WHERE likedby.post_id = \'" + postid + "\' AND likedby.comment_id = comment.id"
#print mySQLquery

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
cursor.execute(mySQLquery)

G = nx.DiGraph()
FBid_nodeid_map = dict()
nodeid_msg_map = dict()
cur_id = 0

rows = cursor.fetchall()

if ( len(rows)==0):
    print("No entries for " + postid)
    sys.exit()

for row in rows:
    if row[2] not in FBid_nodeid_map:
        FBid_nodeid_map[row[2]] = cur_id;
        nodeid_msg_map[cur_id] = str(row[2]) + row[3];
        cur_id += 1

for row in rows:
    if row[0] not in FBid_nodeid_map:
        FBid_nodeid_map[row[0]] = cur_id;
        nodeid_msg_map[cur_id] = str(row[0])
        cur_id += 1
    G.add_edge( FBid_nodeid_map[row[0]], FBid_nodeid_map[row[2]]);

## Associate each node with messages
nx.set_node_attributes(G, "Label", nodeid_msg_map);

## Community detection
#parts = community.best_partition(G)
#nx.set_node_attributes(G, "Modularity Class", parts);

## betweenness_centrality
btwncentral = nx.betweenness_centrality(G)
nx.set_node_attributes(G, "Inbetweenness Centrality", btwncentral);

## current_flow_closeness_centrality
#c1= nx.current_flow_closeness_centrality(G)
#nx.set_node_attributes(G, "current_flow_closeness_centrality", c1);

## current_flow_betweenness_centrality
#c2= nx.current_flow_betweenness_centrality(G)
#nx.set_node_attributes(G, "current_flow_betweenness_centrality", c2);

## load_centrality
c3 = nx.load_centrality(G)
nx.set_node_attributes(G, "load_centrality", c3);

#output
if not os.path.exists('GraphI'):
    os.makedirs('GraphI')
os.chdir('GraphI')
timestr = time.strftime("%Y%m%d-%H%M%S")
output = postid+ "_t_" + timestr
nx.write_gexf(G,output + ".gexf")
cursor.close()
cnx.close()


##fout = open("Clusters_" + output+".txt",'w');
##for key, value in FBid_nodeid_map.iteritems():
##    fout.write(str(key) +':' + str(parts[value])+'\n')
##fout.close()


##adjmatfile = open('Edges_10150316228114999.csv','rb');
##output = open('Nodes_10150316228114999CD.csv','wb');
##outwriter = csv.writer(output, delimiter=',')
##adjmat = csv.reader(adjmatfile)
##
##
##rownum = 0
##for row in adjmat:
##    if rownum==0:
##        rownum += 1
##        continue
##    i= int(float(row[0]))
##    j= int(float(row[1]))
##    k= int(float(row[2]))
##    G.add_edge(i, j)
##    rownum += 1
##
##count=0
##part = community.best_partition(G)
##for key, value in part.iteritems():
##    outwriter.writerow([key,value])
##
##output.close()
##adjmatfile.close()




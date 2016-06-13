import configparser
import mysql.connector
import sys
from collections import defaultdict


fkey = open('user_keys_Snowden2_small.txt', 'w')
fmat = open('adj_matrix_Snowden2_small.txt', 'w')
fdata = open('fdata_Snowden2_small.txt', 'w')


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
               + " WHERE (post.message LIKE '%Snowden%' OR post.message LIKE '%Wikileaks%') "
               + " AND (post.id = comment.post_id) )")

row = cursor.fetchone()
d = defaultdict(list)
cur_users = list()
k = -1

#while row is not None:
for l in range(1,200):
    ## fb_id
    u = row[3]

    ## renaming the first fb_id to be 0th row
    ## second fb_id that comes up is 1th row so on
    if u not in cur_users:
        cur_users.append(u)
        k = k + 1
        user_row = k
        ## save the fb_id --> row i correspondence in a file
        fkey.write(str(k) + ' ' + str(u) + '\n')
    ## if fb_id has appear already, use the previously assigned number
    else:
        user_row = cur_users.index(u)

    if user_row not in d[row[1]]:
        d[row[1]].append(user_row)
    fdata.write(str(row[1]) + ' ' + str(user_row) + '\n')
    row = cursor.fetchone()

print('last row is ' + str(row) + '\n')

mat_size = k + 1
d_likes = dict()

#  d is a dictionary of lists of people that liked the same posts
for post, users in d.iteritems():
    for i in users:
        for j in users:
            idx = i*mat_size +j
            if ( idx not in d_likes):
                d_likes[idx] = 1;
            else:
                d_likes[idx] += 1;

for key, value in d_likes.iteritems():
    if 
    j = key % mat_size
    i = key / mat_size
    ## sparse matrix notation: i j value
    fmat.write(str(i) + ' ' + str(j) + ' ' + str(value) + '\n')

fkey.close()
fmat.close();
fdata.close();
cursor.close()
cnx.close()

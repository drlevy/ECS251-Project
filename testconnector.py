import mysql.connector
from collections import defaultdict

fkey = open('user_keys_Snowden2.txt', 'w');
fmat = open('adj_matrix_Snowden2.txt', 'w');
fdata= open('fdata_Snowden2.txt', 'w');


cnx = mysql.connector.connect(user='root', password='luan92ucdavis',
                      host='127.0.0.1',
                      database='nyt')
if cnx.is_connected():
    print('Connected to MySQL database')

cursor = cnx.cursor()
cursor.execute("SELECT * FROM nyt.likedby WHERE likedby.fb_id"
               + " IN (SELECT comment.fb_id FROM nyt.comment, nyt.post"
               + " WHERE (post.message LIKE '%Snowden%' OR post.message LIKE '%Wikileaks%') "
	       + " AND (post.id = comment.post_id) )" ); 

row = cursor.fetchone()
d = defaultdict(list)
cur_users = list();
k =-1;

while row is not None:
    u = row[3]; ## fb_id

    ## 
    ## renaming the first fb_id to be 0th row
    ## second fb_id that comes up is 1th row so on
    ##
    if u not in cur_users:
        cur_users.append( u )
        k = k + 1
        user_row = k
        ## save the fb_id --> row i correspondence in a file
        fkey.write(str(k) + ' ' + str(u) + '\n')
    ##
    ## if fb_id has appear already, use the previously assigned number
    else:
        user_row = cur_users.index(u)
        
    d[row[1]].append( user_row )
    fdata.write( str(row[1]) +' '+ str(user_row)+'\n');
    row = cursor.fetchone()

print('last row is ' + str(row) +'\n')


mat_size = k + 1;
d_likes = dict()

for post,users in d.iteritems():
    for i in users:
        for j in users:
            d_likes[i*mat_size + j] +=1; 

for k,v in d_likes:
    j = k%mat_size;
    i = k/mat_size;
    ## sparse matrix notation: i j value
    fmat.write(str(i)+' '+str(j)+' '+str(v)+'\n'); 
            
cursor.close()
cnx.close()




    

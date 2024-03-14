# import the package
import pymysql

# setup the connection to the database
db = pymysql.connect(
    host = "localhost",
    user = "mp2",
    passwd = "eecs116",
    db = "blurts"
)

cur = db.cursor()


# Query 1:
sql = "select id, description, count(email)\
       from blurts.blurt_analysis, blurts.topic\
       where blurts.blurt_analysis.topicid = blurts.topic.id\
       group by id"

cur.execute(sql)
print("Query 1")
for row in cur.fetchall():
    print(row)
print()


# Query 2
sql = "select name, count(follower)\
       from blurts.user as usr, blurts.celebrity as cel, follow as fol\
       where usr.email = cel.email and fol.followee = cel.email\
       group by name"

cur.execute(sql)
print("Query 2")
for row in cur.fetchall():
    print(row)
print()


# Query 3
sql = "select name, count(text)\
       from blurts.user as usr, blurts.celebrity as cel, blurts.blurt as blu\
       where usr.email = cel.email and blu.email = cel.email\
       group by name\
       order by count(text) desc;"

cur.execute(sql)
print("Query 3")
for row in cur.fetchall():
    print(row)


# close the database connection
db.close()

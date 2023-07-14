import mysql.connector

# Connecting the server
dbconn= mysql.connector.connect(user = 'michael',
                            host = 'localhost',
                            database = 'microlingolo',
                            password='homewithsonatparty'
                               )

print(dbconn)

def getarray(sql):
    global lingolo_cursor
    lingolo_cursor.execute(sql)

    return lingolo_cursor.fetchall()

def insert_data(sql):
    global lingolo_cursor
    lingolo_cursor.execute(sql)
    dbconn.commit()
    return str(lingolo_cursor.rowcount) + " rows inserted"


# Disconnecting from the server
#conn.close()
global lingolo_cursor
lingolo_cursor = dbconn.cursor()


#test 1 
sql="select * from `bookmarks` limit 10"
bookmarkres=getarray(sql)

for x in bookmarkres:
    print(x)


#test2 
sql="insert into `evernote` (title, remark, catagory_id, content, created) values ('test', 'no remark', 1, 'ccc', NOW()) "
i_res = insert_data(sql)
print(i_res)

sql="select * from `evernote` order by id DESC limit 1"
print(getarray(sql))

dbconn.close()


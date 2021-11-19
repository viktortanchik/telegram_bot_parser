import sqlite3

con = sqlite3.connect('sqlite_python.db')


def sql_insert_all(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO users VALUES( ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)
    con.commit()

def sql_insert_one(con, entitie):
    cursorObj = con.cursor()
    cursorObj.execute(
    'INSERT INTO users(url_channel) VALUES(?)', entitie)
    con.commit()


def sql_insert_something(con,name, entitie):
    cursorObj = con.cursor()
    names = 'INSERT INTO users('+str(name)+ ') VALUES(?)'
    cursorObj.execute(names, entitie)
    con.commit()

############################################# GET IN DB ##########################################

# поиск ID по URL
def sql_select_id(con,url):
    cursorObj = con.cursor()
    stre =''.join(url)
    query="SELECT * FROM users WHERE url_channel = "+ "'" +str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    return values[0]

#print(sql_select_id(con,name))

# получения  первого имени чата  по ID
def sql_select_original_channel_name(con,id):
    cursorObj = con.cursor()
    stre = ''.join(id)
    query = "SELECT original_channel_name FROM users WHERE UID = " + "'" + str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    #print(values)
    return values[0]


# получения  текущего  имени чата  по ID
def sql_select_previous_channel_names(con,id):
    cursorObj = con.cursor()
    stre = ''.join(id)
    query = "SELECT previous_channel_names FROM users WHERE UID = " + "'" + str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    #print(values)
    return values[0]

#Date_of_submission_to_bot
# получения  даты добавления чата  по ID
def sql_select_Date_of_submission_to_bot(con,id):
    cursorObj = con.cursor()
    stre = ''.join(id)
    query = "SELECT Date_of_submission_to_bot FROM users WHERE UID = " + "'" + str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    #print(values)
    return values[0]

#picture_changed
# Значения id изображения чата по id с базы
def sql_select_picture_changed(con,id):
    cursorObj = con.cursor()
    stre = ''.join(id)
    query = "SELECT picture_changed FROM users WHERE UID = " + "'" + str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    #print(values)
    return values[0]


#How_many_times
# сколько раз менялось изображения чата
def sql_select_How_many_times(con,id):
    cursorObj = con.cursor()
    stre = ''.join(id)
    query = "SELECT How_many_times FROM users WHERE UID = " + "'" + str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    #print(values)
    return values[0]
#
# UID=('19')
# print(sql_select_How_many_times(con,UID))

#Текущее количество пользователей в канале
def sql_select_Current_number_of_users_in_channel(con,id):
    cursorObj = con.cursor()
    stre = ''.join(id)
    query = "SELECT Current_number_of_users_in_channel FROM users WHERE UID = " + "'" + str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    #print(values)
    return values[0]


#Количество пользователей на момент вставки в бота:
def sql_select_number_of_users_at_the_moment_of_insertion_into_the_bot(con,id):
    cursorObj = con.cursor()
    stre = ''.join(id)
    query = "SELECT number_of_users_at_the_moment_of_insertion_into_the_bot FROM users WHERE UID = " + "'" + str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    #print(values)
    return values[0]


# Обновления любого значения
def sql_update(con,set,set_name,where,where_name):
    cursorObj = con.cursor()
    strs = 'UPDATE users SET '+str(set)+' = '+"'"+str(set_name)+"'"+' where '+str(where)  +' = '+str(where_name)
    #'UPDATE users SET original_channel_name = "Rogers" where UID = 2'
    #print(strs)
    cursorObj.execute(strs)
    con.commit()

set = ("original_channel_name")
set_name = ('TEST_UPDATE')
where = ('UID')
where_name =2

#sql_update(con,set,set_name,where,where_name)

# Получения всех значений с базы
def sql_select_all(con):
    cursorObj = con.cursor()
    #stre =''.join(previous_channel_names)
    query="SELECT * FROM users  "  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchmany(-1)
    return values

#urls =sql_select_urls(con)
#print(urls[0][1])

def sql_del(con,name):
    cur = con.cursor()
    query = "DELETE FROM users WHERE url_channel =?"
    cur.execute(query,(name))
    con.commit()


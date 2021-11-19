import sqlite3
try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    sqlite_create_table_query = ("""CREATE TABLE IF NOT EXISTS users(
       
       uid INTEGER PRIMARY KEY AUTOINCREMENT,
       url_channel TEXT ,
       original_channel_name TEXT ,
       previous_channel_names TEXT ,
       Date_of_submission_to_bot TEXT ,
       Current_username TEXT ,
       Edited_usernames TEXT ,
       picture_changed TEXT ,
       How_many_times TEXT ,
       Current_number_of_users_in_channel TEXT ,
       number_of_users_at_the_moment_of_insertion_into_the_bot TEXT ,
       There_is_an_ad_inside TEXT 
       );
    """)
    cursor = sqlite_connection.cursor()
    print("The database is connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("SQLite table created")
    cursor.close()

except sqlite3.Error as error:
    print("Error connecting to sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("SQLite connection closed")
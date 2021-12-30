import mysql.connector


def DatabaseManager():
    def create_database(db):
        db.cursor().execute("CREATE DATABASE SongStorage")
        db.cursor().execute("CREATE TABLE music (id INT, artist VARCHAR(256), album VARCHAR(256), title VARCHAR(256), type VARCHAR(256), path VARCHAR(512))")
        song = 5

    def connect_database():
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password=""
        )
        #Verify if database and table are there
        create_database(mydb)
        return mydb

    def get_songs():
        db = connect_database()
        db.close()

    def add_song():
        db = connect_database()
        db.close()

    def remove_song():
        db = connect_database()
        db.close()

    def get_playlists():
        db = connect_database()
        db.close()

    def update_playlists():
        db = connect_database()
        db.close()

    def create_playlist():
        db = connect_database()
        db.close()

    def remove_playlist():
        db = connect_database()
        db.close()

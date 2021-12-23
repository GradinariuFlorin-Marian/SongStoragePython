import mysql.connector


def DatabaseManager():
    def create_database():
        song = 5

    def connect_database():
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password=""
        )
        return mydb

    def get_songs():
        db = connect_database()

    def add_song():
        db = connect_database()

    def remove_song():
        song = 5

    def get_playlists():
        db = connect_database()

    def update_playlists():
        song = 5

    def create_playlist():
        song = 5

    def remove_playlist():
        song = 5

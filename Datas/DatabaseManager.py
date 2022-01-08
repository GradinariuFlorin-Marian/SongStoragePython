import mysql.connector
from datetime import datetime


def close_database(db):
    db.close()


class DatabaseManager:
    def create_database(self, db):
        db.cursor().execute(
            "CREATE TABLE IF NOT EXISTS songs (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, artist VARCHAR(256), album VARCHAR(256), title VARCHAR(256), path VARCHAR(512))")
        db.cursor().execute(
            "CREATE TABLE IF NOT EXISTS playlists (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256), description VARCHAR(256))")
        db.cursor().execute(
            "CREATE TABLE IF NOT EXISTS logs (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, time DATE, description VARCHAR(256))")

    def connect_database(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database='SongStorage'
        )
        # Verify if database and table are there

        return mydb

    def get_songs(self):
        db = self.connect_database()
        db.close()

    def add_song(self, db, artist, album, title, path):
        mycursor = db.cursor()
        sql = "INSERT INTO songs (artist, album, title, path) VALUES (%s, %s, %s, %s)"
        val = (artist, album, title, path)
        mycursor.execute(sql, val)
        db.commit()

    def remove_song(self, db, id):
        mycursor = db.cursor()
        sql = "DELETE FROM songs WHERE id=%s"
        val = id
        mycursor.execute(sql, val)
        db.commit()

    def update_song(self, db, artist, album, title, id):
        mycursor = db.cursor()
        sql = "UPDATE songs SET artist = %s, album = %s, title = %s WHERE id=%s"
        val = (artist, album, title, id)
        mycursor.execute(sql, val)
        db.commit()

    def get_playlists(self, db):
        db = self.connect_database()

        db.close()

    def update_playlists(self, db):
        db = self.connect_database()

        db.close()

    def create_playlist(self, db):
        db = self.connect_database()

        db.close()

    def remove_playlist(self):
        db = self.connect_database()

        db.close()

    def insert_Log(self, db, desc):
        mycursor = db.cursor()
        sql = "INSERT INTO logs (time, description) VALUES (%s, %s)"
        val = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), desc)
        mycursor.execute(sql, val)
        db.commit()

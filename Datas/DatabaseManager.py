import mysql.connector
from datetime import datetime


class DatabaseManager:
    def create_database(self, db):
        db.cursor().execute(
            "CREATE TABLE IF NOT EXISTS songs (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, artist VARCHAR(256), album VARCHAR(256), title VARCHAR(256), path VARCHAR(512))")
        db.cursor().execute(
            "CREATE TABLE IF NOT EXISTS playlists (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) UNIQUE, description VARCHAR(256))")
        db.cursor().execute(
            "CREATE TABLE IF NOT EXISTS logs (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, time DATE, description VARCHAR(256))")

    def connect_database(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database='SongStorage'
        )

        return mydb

    def get_songs(self, db):
        mycursor = db.cursor()

        mycursor.execute("SELECT id, artist, album, title FROM songs")

        return mycursor.fetchall()

    def get_songsplaylist(self, db, playlistname):
        mycursor = db.cursor()

        mycursor.execute("SELECT idsong FROM " + playlistname)

        mylist = []

        for x in mycursor.fetchall():
            print(x[0])
            mycursor.execute("SELECT id, artist, album, title FROM songs WHERE id=" + str(x[0]))
            mylist.append(mycursor.fetchall())

        return mylist

    def get_path(self, db, idsong):
        mycursor = db.cursor()

        mycursor.execute("SELECT path FROM songs WHERE id=" + idsong)

        return mycursor.fetchall()

    def add_song(self, db, artist, album, title, path):
        mycursor = db.cursor()
        sql = "INSERT INTO songs (artist, album, title, path) VALUES (%s, %s, %s, %s)"
        val = (artist, album, title, path)
        mycursor.execute(sql, val)
        db.commit()

        mycursor.execute("SELECT id FROM songs ORDER BY id DESC LIMIT 1")

        return mycursor.fetchall()

    def add_songplaylist(self, db, idsong, playlist):
        mycursor = db.cursor()
        sql = "INSERT INTO " + playlist + " (idsong) VALUES (%s)"
        val = idsong
        mycursor.execute(sql, val)
        db.commit()

    def remove_songplaylist(self, db, idsong, playlist):
        mycursor = db.cursor()
        sql = "DELETE FROM " + playlist + " (idsong) VALUES (%s)"
        val = idsong
        mycursor.execute(sql, val)
        db.commit()

    def remove_song(self, db, idsong):
        mycursor = db.cursor()
        sql = "DELETE FROM songs WHERE id=" + idsong
        mycursor.execute(sql)
        db.commit()

    def update_song(self, db, artist, album, title, idsong):
        mycursor = db.cursor()
        sql = "UPDATE songs SET artist = %s, album = %s, title = %s WHERE id=%s"
        val = (artist, album, title, idsong)
        mycursor.execute(sql, val)
        db.commit()

    def search_songs(self, db, title):
        mycursor = db.cursor()

        mycursor.execute("SELECT id, artist, album, title FROM songs WHERE title LIKE '%" + title + "%'")

        return mycursor.fetchall()

    def get_playlists(self, db):
        mycursor = db.cursor()

        mycursor.execute("SELECT * FROM playlists")

        return mycursor.fetchall()  # Result in tuple [0] [1] [2]

    def update_playlist(self, db, oldname, name, description):
        mycursor = db.cursor()
        sql = "UPDATE playlists SET name = %s, description = %s WHERE name=%s"
        val = (name, description, oldname)
        mycursor.execute(sql, val)
        sql2 = "RENAME TABLE " + oldname + " TO " + name
        mycursor.execute(sql2)
        db.commit()

    def create_playlist(self, db, name, description):
        mycursor = db.cursor()
        sql = "CREATE TABLE IF NOT EXISTS " + name + " (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, idsong INT)"
        mycursor.execute(sql)
        sql2 = "INSERT INTO playlists (name, description) VALUES (%s, %s)"
        val2 = (name, description)
        mycursor.execute(sql2, val2)
        db.commit()

    def remove_playlist(self, db, namep):
        mycursor = db.cursor()
        sql = "DELETE FROM playlists WHERE name = '" + namep + "'"
        mycursor.execute(sql)
        sql2 = "DROP TABLE " + namep
        mycursor.execute(sql2)
        db.commit()

    def insert_Log(self, db, desc):
        mycursor = db.cursor()
        sql = "INSERT INTO logs (time, description) VALUES (%s, %s)"
        val = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), desc)
        mycursor.execute(sql, val)
        db.commit()

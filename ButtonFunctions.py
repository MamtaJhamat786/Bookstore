import sqlite3
class Database:
    def __init__(self, db):
        self.conn=sqlite3.connect("bookstore.db")
        self.cursor=self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS BookStore( id INTEGER PRIMARY KEY , title TEXT, author TEXT, year INT, isbn INT)") 
        self.conn.commit()
        
    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT into BookStore VALUES(NULL, ?, ?, ?, ?)",( title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM BookStore")
        rows=self.cursor.fetchall()
        return rows
        
    def search(self,title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM BookStore WHERE title = ? OR author = ? OR year = ? "
                    "OR isbn = ?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows
    
    def delete(self, id):
        self.cursor.execute("DELETE FROM BookStore WHERE id=?", (id,) )
        self.conn.commit()


    def update(self,id, title, author, year, isbn):
        self.cursor.execute("UPDATE BookStore SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()
        
    def close(self):
        self.conn.close()

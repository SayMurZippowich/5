import sqlite3


class Data():
    def litewrite(self, xcor, ycor):

        con = sqlite3.connect('Coord.db')
        cur = con.cursor()
        (cur.execute('CREATE TABLE IF NOT EXISTS Coord (x INTEGER , y INTEGER)'))
        con.commit()
        cur.execute('INSERT INTO Coord (x, y) VALUES(?, ?)', (xcor, ycor))
        con.commit()
        con.close()

    def getxinputs(self):
        con = sqlite3.connect('Coord.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Coord')
        xinput = []
        for row in cur:
            xinput.append(row[0])
        con.close()
        return xinput

    def getrows(self):
        Data.i = 0
        con = sqlite3.connect('Coord.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Coord')
        xinput = []
        for row in cur:
            Data.i += 1
        con.close()
        return Data.i

    def getyinputs(self):
        con = sqlite3.connect('Coord.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Coord')
        yinput = []
        for row in cur:
            yinput.append(row[1])
        con.close()
        return yinput

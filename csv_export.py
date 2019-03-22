import sqlite3

con = sqlite3.connect("h.db")
cur = con.cursor()
 
print("\n".join(
    "{},{}".format(ts, v)
    for ts, v in cur.execute(
        "SELECT timestamp, value FROM History ORDER BY timestamp DESC LIMIT 60;"
    ).fetchall()
))


import serial
import serial.tools.list_ports
import os
import sqlite3
import time

enva = os.environ.get("ARDUINO")

if enva is None:
    devs = [a.device for a in serial.tools.list_ports.comports() if a[2] != "n/a"]
    assert len(devs) == 1, "Incorrect number of devices found"
else:
    devs = [enva]

s = serial.Serial(devs[0])

con = sqlite3.connect("h.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS History(timestamp INTEGER PRIMARY KEY, value INTEGER)"
)

nt = (time.time()) + 1
while True:
    b0 = int.from_bytes(s.read(), "little")

    if time.time() < nt:
        continue
    else:
        nt = time.time() + 1

    print(bin(b0)[2:].zfill(8))

    cur.execute(
        "INSERT INTO History (timestamp, value) VALUES (?, ?)", (int(time.time()), b0)
    )
    con.commit()

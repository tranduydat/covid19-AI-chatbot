import sqlite3
conn = sqlite3.connect('./database.db')
c = conn.cursor()

# Get data
c.execute("SELECT dg.'9/21/20' FROM Death_Global dg WHERE dg.'Country/Region' = 'Vietnam'")
result = c.fetchone()

print(str(result[0]))
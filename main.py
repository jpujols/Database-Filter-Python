import sqlite3
import pandas

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close
print(rows)

for i in rows:
  print(i[0])

#Database to CSV Converter
  df = pandas.Dataframe.from_records(rows)
  df.columns = ["Rank", "Country", "Area", "Population"]
  df.to_csv("countries_big_area.csv", index=False)

#CSV to Database Convertr
data = pandas.read_csv("countries_big_area.csv")
conn = sqlite3.connect('database.db')
cur = conn.cursor()
for index, row in data.iterrows():
  print(row["Country"], row["Area"])
  cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row,["Country"], row["Area"]))
  conn.commit()
  conn.close()
  
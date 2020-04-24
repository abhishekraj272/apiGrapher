import csv, sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

with open('StormScrapedData.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Topology'], i['Component'], i['ExecuteLatency'], i['Capacity']) for i in dr]

cur.executemany("INSERT INTO api_topologies (topology, component, latency, capacity) VALUES (?, ?, ?, ?);", to_db)
con.commit()
con.close()
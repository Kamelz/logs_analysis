#!/usr/bin/env python3

import connection

db = connection.DB('news', 'postgres', 'localhost')
file = open('output.txt', 'w')


file.write("1. What are the most popular three articles of all time? \n\n")
rows = db.query("""SELECT title ,(SELECT COUNT(*) FROM log
WHERE SUBSTRING(path,10) = slug) as cnt FROM articles
ORDER BY cnt DESC LIMIT 3""")

for row in rows:
    file.write('"%s" — %s views \n' % (row[0], row[1]))

file.write("\n-------------------------------------------- \n")
file.write("2. Who are the most popular article authors of all time? \n\n")
rows = db.query("""
SELECT name ,(SELECT COUNT(*) FROM log WHERE SUBSTRING(path,10) = slug)
as cnt FROM authors JOIN articles ON articles.author = authors.id ORDER
BY cnt DESC""")


for row in rows:
    file.write('%s — %s views \n' % (row[0], row[1]))


file.write("\n-------------------------------------------- \n")
file.write("3. On which days did more than 1% of requests lead to errors?")
file.write("\n\n")

rows = db.query("""SELECT to_char(time,'Mon dd,YYYY')
as year,COUNT(*)::decimal /(SELECT COUNT(*)::decimal FROM log)
*100 FROM log WHERE status !='200 OK' GROUP
BY year""")

for row in rows:
    file.write("%s — %s%s errors \n" % (row[0], round(row[1], 2), "%"))


file.close()

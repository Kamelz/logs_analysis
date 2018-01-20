#!/usr/bin/env python3

import connection

db = connection.DB('news', 'postgres', 'localhost')
file = open('output.txt', 'w')


file.write("1. What are the most popular three articles of all time? \n\n")
rows = db.query("""select title ,(select count(*) from log
where SUBSTRING(path,10) = slug) as cnt from articles
order by cnt desc limit 3""")

for row in rows:
    file.write('"%s" — %s views \n' % (row[0], row[1]))

file.write("\n-------------------------------------------- \n")
file.write("2. Who are the most popular article authors of all time? \n\n")
rows = db.query("""
select name ,(select count(*) from log where SUBSTRING(path,10) = slug)
as cnt from authors join articles on articles.author = authors.id order
by cnt desc""")

for row in rows:
    file.write('%s — %s views \n' % (row[0], row[1]))


file.write("\n-------------------------------------------- \n")
file.write("3. On which days did more than 1% of requests lead to errors?")
file.write("\n\n")

rows = db.query("""select to_char(time,'Mon dd,YYYY')
as year,count(*)::decimal /(select count(*)::decimal from log)
*100 from log where status !='200 OK' group
by year""")

for row in rows:
    file.write("%s — %s%s errors \n" % (row[0], round(row[1], 2), "%"))


file.close()

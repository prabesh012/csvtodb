import csv
import sqlite3

conn = sqlite3.connect('test.db')
print("connection established ",conn)
CREATE_TABLE = f"""CREATE TABLE IF NOT EXISTS students 
                    (
                        name text,
                        rollno int,
                        age int
                    );
                """    
cur = conn.cursor()
cur.execute(CREATE_TABLE)

with open('class.csv','r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        print(row)
        INSERT_SQL = f"""INSERT INTO students(name,rollno,age) VALUES(?,?,?)"""
        cur.execute(INSERT_SQL,row)
        conn.commit()


print("Done")


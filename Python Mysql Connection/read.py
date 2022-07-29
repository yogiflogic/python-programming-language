from database import db

sql = "SELECT username, no_hp FROM sigupuser WHERE username='yogifernando'"

mycursor = db.cursor()
mycursor.execute(sql)

result = mycursor.fetchall()
for x in result:
    print(x)

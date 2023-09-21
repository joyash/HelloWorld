import mysql.connector

mydb = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'xenun333',
    autocommit = True
)

area_code = input("Enter your desired area code:  ")
sql = ("select name,type, iso_country from airport where iso_country = 'FI' order by type;")
mycursor = mydb.cursor()
mycursor.execute(sql)
results = mycursor.fetchall()
if results:
    for name, type, iso_country in results:
        if area_code == iso_country:
            print(f"{name}: {type}")
else:
    print("Invalid error")

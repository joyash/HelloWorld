import mysql.connector

#established a connection to your database

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "flight_game",
    user = "root",
    password = "xenun333",
    autocommit = True
)

# get the country code from the user
icao = input("Enter the ICAO code: ")
#define the sol query
sql = ("select ident, name, municipality as location from airport;")
#execute the query with the provided country code
# create a cursor
mycursor = mydb.cursor()
mycursor.execute(sql)
#Fetch the results
results = mycursor.fetchall()
#check if any results were found
if results:
    print(f"Airports in country  by type: ")
    for ident, name, location in results:
        if icao == ident:
            print(f"{icao}: {name}, {location}.")
else:
    print(f"No airports found in.")
mycursor.close()
mydb.close()

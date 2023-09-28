# question 1 answer
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


# question 2 answer
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
sql = ("select name,type, iso_country from airport order by type;")
mycursor = mydb.cursor()
mycursor.execute(sql)
results = mycursor.fetchall()
if results:
    for name, type, iso_country in results:
        if area_code == iso_country:
            print(f"{name}: {type}")
else:
    print("Invalid error")

mycursor.close()
mydb.close()


# question 3 answer
import mysql.connector
from geopy.distance import geodesic
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    database = "flight_game",
    password = "xenun333",
    autocommit = True
    )

cursor = mydb.cursor()
icao = input("Enter your first icao code: ")
icao1 = input("Enter your second icao code: ")
cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{icao}';")
cord = cursor.fetchone()
cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{icao1}';")
cord1 = cursor.fetchone()

if cord is None or cord1 is None:
    print("Airport not found in database")
else:
    lat1, lon1 = cord
    lat2, lon2 = cord1
    airport1 = (lat1, lon1)
    airport2 = (lat2, lon2)
    distance = geodesic(airport1, airport2).kilometers
    print(f"the distance between {icao} and {icao1} is {distance} kilometers.")

mydb.close()
cursor.close()
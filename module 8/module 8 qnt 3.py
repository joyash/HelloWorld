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
"""import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='xenun333',
    autocommit=True
)
icao_code = input("Enter ICAO code: ")
sql = ("select distinct airport.name, game.location from airport,game where airport.ident like '%EFHK%'")
mycursor = mydb.cursor()
mycursor.execute(sql,icao_code)
for x in mycursor.fetchall():
   print(x)



"""
"""def my_function(side1,side2):
    perimeter = (side1 + side2) * 2
    return perimeter


side1 = 8
side2 = 6
perimeter = my_function(side1,side2)
print(f"The side of rectangle are {side1} and {side2} ")
print(f"The perimeter of the rectangle is {perimeter}")

"""
"""def odd_numbers(numbers):
    odd_numbers = []
    for count in numbers:
        if count % 2 != 0:
            odd_numbers.append(count)
    return odd_numbers


numbers = [12, 5, 21, 4, 8, 0, 11]
odd_numbers = odd_numbers(numbers)
print("Original numbers : " + str(numbers))
print("Odd_numbers: " + str(odd_numbers))"""

"""def greet(name = "ggggg"):
    print(name)


greet( "rohan")
greet()"""


def my_fruits(food):
    for x in food:
        print(x)


"""fruits = ["apple", "banana", "orange"]
fruits.append("leamon")
my_fruits(fruits)

"""
"""def my_function(x):
    y = 5 * x
    return y
print(my_function(3))

my_function(2)
my_function(4)
"""
"""print("yes") if 5 > 2 else print("no")

user1 = int(input("Enter a number:  "))
user2 = int(input("Enter a number: "))
if user1 > user2:
    print(f"{user1} is greater than {user2}")
else:
    print(f"{user2} is greater than {user1}")

"""
"""user = int(input("How much do you want to buy, 1 unit cost 100: "))
total = user * 100
discount = total * 0.1
new_total = total - total * 0.1
if total > 1000:
    print(f"Your total amount is {total} discount amount is {discount} and your amount after discount is {new_total}")
else:
   print(f"your total amount is {total}")

"""
"""user1 = int(input("Enter your age: "))
user2 = int(input("Enter your age: "))
user3 = int(input("Enter your age: "))
if user1 > user2 and user1 > user3:
    oldest = user1
    print(f"{user1} is oldest")
elif(user2 > user3):
     print(f"{user2} is oldest")
else:
   print(f"{user3} is oldest")
if user1 < user2 and user1 < user3:
    oldest = user1
    print(f"{user1} is youngest")
elif(user2 < user3):
     print(f"{user2} is youngest")
else:
   print(f"{user3} is youngest")"""

"""list = []
user1 = int(input("Enter your age: "))
list.append(user1)
user2 = int(input("Enter your age: "))
list.append(user2)
user3 = int(input("Enter your age: "))
list.append(user3)
list.sort()
print(f"oldest is {list[-1]}")
print(f"youngest is {list[0]}")
"""
"""user_year = int(input("Enter your year:  "))
if(user_year % 4 == 0 ) and (user_year % 400 == 0):
  print(f"The year {user_year} is a leap year.")
else:
 print(f"The year {user_year} is not a leap year.")
"""

"""def sumof_list(list1,total_number):
    for count in list1:
       total_number[0] += count
    return total_number[0]


total_number = [0]
list1 = [2,5,8]
total_number = sumof_list(list1,total_number)
print(total_number)

"""
"""
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

"""

import mysql.connector

db_connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    database="flight_game_team12",
    password="xenun333",
    autocommit=True
)

# Establish a database connection
db_connection = mysql.connector.connect(

    # Create a cursor to interact with the database
    cursor=db_connection.cursor()

# Fetch and display airplane information
cursor.execute("select type, size, capacity, co2_emission_per_km, max_range FROM airplane")
airplanes = cursor.fetchall()

print("Available airplanes:")
for airplane in airplanes:
    print(
        f"Type: {airplane[0]}, Size: {airplane[1]}, Capacity: {airplane[2]}, CO2 Emission per km: {airplane[3]}, Max Range: {airplane[4]}")

# Prompt the user for their choice
user_choice = input("Enter the type of airplane you want to choose: ")

# Fetch player ID (replace 'test_player' with the actual player's name)
player_name = 'test_player'  # Change to the appropriate player's name
cursor.execute("SELECT id FROM player WHERE player_name = %s", (player_name,))
player_record = cursor.fetchone()

if player_record:
    player_id = player_record[0]

# Update the choice table with the user's selection and player_id
insert_query = "INSERT INTO choice (player_id, plane_type) VALUES (%s, %s)"
cursor.execute(insert_query, (player_id, user_choice))
db_connection.commit()

print(f"Choice recorded for player with ID {player_id}")
else:
print("Player not found. Please check the player name.")

# Close the database connection
cursor.close()
db_connection.close()

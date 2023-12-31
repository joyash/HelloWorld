# Print First 10 natural numbers using while loop

"""natural_number = 0
while natural_number != 11:
    print(natural_number)
    natural_number += 1
else:
    print("Program end.")"""

# Write a program to print the following number pattern using a loop.

"""n = 6
i = 0
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i += 1

"""
"""using a while loop, len function, an if statement and the str() function; iterate through the given list and if 
there is a 100, assign a notification to the variable my_message with the index of 100."""

"""list = [10, 99, 44,76,89,54,23,76,91,12,32,65,100,76,54,9]
my_message = "There is a 100 at index no: "
count = 0
while count < len(list):
    if list[count] == 100:
        print(f"there is a 100 at index no: {count}")
    count  += 1
print(f"Total count was {count}. ")
"""

# write a program to print multiplication table of a given number.

"""import mysql.connector

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
            break
    else:
      print("Invalid error")

mycursor.close()
mydb.close()"""

"""n = 0
for outer in range(3, 0, -1):
    m = 0
    for inner in [2, 0, 2, 3]:
        if(outer == inner):
            m += 1
        n += 1
    print(m)
print(n)"""

"""import random
def castdice(dice, face):
    total = 0
    for cast in range(dice):
        total = total + random.randint(1, face)
    return total

dice = int(input("how many dice to throw"))
face = int(input("how many face"))
total = castdice(dice, face)
print(f"the total is {total}")
"""
"""n= 2
for i in (2,0):
    for j in range(1,11):
        result = i * j
        print(f"{i} * {j} = {result}")
    break
"""
"""total = 0
for i in range(2,22):
    if i % 2 == 0:
        total = total + i
        print(f"{i} + {total - i} = {total}")"""

"""list1 = ['rrrr', 'ffff', 'ggg', 'eee', 'qqq']
list1.append('xxx')
list1.remove('ffff')
list1.insert(2, 'lll')
print(list1)
list2 = ['111', '222']
list1.extend(list2)
print(list1)
print(list1.index('111'))
print(list1[3])
"""

"""address = {
    'Rabin' : 'Nepal',
    'Mike' : 'America',
    'Juan' : 'Spain',
}
address['Olga'] = 'Suomi'
address['Rajesh'] = 'India'
del address['Rabin']
print(address)

name = input("Enter a name: ")
 if name in address:
    print(f"{name} lives in {address[name]}")
else:
    print("Enter a valid key")
"""
"""numbers = [1, 1, 1, 1, 3]
for i in numbers:
    for j in range(i):
        print("£", end="  ")

    print("")"""

"""list = [255,4,777657,18,1,8,3008,9]
border = (5, 15)
for count in list:
    if count > new_mew:
        new_mew = count
print(f"Highest number is in index {list.index(new_mew)}")
print(f"Number {count} is in index {list.index(count)} in list")"""

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game_team12_mysql',
    user='root',
    password='hyonee',
    autocommit=True
)


# BACKEND functions start here ----------------
def get_airport_info(icao):
    sql = f'''SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


# Riina's code
def create_player():
    while True:
        name = input("Enter name: ")

        sql = f"SELECT player_name FROM player WHERE player_name = '{name}' "
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if cursor.rowcount == 0:
            co2_budget = 100000000
            co2_consumed = 0
            total_travelled = 0
            sql2 = f"INSERT INTO player(player_name,co2_budget,co2_consumed,total_travelled)VALUES (%s,%s,%s,%s)"
            val = [name, co2_budget, co2_consumed, total_travelled]
            cursor = connection.cursor()
            cursor.execute(sql2, val)
            cursor.fetchall()
            break

        else:
            print("Player already exists!")

    print(f"\nWelcome traveller, {name}! ")

    return name


# Rabin's code (modified)
def show_and_choose_airplane():
    mycursor = connection.cursor()
    mycursor.execute("select type, size, capacity, co2_emission_per_km, max_range FROM airplane")
    results = mycursor.fetchall()

    print("Please choose your airplane: ")
    for idx, row in enumerate(results, start=1):
        print(f"{idx}. {row[0]}")

    choice = int(input("Your choice?(1-4): "))
    if choice == 1:
        return "large_airport"
    elif choice == 2:
        return "medium_airport"
    elif choice == 3:
        return "heliport"
    elif choice == 4:
        return "small_airport"


def calculate_distance(current, target):
    from geopy import distance

    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km


def get_userdata(userid):
    sql = f'''SELECT player_name, co2_budget, co2_consumed, total_travelled FROM player WHERE player_name = %s
                '''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (userid,))
    result = cursor.fetchone()
    return result


def left_budget(userid):
    data = get_userdata(userid)
    return data['co2_budget'] - data['co2_consumed']


def range_in(airplane_size, userid, current='EFHK'):
    global airportCode, range, co2_emission

    sql = f'''SELECT ident, airport.name, airport.continent, country.name as country, airplane.max_range, airplane.co2_emission_per_km, airplane.capacity
            FROM airport 
            INNER JOIN airplane on (airplane.size = airport.type)
            INNER JOIN country on (airport.iso_country = country.iso_country)
            WHERE airport.type = '{airplane_size}' ORDER BY RAND () LIMIT 5'''
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\nHere are possible destinations you can choose!\n")
    print("continent |  country  |      airport      |  distance  | expected co2 emission")
    print("-----------------------------------------")
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1):
            # print(f"{row[0]}")
            airportCode = row[0]
            range = row[4]
            distance = calculate_distance(current, airportCode)
            co2_emission = distance * row[4] / row[5]

            if (range > distance) and (co2_emission < left_budget(userid)):
                print(f"{index}   |  {row[2]}    | {row[3]} | {row[1]} | {round(distance)} km | {round(co2_emission)}")

    return


def condition_checker(userid):
    global co2_budget, co2_consumed

    sql = f"SELECT co2_budget, co2_consumed FROM player WHERE player_name = '{userid}'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 1:
        for row in result:
            co2_budget = row[0]
            co2_consumed = row[1]
    co2_left = co2_budget - co2_consumed
    if co2_left <= 0:

        return game_over_and_save(userid)
    else:
        return
    # weak logic. need to improve later on.


def game_over_and_save(userid):
    global name, score
    sql1 = f"SELECT player_name, total_travelled FROM player WHERE (co2_budget <= co2_consumed) AND (player_name = '{userid}')"
    # print(sql1)
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    if cursor.rowcount == 1:
        for row in result:
            print(f"{row[0]}, You cannot fly with the remaining budget anywhere. GAME OVER!")
            name = row[0]
            score = row[1]
    save = input("Do you want to save your score in score board? (y/n): ")
    if save == 'y':
        sql2 = f"INSERT INTO scoreboard (player_name, score) VALUES (%s, %s)"
        val = [name, score]
        cursor = connection.cursor()
        cursor.execute(sql2, val)
        print(f"your userid <{name}> and your score <{score}> has been saved in the scoreboard.")
    return


def show_scoreboard():
    sql = "SELECT * FROM scoreboard ORDER BY score DESC LIMIT 50"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        print(f"<<<SCORE BOARD>>>")
        print(f"Player      | score")
        print(f"--------------------------")
        for row in result:
            print(f"{row[1]} | {row[2]}")
        return


def show_panel(userid):
    sql2 = f"SELECT co2_budget, co2_consumed, total_travelled FROM player where player_name = '{userid}'"
    cursor = connection.cursor()
    cursor.execute(sql2)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print("<<Your status>>")
            print("-------------------------------------")
            print(f"|co2_budget              | {row[0]}|")
            print(f"|co2_consumed            | {row[1]}|")
            print(f"|total distance travelled| {row[2]}|")
            print("-------------------------------------")
    return


# FRONT END(ish) FUNCTIONS & CODES START HERE-------------------
def main_display(userid):
    main_processing = True
    while main_processing:
        sql1 = f"SELECT COUNT(player_id) FROM choice WHERE player_id = '{userid}'"
        cursor = connection.cursor()
        cursor.execute(sql1)
        result = cursor.fetchall()
        if cursor.rowcount == 1:
            for row in result:
                print(f"ROUND {row[0] + 1}")
                print("\n")

        show_panel(userid)
        condition_checker(userid)

        airplane = show_and_choose_airplane()
        range_in(airplane, userid)
        main_processing = False

    print("\n\n from here continue : ask the player his/her decision and double check=--------`...")
    print("\n\n up in the air...")
    print("\n\n 'you've got a message from control tower!' (If event occurs)")
    print("\n\n calculate the final co2_spent and update the data to choice table")
    print("\n\n 'Now it's landing....")

    return


def front_display():
    initial = True
    while initial:
        print("----------------------")
        print("|  NAME OF THE GAME  |")
        print("|                    |")
        print("----------------------")
        print("\n")
        print("1: START A NEW GAME")
        print("2: CHECK TUTORIAL")
        print("3: SCORE BOARD")
        print("4: QUIT")
        print("\n")

        command = int(input("Enter your command: "))
        if command == 1:
            print("Your adventure is about to start,")
            name = create_player()
            print("Your journey begins at Helsinki-Vantaa airport, Finland.\n")

            main_display(name)
            condition_checker(name)

            initial = False

        elif command == 2:
            print("<<TUTORIAL>>")
            print("\n")
            print("You're going to travel across the world by choosing a flight.")
            print("Your GOAL is to travel as far as you can go with your limited co2 budget!")
            print("The game ends when you have spent all the budget and can't go anywhere anymore.")
            print("Good luck!")
            print("\n")
            print("Going back to the front page...")
            print("\n")

        elif command == 3:
            show_scoreboard()
            print("\n")
            print("Going back to the front page....")
            print("\n")
            print("\n")
        elif command == 4:
            print("Bye bye!")
            initial = False
        else:
            print("Invalid command. Please try again!")


# only for test. needs to be change later on when merging all the functions.
front_display()

exit_process = True

while exit_process:
    toScoreboard = input("Do you want to go check score board? (y/n) : ")
    if toScoreboard == 'y':
        show_scoreboard()
        toFrontPage = input("By hitting enter, you'll go back to the front page.: ")
        if toFrontPage == '':
            front_display()
        exit_process = False
    elif toScoreboard == 'n':
        toFrontPage = input("By hitting enter, you'll go back to the front page.: ")
        if toFrontPage == '':
            front_display()
        exit_process = False
    else:
        print("Invalid answer. Try again.")

import mysql.connector

# Establish a MySQL database connection
mydb = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='company',
    user='root',
    password='xenun333',
    autocommit=True
)


def check_user(client_id):
    sql = "SELECT client_id FROM client where client_id = %s"
    mycursor = mydb.cursor()
    mycursor.execute(sql, (client_id,))
    result = mycursor.fetchone()
    return result is not None


def is_valid_name(name):
    return name.isalpha()


def insert_client(new_client_id, new_client_name, new_branch_id):
    sql = "INSERT INTO client (client_id, client_name, branch_id) values (%s, %s, %s)"
    values = (new_client_id, new_client_name, new_branch_id)
    mycursor = mydb.cursor()
    mycursor.execute(sql, values)
    if mycursor.rowcount == 1:
        print("status updated")


while True:
    new_client_id = input("Enter your client id(Press Enter to exit):  ")
    if new_client_id == "":
        break
    if not new_client_id.isdigit():
        print("Invalid input for client id. Please enter a valid client id.")
        new_client_id = input("Enter a new client id or press Enter to exit: ")
        if new_client_id == "":
            break
    new_client_id = int(new_client_id)
    while check_user(new_client_id):
        print(f"User with client_id {new_client_id} already exist.")
        new_client_id = input("Enter a new client id or press Enter to exit: ")
        if new_client_id == "":
            break
        if not new_client_id.isdigit():
            print("Invalid input for client id. Please enter a valid client id: ")
            continue
        new_client_id = int(new_client_id)
    if new_client_id == "":
        break

    while True:
        new_client_name = input("Enter your name: ")
        if new_client_name == "":
            break
        if is_valid_name(new_client_name):
            break
        else:
            print("Invalid input for name.Please enter a valid name consist a-z letter only")

    new_branch_id = input("Enter your branch id: ")
    insert_client(new_client_id, new_client_name, new_branch_id)

mydb.close()

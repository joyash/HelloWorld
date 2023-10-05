from geopy.distance import great_circle
import sqlite3

# Connect to the SQLite database containing airport data
conn = sqlite3.connect('your_database_file.db')  # Replace with your actual database file name
cursor = conn.cursor()


# Function to fetch airport coordinates from the database
def fetch_airport_coordinates(icao):
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airports WHERE ident=?", (icao,))
    row = cursor.fetchone()
    if row:
        return row
    else:
        return None


# Function to calculate distance between two airports
def calculate_distance(coord1, coord2):
    if coord1 is not None and coord2 is not None:
        distance = great_circle(coord1, coord2).kilometers
        return distance
    else:
        return None


# Main program
if __name__ == "__main__":
    # Get ICAO codes from the user
    icao1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    # Fetch coordinates from the database
    coord1 = fetch_airport_coordinates(icao1)
    coord2 = fetch_airport_coordinates(icao2)

    # Calculate and print the distance
    distance = calculate_distance(coord1, coord2)
    if distance is not None:
        print(f"The distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    else:
        print("Invalid ICAO codes or airport not found in the database. Please check your input.")

    # Close the database connection
    conn.close()

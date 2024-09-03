import mysql.connector
import json


def menu():
    print("[1] Insert data")
    print("[2] View all data")
    print("[3] Get rank")
    print("[4] Update score")
    print("[5] Delete one record")
    print("[6] Calculate Average SAT Score")
    print("[7] Filter records by Pass/Fail Status.")
    print("[8] Put the inserted data in json format in a file.")
    print("[0] Exit program")


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin123!",
        database="sat_scores"
    )


def close_connections(db, cursor):
    db.close()
    cursor.close()


def insert_data(db, cursor):
    name = input("Enter name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    country = input("Enter country: ")
    pincode = input("Enter pincode: ")
    sat_score = input("Enter sat_score: ")
    passed = "Pass" if (int(sat_score)/1600) > 0.3 else "Fail"
    command = "INSERT INTO scores (name, address, city, country, pincode, SAT_score, PASSED) VALUES (\'" + name + "\',\'" + address + "\',\'" + city + "\',\'" + country + "\'," + pincode + "," + sat_score + ",\'" + passed + "\')"
    try:
        print("Inserting data...")
        cursor.execute(command)
        db.commit()
        print("Successfully inserted data")
    except:
        print("Insertion failed")


def view_data(db):
    t_cursor = db.cursor(dictionary=True)
    t_cursor.execute("SELECT * FROM scores")
    rows = t_cursor.fetchall()
    json_data = json.dumps(rows, indent=4)
    print(json_data)
    t_cursor.close()


def get_rank(cursor):
    person = input("Enter name: ")
    query = "SELECT name, RANK() OVER (ORDER BY SAT_score DESC) FROM scores"
    cursor.execute(query)
    print("Getting rank...")
    for x in cursor:
        if x[0] == person:
            print(f"Rank of {person} is {x[1]}")


if __name__ == "__main__":
    option = None
    db = connect_to_database()
    cursor = db.cursor()
    while option != 0:
        menu()
        try:
            option = int(input("Enter the option: "))
        except:
            print("Invalid input")
            input("Press enter to continue\n")
            continue
        match option:
            case 0:
                print("Exiting program...")
                break
            case 1:
                insert_data(db, cursor)
            case 2:
                print("Viewing all data...")
                view_data(db)
            case 3:
                get_rank(cursor)
            case 4:
                print("Updating score...")
            case 5:
                print("Deleting record...")
            case 6:
                print("Calculating average SAT score...")
            case 7:
                print("Filtering records by Pass/Fail Status...")
            case 8:
                print("Putting inserted data in json format...")
            case _:
                print("No such option available")
        option = input("Press enter to continue, 0 to exit\n")
        if option == "0":
            print("Exiting program...")
            break
    close_connections(db, cursor)

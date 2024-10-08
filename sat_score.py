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
    print("Viewing all data...")
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


def update_score(db, cursor):
    person = input("Enter name: ")
    new_score = input("Enter_new_score: ")
    query = f"UPDATE scores SET SAT_score = {new_score} WHERE name = '{person}'"
    try:
        print("Updating score...")
        cursor.execute(query)
        db.commit()
        print("Update successful")
    except:
        print("Update failed")


def delete_row(db, cursor):
    person = input("Enter name: ")
    query = f"DELETE FROM scores WHERE name = '{person}'"
    try:
        print("Deleting...")
        cursor.execute(query)
        db.commit()
        print("Successfully deleted entry")
    except:
        print("Failed to delete")


def get_avg_score(cursor):
    query = "SELECT AVG(SAT_score) FROM scores"
    cursor.execute(query)
    print("Average score is:",cursor.fetchone()[0])


def filter_record(db):
    t_cursor = db.cursor(dictionary=True)
    print("PASSED\n")
    query = "SELECT * FROM scores WHERE PASSED = \'Pass\'"
    t_cursor.execute(query)
    rows = t_cursor.fetchall()
    json_data = json.dumps(rows, indent=4)
    print(json_data)
    print("\nFAILED\n")
    query = "SELECT * FROM scores WHERE PASSED = \'Fail\'"
    t_cursor.execute(query)
    rows = t_cursor.fetchall()
    json_data = json.dumps(rows, indent=4)
    print(json_data)
    t_cursor.close()


def write_table_to_file(cursor):
    query = "SELECT * FROM scores"
    cursor.execute(query)
    results = cursor.fetchall()
    file_name = "scores.json"
    with open(file_name, "w") as f:
        if results:
            print("Writing to file")
            f.write(str(results))
            print("Write successful")
        else:
            print("No data available")


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
                view_data(db)
            case 3:
                get_rank(cursor)
            case 4:
                update_score(db, cursor)
            case 5:
                delete_row(db, cursor)
            case 6:
                get_avg_score(cursor)
            case 7:
                filter_record(db)
            case 8:
                write_table_to_file(cursor)
            case _:
                print("No such option available")
        option = input("Press enter to continue, 0 to exit\n")
        if option == "0":
            print("Exiting program...")
            break
    close_connections(db, cursor)

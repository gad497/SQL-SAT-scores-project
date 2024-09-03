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


if __name__ == "__main__":
    option = None
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
                print("Inserting data...")
            case 2:
                print("Viewing all data...")
            case 3:
                print("Getting rank...")
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

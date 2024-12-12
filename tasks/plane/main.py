from Plane import Plane, Passenger, Baggage, Crew

def build_plane():
    plane_name = str(input('Enter plane name: '))
    plane = Plane(plane_name)
    plane_rows = int(input('Enter number of rows: '))
    plane_cols = int(input('Enter number of columns: '))
    plane.build_seats(rows = plane_rows, cols = plane_cols)

    return plane


def add_passengers(plane):
    """ Add passengers to the plane
    Parameters:
        plane (Plane): The plane object
    Returns:
        Plane: The plane object with passengers added
    """
    passenger_count = int(input('Enter number of passengers: '))

    for i in range(passenger_count):
        passenger_name = str(input(f'Enter name of passenger {i+1}: '))
        try:
            baggage_weight = int(input(f'Enter baggage weight of passenger {i+1} in kg: '))
            baggage = Baggage(baggage_weight)
            passenger = Passenger(passenger_name, baggage)
        except ValueError:
            passenger = Passenger(passenger_name)
        plane.add_passenger(passenger)

    return plane


def start_dashboard(plane):
    print("\n")
    print("-----------------------------------------------")
    print("Welcome to the Plane Dashboard!")
    print("1. Board crewmember")
    print("2. Add passengers")
    print("3. Print status")
    print("4. Start plane")
    print("5. Land plane")
    print("6. Exit")

    choice = input("Enter choice: ")
    print("\n")
    match choice:
        case "1":
            try:
                name = str(input("Enter crew member name: "))
                crew_type = int(input("Enter 1 for pilot, 2 for cabin crew: ")) 

                if crew_type not in [1, 2]:
                    raise ValueError
                elif crew_type == 1:
                    crew = Crew(name, True)
                else:
                    crew = Crew(name, False)

                plane.add_crew(crew)
            except ValueError:
                print("Invalid input! Please enter a number.")
                start_dashboard(plane)
        case "2":
            plane = add_passengers(plane)
        case "3":
            plane.get_status()
        case "4":
            plane.start_plane()
        case "5":
            plane.land_plane()
            exit()
        case "6":
            exit()
        case _:
            print("Invalid choice! Please enter a valid choice.")

    if choice != "6":
        start_dashboard(plane)


def main():
    plane = build_plane()

    start_dashboard(plane)


if __name__ == "__main__":
    main()

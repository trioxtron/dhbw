class Person:
    def __init__(self, name: str):
        self.name = name

class Baggage:
    def __init__(self, weight: int):
        self.weight = weight

    def get_weight(self):
        """ Get the weight of the baggage
        Returns:
            int: The weight of the baggage
        """
        return self.weight

class Crew(Person):
    def __init__(self, name: str, pilot: bool):
        super().__init__(name)
        if pilot:
            self.role = "Pilot"
        else:
            self.role = "Cabin Crew"

class Passenger(Person):
    def __init__(self, name, baggage = None):
        super().__init__(name)
        self.baggage = baggage

    def get_baggage_weight(self):
        """ Get the weight of the passenger's baggage
        Returns:
            int: The weight of the baggage
        """
        if self.baggage:
            return self.baggage.get_weight()
        return 0

class Plane:
    def __init__(self, name: str):
        self.name = name
        self.passengers = []
        self.pilots = []
        self.cabin_crew = []
        self.seats = []
        self.flying = False

    def add_passenger(self, passenger: Passenger):
        """ Add a passenger to the plane
        Parameters:
            passenger (str): The name of the passenger
        """
        self.passengers.append(passenger)
        for row in self.seats:
            for i, seat in enumerate(row):
                if seat is None:
                    row[i] = passenger
                    return

    def add_crew(self, crew: Crew):
        """ Add a crew member to the plane
        Parameters:
            crew (str): The name of the crew member
        """
        if crew.role == "Pilot":
            self.pilots.append(crew)
        else:
            self.cabin_crew.append(crew)

    def build_seats(self, rows: int, cols: int):
        """ Build the plane seats
        Parameters:
            rows (int): The number of rows in the plane
            cols (int): The number of columns in the plane
        """
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(None)
            self.seats.append(row)

    def get_capacity_left(self):
        """ Get the number of empty seats in the plane
        Returns:
            int: The number of empty seats
        """
        return sum(row.count(None) for row in self.seats)

    def get_status(self):
        """ Get the status of the plane
        Returns:
            str: The status of the plane
        """
        if self.flying:
           print("Flying") 
        else:
            print("Not flying")
        print(f"Number of passengers: {len(self.passengers)}")
        print(f"Number of pilots: {len(self.pilots)}")
        print(f"Number of cabin crew members: {len(self.cabin_crew)}")

        full_baggage_weight = 0
        for row in self.seats:
            for person in row:
                if person != None:
                    full_baggage_weight += person.get_baggage_weight()

        print(f"Total baggage weight: {full_baggage_weight}kg")
        print(f"Seats left: {self.get_capacity_left()}")

    def start_plane(self):
        """ Start the plane after validation"""
        if len(self.pilots) < 2:
            print("Cannot start plane! Need at least 2 pilots.")
            return
        if self.flying:
            print("Plane is already flying!")
            return
        if len(self.passengers) <= 1:
            print("Cannot start plane! No passengers on board.")
            return
        if len(self.cabin_crew) <= 1:
            print("Cannot start plane! No cabin crew on board.")
            return

        self.flying = True
        print("Plane started!")

    def land_plane(self):
        """ Land the plane """
        if not self.flying:
            print("Plane is not flying!")
            return
        self.flying = False
        print("Thank you for flying with ", self.name)

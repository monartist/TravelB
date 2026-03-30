# app.py

# This class represents our "Trip" table in the database
class Trip:
    def __init__(self, title, destination):
        self.title = title
        self.destination = destination

# This list acts as our temporary database
database = []

def create_trip(title, destination):
    new_trip = Trip(title, destination)
    database.append(new_trip)
    return f"Trip to {destination} created!"

if __name__ == "__main__":
    print(create_trip("Summer Break", "Lonodn"))
    print(f"Items in database: {len(database)}")
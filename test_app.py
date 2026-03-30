from app import create_trip, database

def test_trip_behavior():
    # GIVEN: The database starts empty
    database.clear()
    
    # WHEN: We create a trip to Tokyo
    create_trip("Work Trip", "Tokyo")
    
    # THEN: The database should have 1 item, and it should be Tokyo
    assert len(database) == 1
    assert database[0].destination == "Tokyo"
    print("BDD Test Passed: Trip behavior is correct!")

# Call the new test
if __name__ == "__main__":
    test_trip_behavior()
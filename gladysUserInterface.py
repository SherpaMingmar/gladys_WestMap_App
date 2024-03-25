import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

def runTests():
    """
    Runs some module functions for testing.
    """
    print("Running module tests...\n")

    # Call login function from gladysUserLogin module
    userLogin.login()

    # Call readSat function from gladysSatellite module
    satellite_data = satellite.readSat()
    print(f"Satellite data: {satellite_data}\n")

    # Call gpsValue function from gladysCompute module
    a, b = 10, 20
    sat_name = "GPS-1"
    gps_result = compute.gpsValue(a, b, sat_name)
    print(f"GPS value for ({a}, {b}) using {sat_name}: {gps_result}\n")

def get_valid_position(prompt):
    """
    Asks the user for (x,y) coordinates and validates them.
    Returns a tuple (x, y) if valid, otherwise None.
    """
    try:
        x, y = map(int, input(prompt).split(","))
        if 0 <= x < 100 and 0 <= y < 100:
            return x, y
        else:
            print("Invalid position. Please enter valid (x, y) values (0-99).")
            return None
    except ValueError:
        print("Invalid input. Please enter valid integer values.")
        return None

def start():
    """
    Logs the user in and runs the app.
    """
    user_name = userLogin.login()
    runApp(user_name)

def runApp(user_name):
    """
    Runs the main app loop.
    """
    user_quit = False
    while not user_quit:
        print("\n-- Welcome to the Gladys West Map App --")
        print("Type c to set current position")
        print("Type d to set destination position")
        print("Type m to calculate distance")
        print("Type t to run module tests")
        print("Type q to quit")

        user_input = input("Enter a command: ").lower()

        if user_input == 'q':
            user_quit = True
            print("Thank You!")
        elif user_input == 't':
            runTests()
        elif user_input == 'c':
            current_position = get_valid_position("Enter current position (x,y): ")
            if current_position:
                print(f"Current position set to {current_position}")
        elif user_input == 'd':
            destination_position = get_valid_position("Enter destination position (x,y): ")
            if destination_position:
                print(f"Destination position set to {destination_position}")
        elif user_input == 'm':
            # Calculate distance using appropriate function
            # (You can add this part based on your other modules)
            print("Calculating distance...")
        else:
            print(f"ERROR: {user_input} is not a valid command")

if __name__ == "__main__":
    start()

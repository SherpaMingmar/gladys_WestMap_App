import io
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

def start():
    """
    Logs the user in and runs the app.
    """
    user_name = userLogin.login()
    runApp(user_name)

def get_valid_position(prompt):
    """
    Gets a valid (x, y) position from the user.
    """
    valid_position = False
    while not valid_position:
        try:
            x, y = map(int, input(prompt).split())
            if 0 <= x <= 99 and 0 <= y <= 99:
                valid_position = True
            else:
                print("Invalid position. Please enter (x, y) values between 0 and 99.")
        except ValueError:
            print("Invalid input. Please enter integer values for (x, y).")
    return x, y

def calculate_distance(pos1, pos2):
    """
    Calculates Euclidean distance between two positions.
    """
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

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
            print("Thank You! Visiting Gladys West Map App")
        elif user_input == 't':
            runTests()
        elif user_input == 'c':
            current_position = get_valid_position("Enter current position (x ,y): ")
        elif user_input == 'd':
            destination_position = get_valid_position("Enter destination position (x ,y): ")
        elif user_input == 'm':
            if 'current_position' not in locals():
                print("Please set current position first.")
                continue
            elif 'destination_position' not in locals():
                print("Please set destination position first.")
                continue
            else:
                distance = calculate_distance(current_position, destination_position)
                print(f"Distance between current_position and destination_position is : {distance}")
        else:
            print(f"ERROR: {user_input} is not a valid command")


if __name__ == "__main__":
    start()
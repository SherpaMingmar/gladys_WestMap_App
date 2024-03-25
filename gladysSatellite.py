import json

def readSat(sat, pathToJSONDataFiles):
    """
    Reads satellite data from a JSON file.
    Returns the data as a dictionary.
    """
    try:
        file_path = f"{pathToJSONDataFiles}/{sat}-satellite.json"
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"ERROR: Unable to open the file {file_path}")
        return None

def gpsValue(x, y, sat, pathToJSONDataFiles):
    """
    Calculates the GPS value for the given (x, y) coordinates using satellite data.
    Returns the calculated value.
    """
    # Read satellite data
    data = readSat(sat, pathToJSONDataFiles)

    if data is not None:
        # Extract the value based on (x, y) coordinates
        gps_result = data.get("value", 0)  # Default to 0 if value is not found
        return gps_result
    else:
        return None

# Example usage
if __name__ == "__main__":
    sat_name = "GPS-1"
    x_coord, y_coord = 0, 0
    path_to_data_files = "/Users/sherpamingmar/Desktop/Gladys_WestMap_ App/gladysWestMapApp"  # Update this with the actual path
    result = gpsValue(x_coord, y_coord, sat_name, path_to_data_files)
    if result is not None:
        print(f"GPS value for ({x_coord}, {y_coord}) using {sat_name}: {result}")
    else:
        print("Error: Unable to calculate GPS value.")

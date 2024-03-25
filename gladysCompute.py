import gladysSatellite as satellite

def gpsAverage(x, y):
    """
    Calculates the GPS average value for the given (x, y) coordinates.
    Returns the calculated average.
    """
    # Call gpsValue function to get satellite data
    sat_name = "altitude"
    value = satellite.gpsValue(x, y, sat_name)

    # Calculate average
    average = value / 2

    return average

def distance(current, destination):
    """
    Calculates the distance between current and destination positions.
    Returns the calculated distance.
    """
    # Call gpsValue function to get satellite data
    sat_name = "distance"
    current_value = satellite.gpsValue(*current, sat_name)
    dest_value = satellite.gpsValue(*destination, sat_name)

    # Calculate distance
    distance = abs(dest_value - current_value)

    return distance

# Example usage
if __name__ == "__main__":
    current_pos = (10, 20)
    dest_pos = (30, 40)
    avg = gpsAverage(*current_pos)
    dist = distance(current_pos, dest_pos)
    print(f"GPS average for {current_pos}: {avg}")
    print(f"Distance between {current_pos} and {dest_pos}: {dist}")

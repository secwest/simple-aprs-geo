

from shapely.geometry import Point, Polygon

# Inline subset of coordinates for each country for simple bounding calculation
country_coordinates = {
    'India': [
        (93.8, 6.8), (73.0, 8.3), (68.1, 23.6), (69.6, 27.2), (75.8, 32.9), (76.5, 33.2), (77.8, 33.0), (96.5, 28.2), (97.1, 27.8), (97.2, 27.1), (93.8, 6.8)
    ],
    'Indonesia': [
        (122.8, -10.9), (106.4, -7.4), (102.3, -5.5), (98.9, -1.7), (95.7, 2.8), (95.2, 5.9), (126.7, 4.5), (141.0, -2.6), (141.0, -9.1), (122.8, -10.9)
    ],
    'Malaysia': [
        (110.6, 0.9), (103.5, 1.3), (101.3, 2.8), (99.6, 6.4), (100.2, 6.7), (117.0, 7.4), (117.3, 7.3), (119.3, 5.3), (118.5, 4.4), (114.6, 1.4), (110.6, 0.9)
    ],
    'Philippines': [
        (119.8, 5.1), (117.0, 7.8), (116.9, 8.0), (120.6, 18.5), (121.5, 19.4), (122.2, 18.5), (125.5, 12.2), (126.2, 9.8), (126.6, 7.3), (126.2, 6.3), (125.4, 5.6), (119.8, 5.1)
    ],
    'Vietnam': [
        (104.9, 8.6), (103.8, 10.4), (102.1, 22.4), (102.5, 22.8), (105.4, 23.3), (106.7, 22.9), (108.0, 21.5), (109.5, 12.9), (109.0, 11.4), (104.9, 8.6)
    ],
    'New Zealand': [
        (169.2, -52.6), (-176.6, -44.1), (-176.8, -43.8), (173.0, -34.4), (178.6, -37.7), (178.8, -49.6), (169.2, -52.6)
    ],
    'China': [
        (109.6, 18.2), (100.2, 21.4), (81.1, 30.0), (78.9, 31.2), (74.4, 37.1), (73.6, 39.2), (74.0, 40.0), (79.9, 44.9), (83.0, 47.2), (86.9, 49.1), (123.3, 53.6), (125.2, 53.2), (126.1, 52.8), (134.7, 48.3), (134.8, 47.7), (133.9, 46.3), (119.8, 25.4), (116.5, 22.9), (109.6, 18.2)
    ],
    'Taiwan': [
        (120.7, 21.9), (118.3, 24.4), (121.5, 25.3), (122.0, 25.0), (121.4, 23.1), (120.7, 21.9)
    ],
    'Japan': [
        (123.9, 24.3), (123.7, 24.3), (129.5, 34.7), (141.0, 45.5), (142.0, 45.5), (145.3, 44.3), (145.8, 43.4), (140.3, 35.1), (127.8, 26.2), (125.4, 24.7), (123.9, 24.3)
    ],
    'Australia': [
        (158.8, -54.8), (115.0, -34.3), (113.0, -25.8), (113.7, -22.6), (114.0, -21.8), (115.4, -20.7), (130.4, -11.2), (142.3, -10.2), (153.3, -24.7), (159.0, -54.5), (158.8, -54.8)
    ],
    'Thailand': [
        (101.1, 5.6), (99.7, 6.5), (98.3, 7.8), (97.3, 18.5), (98.0, 19.8), (100.0, 20.5), (100.3, 20.4), (104.0, 18.3), (104.8, 17.4), (105.6, 15.6), (105.5, 14.6), (102.1, 6.2), (101.8, 5.7), (101.1, 5.6)
    ],
    'Yemen': [
        (52.4, 12.2), (43.5, 12.7), (42.7, 14.0), (42.6, 15.4), (43.2, 17.3), (43.4, 17.5), (49.1, 18.6), (52.0, 19.0), (53.1, 16.6), (54.5, 12.5), (53.8, 12.3), (52.4, 12.2)
    ],
}
# Create polygons for each country
country_polygons = {}
for country, coords in country_coordinates.items():
    polygon = Polygon(coords)
    country_polygons[country] = polygon

# Define APRS frequencies for the countries
aprs_frequencies = {
    'India': '144.390 MHz',
    'Indonesia': '144.390 MHz',
    'Malaysia': '144.390 MHz',
    'Philippines': '144.390 MHz',
    'Vietnam': '144.390 MHz',
    'New Zealand': '144.575 MHz',
    'South Korea': '144.620 MHz',
    'China': '144.640 MHz',
    'Taiwan': '144.640 MHz',
    'Japan': '144.660 MHz',
    'Australia': '145.175 MHz',
    'Thailand': '145.525 MHz',
    'North America': '144.390 MHz',
    'Europe': '144.800 MHz',
    'Default': '144.390 MHz'
}

# Function to determine the appropriate APRS frequency
def get_aprs_frequency(lon, lat):
    point = Point(lon, lat)

    # Check if within longitude boundaries for the Americas
    if -167.5 <= lon <= -25.0:  # Longitude range for the Americas
        return aprs_frequencies['North America']

    # Check if within longitude boundaries for Europe
    elif -25.0 < lon < 40.0:  # Approximate longitude range for Europe
        return aprs_frequencies['Europe']

    # Check other countries
    for country, polygon in country_polygons.items():
        if polygon.contains(point):
            return aprs_frequencies.get(country, aprs_frequencies['Default'])

    # Default frequency if not in any specified region
    return aprs_frequencies['Default']

# Example GPS coordinates
gps_lon = -90.0  # Replace with actual longitude
gps_lat = 40.0  # Replace with actual latitude

# Determine the APRS frequency
aprs_frequency = get_aprs_frequency(gps_lon, gps_lat)

print(f"The APRS frequency for the given coordinates is: {aprs_frequency}")

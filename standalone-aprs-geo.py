class Polygon:
    def __init__(self, points):
        self.points = points

    def contains(self, x, y):
        n = len(self.points)
        inside = False
        p1x, p1y = self.points[0]
        for i in range(1, n + 1):
            p2x, p2y = self.points[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside


# Inline subset of coordinates for each country for simple bounding calculation
country_coordinates = {
    'India': Polygon([
        (93.8, 6.8 ), (73.0, 8.3), (68.1, 23.6), (69.6, 27.2), 
        (75.8, 32.9), (76.5, 33.2), (77.8, 33.0), (96.5, 28.2), 
        (97.1, 27.8 ), (97.2, 27.1), (93.8, 6.8 )
    ]),
    'Indonesia': Polygon([
        (122.8, -10.9), (106.4, -7.4), (102.3, -5.5), (98.9, -1.7),
        (95.7, 2.8 ), (95.2, 5.9), (126.7, 4.5), (141.0, -2.6),
        (141.0, -9.1), (122.8, -10.9)
    ]),
    'Malaysia': Polygon([
        (110.6, 0.9), (103.5, 1.3), (101.3, 2.8 ), (99.6, 6.4), 
        (100.2, 6.7), (117.0, 7.4), (117.3, 7.3), (119.3, 5.3), 
        (118.5, 4.4), (114.6, 1.4), (110.6, 0.9)
    ]),
    'Philippines': Polygon([
        (119.8, 5.1), (117.0, 7.8 ), (116.9, 8.0), (120.6, 18.5), 
        (121.5, 19.4), (122.2, 18.5), (125.5, 12.2), (126.2, 9.8 ), 
        (126.6, 7.3), (126.2, 6.3), (125.4, 5.6), (119.8, 5.1)
    ]),
    'Vietnam': Polygon([
        (104.9, 8.6), (103.8, 10.4), (102.1, 22.4), (102.5, 22.8 ), 
        (105.4, 23.3), (106.7, 22.9), (108.0, 21.5), (109.5, 12.9), 
        (109.0, 11.4), (104.9, 8.6)
    ]),
    'New Zealand': Polygon([
        (-34.4, 166.5), (-34.4, 178.6), (-47.3, 178.6), (-47.3, 166.5),
        (-34.4, 166.5)
    ]),
    'China': Polygon([
        (109.6, 18.2), (100.2, 21.4), (81.1, 30.0), (78.9, 31.2), 
        (74.4, 37.1), (73.6, 39.2), (74.0, 40.0), (79.9, 44.9), 
        (83.0, 47.2), (86.9, 49.1), (123.3, 53.6), (125.2, 53.2), 
        (126.1, 52.8 ), (134.7, 48.3), (134.8, 47.7), (133.9, 46.3), 
        (119.8, 25.4), (116.5, 22.9), (109.6, 18.2)
    ]),
    'Taiwan': Polygon([
        (120.7, 21.9), (118.3, 24.4), (121.5, 25.3), (122.0, 25.0), 
        (121.4, 23.1), (120.7, 21.9)
    ]),
    'Japan': Polygon([
        (123.9, 24.3), (123.7, 24.3), (129.5, 34.7), (141.0, 45.5), 
        (142.0, 45.5), (145.3, 44.3), (145.8, 43.4), (140.3, 35.1), 
        (127.8, 26.2), (125.4, 24.7), (123.9, 24.3)
    ]),
    'Australia': Polygon([
        (158.8, -54.8 ), (115.0, -34.3), (113.0, -25.8 ), (113.7, -22.6), 
        (114.0, -21.8 ), (115.4, -20.7), (130.4, -11.2), (142.3, -10.2), 
        (153.3, -24.7), (159.0, -54.5), (158.8, -54.8 )
    ]),
    'Thailand': Polygon([
        (101.1, 5.6), (99.7, 6.5), (98.3, 7.8 ), (97.3, 18.5), 
        (98.0, 19.8 ), (100.0, 20.5), (100.3, 20.4), (104.0, 18.3), 
        (104.8, 17.4), (105.6, 15.6), (105.5, 14.6), (102.1, 6.2), 
        (101.8, 5.7), (101.1, 5.6)
    ]),
    'Yemen': Polygon([
        (52.4, 12.2), (43.5, 12.7), (42.7, 14.0), (42.6, 15.4), 
        (43.2, 17.3), (43.4, 17.5), (49.1, 18.6), (52.0, 19.0), 
        (53.1, 16.6), (54.5, 12.5), (53.8, 12.3), (52.4, 12.2)
    ]),
    'North Korea': Polygon([
        (125.3, 37.7), (124.7, 38.1), (124.4, 40.1), (126.9, 41.8 ), 
        (129.9, 43.0), (130.3, 42.9), (130.7, 42.3), (128.3, 38.4), 
        (126.6, 37.8 ), (125.3, 37.7)
    ]),
    'South Korea': Polygon([
        (126.3, 33.2), (126.1, 34.4), (126.1, 36.7), (126.4, 37.8 ), 
        (127.1, 38.3), (128.4, 38.6), (129.4, 37.1), (129.6, 36.0), 
        (129.5, 35.5), (129.2, 35.2), (126.8, 33.3), (126.3, 33.2)
    ]),
    'United Kingdom': Polygon([
        (-5.2, 50.0), (-5.7, 50.1), (-8.2, 54.5), (-7.5, 57.6), 
        (-7.0, 58.2), (-0.8, 60.8 ), (1.7, 52.6), (1.4, 51.2), 
        (0.3, 50.7), (-5.2, 50.0)
    ]),
}

# Define APRS frequencies for the countries
aprs_frequencies = {
    'Yemen': 'Bad Juju',
    'United Kingdom': 'Bad Juju',
    'North Korea': 'Bad Juju',
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
    # Check specific countries first
    for country, polygon in country_polygons.items():
        if polygon.contains(lon, lat):
            return aprs_frequencies.get(country, aprs_frequencies['Default'])

    # Check if within longitude boundaries for the Americas
    if -167.5 <= lon <= -25.0:  # Longitude range for the Americas
        return aprs_frequencies['North America']

    # Check if within longitude boundaries for Europe & Africa
    elif -25.0 < lon < 40.0:  # Approximate longitude range for Europe
        return aprs_frequencies['Europe']

    # Default frequency if not in any specific country or region
    return aprs_frequencies['Default']


# Example GPS coordinates and determining the APRS frequency
gps_lon = -90.0  # Replace with actual longitude
gps_lat = 40.0  # Replace with actual latitude

aprs_frequency = get_aprs_frequency(gps_lon, gps_lat)
print(f"The APRS frequency for the given coordinates is: {aprs_frequency}")

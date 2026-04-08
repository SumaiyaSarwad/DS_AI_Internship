# data.py

PLACES = {
    1: "Main Gate",
    2: "Hostel",
    3: "Parking",
    4: "Block B"
}

DESTINATIONS = {
    1: "Library",
    2: "Canteen",
    3: "Block A",
    4: "Auditorium"
}

DISTANCES = {
    ("Main Gate", "Library"): 120,
    ("Main Gate", "Auditorium"): 180,
    ("Hostel", "Canteen"): 300,
    ("Hostel", "Library"): 350,
    ("Parking", "Block A"): 200,
    ("Block B", "Auditorium"): 250
}

DEFAULT_DISTANCE = 100

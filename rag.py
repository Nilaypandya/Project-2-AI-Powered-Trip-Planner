travel_data = {

    "Goa": """
    Goa is famous for beaches, nightlife,
    water sports, seafood, and adventure activities.
    Best time to visit is during winter and summer.
    """,

    "Manali": """
    Manali is famous for snow activities,
    trekking, mountain adventures, and cafes.
    Winter is best for snow experiences.
    """,

    "Gujarat": """
    Gujarat is famous for Navratri festival,
    temples, cultural tourism, and local food.
    October is best for cultural experiences.
    """,

    "Kerala": """
    Kerala is famous for backwaters,
    houseboats, greenery, and Ayurvedic tourism.
    Monsoon season is very popular.
    """,

    "Rajasthan": """
    Rajasthan is famous for forts,
    desert safari, royal palaces, and heritage tourism.
    Winter is best for visiting Rajasthan.
    """
}

def retrieve_data(destination):

    destination = destination.strip()

    return travel_data.get(
        destination,
        "Popular tourist destination with many attractions."
    )
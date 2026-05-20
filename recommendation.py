def get_recommendations(season, destination):

    recommendations = {

        "Summer": [
            "Hill stations",
            "River rafting",
            "Water activities"
        ],

        "Winter": [
            "Snow activities",
            "Skiing",
            "Hot cafes"
        ],

        "Monsoon": [
            "Waterfalls",
            "Nature walks",
            "Green valleys"
        ]
    }

    festival_data = {

        "Gujarat": [
            "Navratri Festival",
            "Garba Nights",
            "Dwarka Temple Visit"
        ],

        "Jammu": [
            "Vaishno Devi Yatra",
            "Bahu Fort Visit",
            "Local Dogra Culture"
        ],

        "Goa": [
            "Sunburn Festival",
            "Beach Carnival",
            "Nightlife Events"
        ],

        "Kerala": [
            "Onam Festival",
            "Kathakali Shows",
            "Boat Races"
        ]
    }

    season_places = recommendations.get(season, [])

    festival_places = festival_data.get(destination, [])

    return {

        "season_recommendations": season_places,

        "festival_recommendations": festival_places
    }
capitals = {
    "France": "Paris",
    "Spain": "Madrid", 
}


nested_list = ["A","B", ["C", "D", "E"]]

print(nested_list[2][1])  


travel_log = {
    "France": {
        "Cities_visited": ["Paris", "Lille", "Dijon"],
        "Total_visits": 12
        }
        ,
    "Spain": {
        "Cities_visited": ["Madrid", "Barcelona", "Seville"],
        "Total_visits": 5
        }
}

print(travel_log["France"]["Cities_visited"][1])
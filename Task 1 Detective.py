#RICHARD KAINUKU 
#Student ID: 270565532

#Task 1: Detective

#Room values
rooms = {"Kitchen": 0.1, "Bathroom": 0.3, "Master bedroom": 0.3, "Ball": 0.5, "Dining": 0.9}
#Tool values
tools = {"Lead pipe": 0.1, "Dagger": 0.4, "Revolver": 0.7, "Hammer": 0.8}

#Scenario dictionary
scenarios = [
    {"suspect": "John", "room": "Bathroom", "tool": "Lead pipe"},
    {"suspect": "Cathy", "room": "Dining", "tool": "Revolver"},
    {"suspect": "Cathy", "room": "Ball", "tool": "Dagger"},
    {"suspect": "Samuel", "room": "Master bedroom", "tool": "Revolver"},
    {"suspect": "John", "room": "Kitchen", "tool": "Dagger"},
    {"suspect": "Cathy", "room": "Master bedroom", "tool": "Hammer"}
]

#Calculate scenario values
for scenario in scenarios:
    scenario["value"] = rooms[scenario["room"]] + tools[scenario["tool"]]

#Sorting scenarios by value
scenarios.sort(key=lambda scenario: scenario["value"], reverse=True)

#Display murder scenarios
print("Murder scenarios in order:")

for scenario in scenarios:
    print(
        scenario["suspect"],
        "-",
        scenario["room"],
        "-",
        scenario["tool"],
        "- Value:",
        scenario["value"]
    )
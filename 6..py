rooms = {"A": "Dirty", "B": "Dirty"}
position = "A"

while "Dirty" in rooms.values():
    print("Current position:", position)

    if rooms[position] == "Dirty":
        rooms[position] = "Clean"
        print("Room", position, "cleaned")

    position = "B" if position == "A" else "A"

print("Final room status:", rooms)
print("All rooms are clean")

# Vacuum Cleaner Problem

rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

current_room = 'A'

while 'Dirty' in rooms.values():
    print("Current Room:", current_room)

    if rooms[current_room] == 'Dirty':
        print("Cleaning Room", current_room)
        rooms[current_room] = 'Clean'

    if current_room == 'A':
        current_room = 'B'
    else:
        current_room = 'A'

print("All rooms are clean!")
print(rooms)

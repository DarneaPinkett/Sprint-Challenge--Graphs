from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room

moves = Stack()

while len(visited_rooms) < len(world.rooms):
    exits = player.current_room.get_exits()
    possible_directions = []

    for exit in exits:
        if (exit is not None) and (player.current_room.get_room_in_direction(exit) not in visited_rooms):
            possible_directions.append(exit)
            
    visited_rooms.add(player.current_room)

    if len(possible_directions) > 0:
        random_direction = random.randint(0, len(possible_directions) -1)
        moves.push(possible_directions[random_direction])
        player.travel(possible_directions[random_direction])
        traversal_path.append(possible_directions[random_direction])
    else:
        last_move = moves.pop()


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

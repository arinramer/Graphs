from room import Room
from player import Player
from world import World
from util import Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

def bfs(direction):
    q = Queue()
    q.enqueue([direction])

    while q.size() > 0:
        current_path = q.dequeue()
        node = current_path[-1]
        player.travel(node)
        directions = player.current_room.get_exits()
        for direction in directions:
            if graph.get(player.current_room.id) is not None:
                if graph[player.current_room.id][direction] == '?':
                    for i in current_path:
                        traversal_path.append(i)
            else:
                new_path = list(current_path)
                new_path.append(direction)
                q.enqueue(new_path)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
s = []
graph = {
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
directions = player.current_room.get_exits()
for direction in directions:
    if graph[player.current_room.id][direction] == '?':
        s.append(direction)

while len(s) > 0:
    current_direction = s.pop()
    prev = player.current_room.id
    directions = player.current_room.get_exits()
    if current_direction in directions:
        player.travel(current_direction)
    graph[prev][current_direction] = player.current_room.id
    
    for direction in directions:
        if player.current_room.id not in graph:
            graph[player.current_room.id] = {}
        if direction not in graph[player.current_room.id]:
            graph[player.current_room.id][direction] = '?'                
        if graph[player.current_room.id][direction] == '?':
            s.append(direction)
            traversal_path.append(direction)
    # if '?' not in graph[player.current_room.id]:
    #     bfs(direction)
print(graph)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

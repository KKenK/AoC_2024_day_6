from classes import input_parser
from classes import grid
from classes import guard
from modules import find_guard
from modules import add_char_border
import copy

class RouteLogger():

    def __init__(self):
        self.log_entries = []
    
    def add_entry(self, x, y , guard_orientation):

        self.log_entries.append((x, y ,guard_orientation))

    def check_if_entry_in_log(self, x, y, guard_orientation):

        if (x, y, guard_orientation) in self.log_entries:

            return True
        
        return False

def make_set_of_possible_points_to_insert_object(log_entries):

    positions_visited_coordinates_set = []
    positions_visited_set = []

    for log in log_entries:

        if (log[0], log[1]) in positions_visited_coordinates_set:
            continue
        
        positions_visited_coordinates_set.append((log[0], log[1]))
        positions_visited_set.append((log[0], log[1], log[2]))
    
    return positions_visited_set
    
def find_loop_causing_obstruction_count(floor_plan, positions_visited_set, guard_starting_coordinates):

    viable_loop_position_count = 0

    for i in range(len(positions_visited_set)):
        print(i)
        floor_simulation_with_new_obstruction = copy.deepcopy(floor_plan)

        floor_simulation_with_new_obstruction.mark_grid_position(x = positions_visited_set[i][0],
                                y = positions_visited_set[i][1],
                                mark_char = "#")
        
        guard_simulation = guard.Guard(floor_plan = floor_simulation_with_new_obstruction, orientation = "^", 
                                       current_location_coordinates = guard_starting_coordinates)

        simulation_log = RouteLogger()

        while guard_simulation.has_exited() == False:
           
   
            while guard_simulation.look_ahead_at_the_next_adjacent_space() == "#":
                    
                guard_simulation.turn_90_degrees_right()
            
            if simulation_log.check_if_entry_in_log(x = guard_simulation.current_location_x_coordinate, y = guard_simulation.current_location_y_coordinate,
                                guard_orientation = guard_simulation.orientation):
                
                viable_loop_position_count += 1   

                break

            simulation_log.add_entry(x = guard_simulation.current_location_x_coordinate, y = guard_simulation.current_location_y_coordinate,
                                guard_orientation = guard_simulation.orientation)
            
            guard_simulation.take_one_step_forward()

    return viable_loop_position_count

parsed_input = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_6\input.txt").parsed_input

parsed_input_with_border = add_char_border.add_char_border(parsed_input, "O")

lab = grid.Grid(parsed_input_with_border)

guard_starting_coordinates = find_guard.return_guard_coordinates(parsed_input_with_border)

lab_guard = guard.Guard(floor_plan = lab, orientation = "^", current_location_coordinates = guard_starting_coordinates)

guard_log = RouteLogger()

while lab_guard.has_exited() == False:

    lab.mark_grid_position(x = lab_guard.current_location_x_coordinate,
                            y = lab_guard.current_location_y_coordinate,
                            mark_char = "X")
    
    if lab_guard.look_ahead_at_the_next_adjacent_space() == "#":
            
        lab_guard.turn_90_degrees_right()

    guard_log.add_entry(x = lab_guard.current_location_x_coordinate, y = lab_guard.current_location_y_coordinate,
                        guard_orientation = lab_guard.orientation)
    
    lab_guard.take_one_step_forward()

floor_plan = copy.deepcopy(lab)

#positions_visited_set = copy.copy(guard_log.log_entries)

#positions_visited_set = make_set_of_possible_points_to_insert_object(positions_visited_set)

positions_visited_set = []
for row in lab.grid:
    for point in row:
        if not point.char == "X":
            continue
        positions_visited_set.append((point.x, point.y))

i = 0
while i < len(positions_visited_set):
    if not positions_visited_set[i] == guard_starting_coordinates:
        i += 1
        continue
    positions_visited_set.pop(i)


floor_plan.mark_grid_position(x = guard_starting_coordinates[0], y = guard_starting_coordinates[1], mark_char = ".")

with open((r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_6\marked_grid.txt"),"w") as f:
    
    for row in lab.grid:
        f.write(str("".join([x.char for x in row])) + "\n")

print(find_loop_causing_obstruction_count(floor_plan = grid.Grid(parsed_input_with_border), positions_visited_set = positions_visited_set, guard_starting_coordinates = guard_starting_coordinates))
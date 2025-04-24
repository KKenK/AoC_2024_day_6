from classes import input_parser
from classes import grid
from classes import guard
from modules import find_guard
from modules import add_char_border

parsed_input = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_6\test.txt").parsed_input

parsed_input_with_border = add_char_border.add_char_border(parsed_input, "O")

lab = grid.Grid(parsed_input_with_border)

lab_guard = guard.Guard(floor_plan = lab, orientation = "^", current_location_coordinates = find_guard.return_guard_coordinates(parsed_input_with_border))

while lab_guard.has_exited() == False:

    lab.mark_grid_position(x = lab_guard.current_location_x_coordinate,
                            y = lab_guard.current_location_y_coordinate,
                            mark_char = "X")
    
    if lab_guard.look_ahead_at_the_next_adjacent_space() == "#":
            
        lab_guard.turn_90_degrees_right()

    lab_guard.take_one_step_forward()

distinct_positions_visited_count = 0 

for row in lab.grid:

    distinct_positions_visited_count += [x.char for x in row].count("X")


with open((r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_6\marked_grid.txt"),"w") as f:
    for row in lab.grid:

        f.write(str("".join([x.char for x in row])) + "\n")

print(distinct_positions_visited_count)
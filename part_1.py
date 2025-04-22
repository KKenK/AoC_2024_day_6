from classes import input_parser
from classes import grid
from classes import guard
from modules import find_guard

if __name__ == "__main__":

    parsed_input = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_6\input.txt").parsed_input

    lab = grid.Grid(parsed_input)

    lab_guard = guard.Guard("^", find_guard.return_guard_coordinates(parsed_input))

    while lab_guard.has_exited(parsed_input) == False:

        lab.mark_grid_position(x = lab_guard.current_location_x_coordinate,
                               y = lab_guard.current_location_y_coordinate,
                               mark_char = "X")

        lab_guard.take_one_step_forward(parsed_input)

    distinct_positions_visited_count = 0 
    
    for row in lab.grid:

        distinct_positions_visited_count += [x.char for x in row].count("X")

    
    with open((r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_6\marked_grid.txt"),"w") as f:
        for row in lab.grid:

            f.write(str("".join([x.char for x in row])) + "\n")

    print(distinct_positions_visited_count)
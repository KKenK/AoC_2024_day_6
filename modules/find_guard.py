def return_guard_coordinates(char_grid):
 
    guard_y_coordinate = [y for y in range(len(char_grid)) if "^" in char_grid[y]][0]

    guard_x_coordinate = char_grid[guard_y_coordinate].index("^")

    return guard_x_coordinate, guard_y_coordinate
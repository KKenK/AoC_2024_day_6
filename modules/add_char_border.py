def add_char_border(grid, char):

    grid_width = len(grid[0])

    grid_with_top_bottom_border = [char * grid_width] + grid + [char * grid_width]

    grid_with_border = [char + row + char for row in grid_with_top_bottom_border]

    return grid_with_border


from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "char"])

def generate_grid_permutations(grid):

    grid_length = len(grid)
    grid_width = len(grid[0])

    center_point_coordinates = Point( x = grid_width / 2 , y = grid_length / 2, char = input[grid_length / 2][grid_width / 2])

    for y in range(grid_length):

        row = []

        for x in range(grid_width):

            row.append(Point(x = grid[y][x].x - 65, y = grid[y][x].y - 65, char = grid[y][x].char))

def _rotate_grid_by_90_degrees_clockwise(grid_with_center_relative_coordinates):
    
    for position in range(len(grid_with_center_relative_coordinates)):
        
        position = self.pattern_relative_coordinates[position]
                    
        position.relative_x, position.relative_y= position.relative_y * -1, position.relative_x
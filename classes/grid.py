class Point():
    def __init__(self, x, y, char):
        self.x = x 
        self.y = y
        self.char = char


class Grid():

    def __init__(self, input):

        self.grid = self._make(input)
    
    def _make(self, input):

        grid = []

        grid_length = len(input)
        grid_width = len(input[0])

        for y in range(grid_length):

            row = []

            for x in range(grid_width):

                row.append(Point(x = x, y = y, char = input[y][x]))
            
            grid.append(row)
            
        return grid
    
    def print_grid(self):
        
        for row in self.grid:

            print([x.char for x in row])

    def mark_grid_position(self, x, y, mark_char):
        
        self.grid[y][x].char = mark_char
        
class Guard():

    def __init__(self, orientation, current_location_coordinates):
        self.orientation = orientation
        self.current_location_x_coordinate = current_location_coordinates[0]
        self.current_location_y_coordinate = current_location_coordinates[1]

        self.number_of_turns = 0
        self.walking_instruction_dictionary = {"^": (0 , -1), 
                                               ">": (1 , 0), 
                                               "v": (0 , 1), 
                                               "<": (-1 , 0)}
        
        self.reorientate_instructions =  {"^": ">", 
                                            ">": "v", 
                                            "v": "<", 
                                            "<": "^"}
        
    def take_one_step_forward(self, grid):
        
        next_position_x = self.current_location_x_coordinate + self.walking_instruction_dictionary[self.orientation][0]
        next_position_y = self.current_location_y_coordinate + self.walking_instruction_dictionary[self.orientation][1]
        
        if grid[next_position_y][next_position_x] == "#":
            self.orientation = self._change_direction()
            self.number_of_turns +=1

        self.current_location_x_coordinate += self.walking_instruction_dictionary[self.orientation][0]    
        self.current_location_y_coordinate += self.walking_instruction_dictionary[self.orientation][1]      
     
    def _change_direction(self):

        return self.reorientate_instructions[self.orientation]

    def has_exited(self, grid):
        
        if self.current_location_x_coordinate < 0 or self.current_location_x_coordinate > len(grid[0]):
            return True
        if self.current_location_y_coordinate < 0 or self.current_location_x_coordinate > len(grid):
            return True
        return False
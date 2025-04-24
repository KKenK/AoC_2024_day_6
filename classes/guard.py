class Guard():

    def __init__(self, floor_plan, orientation, current_location_coordinates):
        self.floor_plan = floor_plan
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
        
    def take_one_step_forward(self):
        
        self.current_location_x_coordinate += self.walking_instruction_dictionary[self.orientation][0]    
        self.current_location_y_coordinate += self.walking_instruction_dictionary[self.orientation][1]      
    
    def look_ahead_at_the_next_adjacent_space(self):

        next_position_x = self.current_location_x_coordinate + self.walking_instruction_dictionary[self.orientation][0]
        next_position_y = self.current_location_y_coordinate + self.walking_instruction_dictionary[self.orientation][1]
        
        return self.floor_plan.grid[next_position_y][next_position_x].char
        
    def turn_90_degrees_right(self):

        self.orientation = self.reorientate_instructions[self.orientation]

    def has_exited(self):
        
        if self.floor_plan.grid[self.current_location_y_coordinate][self.current_location_x_coordinate].char == "O":
            return True
        
        return False
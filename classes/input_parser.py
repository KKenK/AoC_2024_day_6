class InputParser():

    def __init__(self, input_path):
        
        input = []

        with open(input_path) as f:
            input = f.read()
        
        self.parsed_input = self._parse_input(input)
    
    def _parse_input(self, input):

        grid = input.split("\n")

        return grid

if __name__ == "__main__":

    input_parser = InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_6\input.txt")

    #print(input_parser.parsed_input)
    print(input_parser.parsed_input[0])

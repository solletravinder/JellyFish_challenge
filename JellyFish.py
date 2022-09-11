ORIENTATION = (
    ("N", "NORTH"),
    ("S", "SOUTH"),
    ("E", "EAST"),
    ("W", "WEST")
    )


class JellyFish:

    def __init__(self, x, y, orientation):
        self.coordinates = (int(x), int(y))
        self.orientation = orientation
        self.instructions = ""
        self.is_fish_lost = False


    def compare_coordinates(self, tank_coord, curr_coord):
        if tank_coord[0] <= curr_coord[0] and tank_coord[1] <= curr_coord[1]:
            return True
        return False

    def move_forward(self, tank_size):
        if self.orientation == "N":
            x, y = 0, 1
        elif self.orientation == "S":
            x, y = 0, -1
        elif self.orientation == "E":
            x, y = 1, 0
        elif self.orientation == "W":
            x, y = -1, 0

        curr_coord = tuple(map(lambda i, j: i + j, self.coordinates, (x,y)))
        is_not_dead = self.compare_coordinates(tank_size, curr_coord)
        if is_not_dead:
            self.coordinates = curr_coord

    def change_orientation(self, instruction, tank_size, LOST_COORD_POS=None):
        curr_orientation = self.orientation
        if curr_orientation == "N":
            if instruction == "L":
                self.orientation = "W"
            elif instruction == "R":
                self.orientation = "E"
        elif curr_orientation == "S":
            if instruction == "L":
                self.orientation = "E"
            elif instruction == "R":
                self.orientation = "W"
        elif curr_orientation == "E":
            if instruction == "L":
                self.orientation = "N"
            elif instruction == "R":
                self.orientation = "S"
        elif curr_orientation == "W":
            if instruction == "L":
                self.orientation = "S"
            elif instruction == "R":
                self.orientation = "N"

    def coordinate_checker(self, x, y):
        pass

    def add_instructions(self, instructions):
        self.instructions = instructions

    def run_simulation(self, tank_size, Lost_coord_pos):
        for i in list(self.instructions):
            if i == "F":
                self.move_forward(tank_size)
            else:
                self.change_orientation(i, tank_size, Lost_coord_pos)
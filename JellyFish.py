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
        self.Lost_coord_pos = None


    def compare_coordinates(self, tank_coord, curr_coord):
        if curr_coord[0] <= tank_coord[0] and curr_coord[1] <= tank_coord[1]:
            return True
        return False

    def move_forward(self, tank_size, Lost_coord_pos=None):
        if not Lost_coord_pos:
            Lost_coord_pos = []

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
        if not is_not_dead:
            passed_through_already_taken_path = self.compare_coordinates_with_last_fish(curr_coord, Lost_coord_pos)
            if not passed_through_already_taken_path:
                self.Lost_coord_pos = curr_coord
                self.is_fish_lost = True
        else:
            self.coordinates = curr_coord
        return 

    def compare_coordinates_with_last_fish(self, curr_coord, lost_coord_pos):
        for (x,y) in lost_coord_pos:
            if x == curr_coord[0] and y == curr_coord[1]:
                return True
        return False

    def change_orientation(self, instruction):
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
        for i in self.instructions:
            if self.is_fish_lost:
                break;
            if i == "F":
                self.move_forward(tank_size, Lost_coord_pos)
            else:
                self.change_orientation(i)

        if self.Lost_coord_pos:
            Lost_coord_pos.append(self.Lost_coord_pos)
        return Lost_coord_pos
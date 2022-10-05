"""
 Contains main function
"""
from JellyFish import JellyFish

MAX_COORD = 60
MAX_INSTRUCTIONS = 100

class FishTank:
    """
        Represents the Fish Tank
    """

    def __init__(self, x_coord, y_coord):
        self.size = (x_coord, y_coord)
        self.fish_list = []
        self.lost_coord_pos = []

    def add_fish(self, x_coord, y_coord, position):
        """
            Adding a Jelly Fish
        """
        jelly_fish = JellyFish(x_coord, y_coord, position)
        self.fish_list.append(jelly_fish)
        return jelly_fish

    def run_simulation(self):
        """
            Here Simulation runs
        """
        for jelly_fish in self.fish_list:
            # curr_fish_coord_position = ""
            self.lost_coord_pos = jelly_fish.run_simulation(self.size, self.lost_coord_pos)
            is_fish_lost = jelly_fish.is_fish_lost
            curr_fish_final_coord_position = "".join(list(map(str, jelly_fish.coordinates)) \
                 +[jelly_fish.orientation, "LOST" if is_fish_lost else ""])
            print(curr_fish_final_coord_position)




if __name__ == '__main__':
    ftSize = map(int, list(input("\nEnter the coordinates of the fish tank.")))

    FT = FishTank(*ftSize)
    num_of_fishes = int(input("\nNumber of fish in the tank."))
    for i in range(0, num_of_fishes):
        coord_instr = input("\nEnter the coordinates and instructions for the fish.")
        coord_position, instructions = coord_instr.split()
        if float(coord_position[:2]) > MAX_COORD or len(instructions) > MAX_INSTRUCTIONS:
            break

        JF = FT.add_fish(*list(coord_position))
        JF.add_instructions(instructions)

    if len(FT.fish_list) > 0:
        FT.run_simulation()

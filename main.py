from JellyFish import JellyFish
MAX_COORD = 60
MAX_INSTRUCTIONS = 100

class FishTank:

    def __init__(self, x, y):
        self.SIZE = (x, y)
        self.fish_list = []

    def add_fish(self, x, y, position):
        JF = JellyFish(x, y, position)
        self.fish_list.append(JF)
        return JF

    def run_simulation(self):
        Lost_coord_pos = []
        for a_JF in self.fish_list:
            # curr_fish_coord_position = ""
            a_JF.run_simulation(self.SIZE, Lost_coord_pos)
            is_fish_lost = a_JF.is_fish_lost
            curr_fish_final_coord_position = "".join(list(map(str, a_JF.coordinates)) +[a_JF.orientation, "LOST" if is_fish_lost else ""])
            print(curr_fish_final_coord_position)




if __name__ == '__main__':
    ftSize = map(int, list(input("\nEnter the coordinates of the fish tank.")))

    FT = FishTank(*ftSize)
    num_of_fishes = int(input("\nNumber of fish in the tank."))
    for i in range(0, num_of_fishes):
        coord_instr = input("\nEnter the coordinates and instructions for the fish.")
        coord_position, instructions = coord_instr.split()
        if float(coord_position[:2]) > MAX_COORD or len(instructions) > MAX_INSTRUCTIONS:
            break;
        
        JF = FT.add_fish(*list(coord_position))
        JF.add_instructions(instructions)

    if len(FT.fish_list) > 0:
        FT.run_simulation()
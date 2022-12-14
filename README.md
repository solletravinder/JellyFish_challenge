# JellyFish_challenge (Python 3.9.10)

Jellyfish Challenge  The Jellyfish tank can be modelled by a rectangular grid around which Jellyfish can move according to instructions provided by the Tank IR Remote Control. You are to write a program that determines each sequence of Jellyfish positions and reports the final position of the Jellyfish. A Jellyfish position consists of a grid coordinate (a pair of integers: x-coordinate followed by y-coordinate) and an orientation (N, S, E, W for north, south, east, and west).  A Jellyfish instruction is a string of the letters “L”, “R”, and “F”, which represent, respectively, the instructions:  Left: the jellyfish turns left 90 degrees and remains on the current grid point. Right: the jellyfish turns right 90 degrees and remains on the current grid point. Forward: the jellyfish moves forward one grid point in the direction of the current orientation and maintains the same orientation. The direction North corresponds to the direction from grid point (x, y) to grid point (x, y+1). There is also a possibility that additional command types may be required in the future, and provisions should be made for this.  Since the grid is rectangular and bounded (...yes, the Jellyfish tank is a very flat tank), a jellyfish that moves “off” the edge of the grid is lost forever. However, lost jellyfish leave a “scent” that prohibits future jellyfish from dropping off the tank at the same grid point. The scent is left at the jellyfish's last grid position before disappearing over the edge. The current jellyfish simply ignores an instruction to move “off” the tank from a grid point from which a jellyfish has been previously lost.  The Input The first line of input is the upper-right coordinates of the rectangular tank, the lower-left coordinates are assumed to be 0, 0. The remaining input consists of a sequence of jellyfish positions and instructions (two lines per jellyfish). A position consists of two integers specifying the initial coordinates of the jellyfish and an orientation (N, S, E, W), all separated by whitespace on one line. A jellyfish instruction is a string of the letters “L”, “R”, and “F” on one line.  Each jellyfish is processed sequentially, i.e., it finishes executing the jellyfish instructions before the next jellyfish begins execution. The maximum value for any coordinate is 60. All instruction strings will be less than 100 characters in length.  The Output For each jellyfish position/instruction in the input, the output should indicate the jellyfish's final grid position and orientation. If a jellyfish falls off the edge of the grid, the word “LOST” should be printed after the position and orientation.
<br>
<br>Sample Input  
53 <br>
11E RFRFRFRF <br>
32N FRRFLLFFRRFLL <br>
03W LLFFFLFLFL <br>
<br>
Output  
11E<br>
33NLOST<br> 
23S

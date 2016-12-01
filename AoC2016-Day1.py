
def true_dir(current_direction, r):
    dirs = ["N", "E", "S", "W"]
    cur_pos = dirs.index(current_direction)
    if r == "R":
        if cur_pos == 3:
            new_pos = 0
        else:
            new_pos = cur_pos + 1
        return dirs[new_pos]
    elif r == "L":
        if cur_pos == 0:
            new_pos = 3
        else:
            new_pos = cur_pos - 1
        return dirs[new_pos]

def blocks(direction, distance):
    x_dist = 0
    y_dist = 0
    if direction == "E":
        x_dist = x_dist + distance
    elif direction == "W":
        x_dist = x_dist - distance

    if direction == "N":
        y_dist = y_dist + distance
    if direction == "S":
        y_dist = y_dist - distance

    no_blocks = x_dist + y_dist
    return [no_blocks, x_dist, y_dist]

#for testing without needing to read whole file
data = ["R8", "R4", "R4", "R8"]

#Read file contents
#fh = open("AoC2016-day1-input.txt", "r")
#or i in fh:
    #data = i.replace(" ", "").rstrip().split(",")

direction = "N"
x_travel = 0
y_travel = 0

for i in data:
    compass = i[0]
    distance = int(i[1:])
    direction = true_dir(direction, compass)
    travelled = blocks(direction, distance)[0]
    x_travel = x_travel + blocks(direction, distance)[1]
    #print "X Travel: ", x_travel
    y_travel = y_travel + blocks(direction, distance)[2]
    #print "Y Travel: ", y_travel

print "Blocks travelled: ", abs(x_travel) + abs(y_travel)

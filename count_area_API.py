"""
This is an API for count area application
"""

# colour_dict is a dictionary
# if a colour exists in graph, then the key of that colour is added in the dictionary.
# the corresponding value of that key will be an array of all areas with that colour value
colour_dict = {}


# checks if the colour value exists in graph previously

def check_exist(colour):
    if str(colour) in colour_dict:
        return True
    else:
        return False


# checks if a pixel is connected with other patterns with same colour
# input: the pixel's row i and column j and the colour of that pixel
# output: the array of areas that the pixel connects to, if it's not connected with any area, return empty array

def check_connection(i, j, colour):
    existed_areas = colour_dict[str(colour)]
    connected_area = []
    for area in existed_areas:
        for pixel in area:
            cond_one = abs(pixel[0]-i) <= 1 and pixel[1] == j
            cond_two = pixel[0] == i and abs(pixel[1]-j) <= 1
            if cond_one or cond_two:
                connected_area.append(area)
                break
    return connected_area


# given the pixel coordinate (i, j) and the area it connects to
# add the pixel into the dictionary

def add_pixel(i, j, connected_area, colour):
    # if it's not connected with any area, add a new area in the dictionary
    if len(connected_area) == 0:
        colour_dict[str(colour)].append([[i, j]])
    # if it's connected with one area, add the coordinate into that area
    elif len(connected_area) == 1:
        connected_area[0].append([i, j])
    # if it's connected with more than one area, it means some areas are merged by it
    # hence combine all these areas
    else:
        new_area = [[i, j]]
        for area in connected_area:
            new_area += area
        for area in connected_area:
            colour_dict[str(colour)].remove(area)
        colour_dict[str(colour)].append(new_area)


# main program

def count_area(file_name, height, width):
    graph = []
    with open(file_name, "rb") as f:
        for i in range(height):
            row = []
            for j in range(width):
                byte = f.read(1)
                row.append(int.from_bytes(byte, byteorder='big'))
            graph.append(row)

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            colour = graph[i][j]
            if check_exist(graph[i][j]):
                connected_area = check_connection(i, j, colour)
                add_pixel(i, j, connected_area, colour)
            else:
                colour_dict[str(colour)] = [[[i, j]]]
    # create an array with length 256 and all elements set to 0
    output_arr = []
    for i in range(256):
        output_arr.append(0)
    # for colours with areas in the graph, assign the number of areas
    for key in colour_dict:
        output_arr[int(key)] = int(len(colour_dict[key]))
    for n in output_arr:
        print(n)


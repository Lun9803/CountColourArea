"""
This is an API for count area application
"""
colour_dict = {};



# checks if the colour value exists in graph previously
def check_exist(colour):
    if colour_dict.has_key(str(colour)):
        return True;
    else:
        return False;

# checks if a pixel is connected with other patterns with same colour
def check_connection():



# main program
def count_area(graph):
    for i in graph:
        for j in graph[i]:
            if check_exist(graph[i][j]):

            else:
                colour_dict[str(graph[i][j])]=[i, j];
# Na podstawie dwóch par punktów wyzaczyć wzór prostej a potem sprawdzić czy proste są prostopadłe, równoległe

# input:
# [((0,0),(1,1)),((0,1)(1,2))]

# output:
# linie są równoległe
# linie nie są prostopadłe

# input:
# [((0,0),(1,1)),((0,10),(1,10))]
# output:
# linie nie są równoległe
# linie nie są prostopadłe

# Warunki prostopadłości i równoległości lini
# # ax+b
# # równoległe
# # a1=a2
# # prostopadłe
# # a1*a2=-1

# nierowne [((0,0)(1,1)),((0,-1)(-1,2))]
# rownolegle [((0,0)(-1,2)),((0,0)(-1,2))]
# prostopadle [((0,1)(2,2)),((3,5)(5,1))]

import re

correct_point_coordinates_definition = "\([-\d]+,[-\d]+\)"

def print_task_and_return_reply():
    print("Enter 4 pairs of co-ordinates points in format:\n-[((X,Y)(X,Y)),((X,Y)(X,Y))]- ")
    user_input = input()
    return user_input

def input_checker(user_input, correct_point_coordinates):
    is_correct_user_input = re.match(f"\[\({correct_point_coordinates}{correct_point_coordinates}\),\({correct_point_coordinates}{correct_point_coordinates}\)\]", user_input)
    if(is_correct_user_input):
        return True
    else:
        return False

def get_parameters_from_input(user_input):
    parameters_list = [int(number) for number in re.findall(r"[-\d]+", user_input)]
    return parameters_list

def count_lines_a_coefficients(parameters_list):
    # rownanie prostej y = ax + b
    # wzor na wspolczynnik a: a = (yB - yA)/(xB - xA)
    # ((xA,yA)(xB,yB)),((xC,yC)(xD,yD))
    coefficient_a_straight_1 = (parameters_list[3] - parameters_list[1])/(parameters_list[2] - parameters_list[0])
    coefficient_a_straight_2 = (parameters_list[7] - parameters_list[5])/(parameters_list[6] - parameters_list[4])
    a_coefficients = (coefficient_a_straight_1, coefficient_a_straight_2)
    return a_coefficients

def print_straight_relations(a_coefficients):
    if(a_coefficients[0] == a_coefficients[1]):
        return print("linie sa rownolegle\nlinie nie sa prostopadle")
    elif(a_coefficients[0] * a_coefficients[1] == -1):
        return print("linie nie sa rownolegle\nlinie sa prostopadle")
    else:
        return print("linie nie sa rownolegle\nlinie nie sa prostopadle")

user_input_to_functions = print_task_and_return_reply()

if(input_checker(user_input_to_functions, correct_point_coordinates_definition)):
    list_of_coordinates = get_parameters_from_input(user_input_to_functions)
    a_coefficients_touple = count_lines_a_coefficients(list_of_coordinates)
    print_straight_relations(a_coefficients_touple)
else:
    print("invalid input")

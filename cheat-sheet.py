#!/usr/bin/env python3
""" Python cheat sheet """

import sys

def __h1(title):
    print("\n##### %s #####" % title)

def __h2(func):
    title = func.__name__.replace("_", " ")
    title = title[0].capitalize() + title[1:]
    print("--- %s ---" % title)
    func()
    print("")


__h1("BASE") ###################################################################

@__h2
def conditionnals():
    print("if 5 < 6:\n\tprint(\"5 < 6\")\n-->")
    if 5 < 6:
        print("5 < 6")

    print("\nif 5 > 6:\n\tprint(\"5 > 6\")\nelif 5 < 6:\n\tprint(\"5 < 6\")\n"
          "else:\n\tprint(\"5 = 6\")\n-->")
    if 5 > 6:
        print("5 > 6")
    elif 5 < 6:
        print("5 < 6")
    else:
        print("5 = 6")

@__h2
def loops():
    i = 0
    str_list = ""
    while i < 10:
        str_list += str(i) + ", "
        i = i + 1
    print("While loop:", str_list.rstrip(", "))

    str_list = ""
    for i in range(10):
        str_list += str(i) + ", "
    print("For loop:", str_list.rstrip(", "))

    str_list = [str(i) + ", " for i in range(3, 10)]
    print("From list comprehension:", "".join(str_list).rstrip(", "))

__h1("BASE TYPES") #############################################################

@__h2
def strings():
    string = "hElLo woRld"
    print(string.lower())
    print(string.upper())
    print("find E:", string.find("E"))
    print("find last l:", string.rfind("l"))


__h1("COLLECTIONS") ############################################################

@__h2
def dictionnaries():
    empty_dict = {}
    print("empty dictionnary:", empty_dict)
    some_dict = {"key" : "value", "key2" : "value2"}
    print("initialized dictionnary:", some_dict)
    print("keys:")
    print(some_dict.keys())    # has specific type 'dict_keys'
    print("value of key: " + some_dict.get("key", "not found"))
    print("unexisting key: " + some_dict.get("unexisting", "not found"))

@__h2 # C/C++ struct equivalency
def named_tuples():
    from collections import namedtuple
    Point = namedtuple("Point", "x y")
    point = Point(1, 2)
    print("Point:", point, ", point.x:", point.x, ", point.y:", point.y)

@__h2
def tables():
    empty_table = []
    empty_table.append("value")
    empty_table.append("value2")
    some_table = [2, 5, 6]
    print(empty_table)
    print(some_table)


__h1("C-C++ EQUIVALENCIES") ####################################################

@__h2
def ternary():
    result = 1 if 2 == 3 else 2
    print("ternary: ", result)

@__h2
def variadics_arguments():
    def print_error(*args):
        print(args, file=sys.stderr)

    print_error("This is an error message", 3)



katz_deli = []

def line(deli_line:list):
    line_num = len(deli_line)
    if line_num == 0:
        print(f"The line is currently empty.")
    else:
        i = 1
        line_order = ''
        for person in deli_line:
            line_order += f" {i}. {person}"
            i += 1
        print(f"The line is currently:{line_order}")

def take_a_number(deli_line:list, name:str):
    deli_line.append(name)
    print(f"Welcome, {name}. You are number {len(deli_line)} in line.")

def now_serving(deli_line:list):
    if len(deli_line) > 0:
        print(f"Currently serving {deli_line[0]}.")
        deli_line.pop(0)
    else:
        print("There is nobody waiting to be served!")


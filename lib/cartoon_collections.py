def roll_call_dwarves(list):
    for index in range(len(list)):
        print(f"{index + 1}. {list[index]}")

def summon_captain_planet(list):
    return [(element[0].upper() + element[1:] + "!") for element in list]

def long_planeteer_calls(list):
    for call in list:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(list):
    cheeses = ["cheddar", "gouda", "camembert"]
    for element in list:
        if element in cheeses:
            return element
    return None

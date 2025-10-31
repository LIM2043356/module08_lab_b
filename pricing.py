"""
 This program tests the pricing of each of the offered services
 """

def clean_floor(area):
    
    if not isinstance(area, (int, float)) or area <= 0:
        return -1
    if area <= 500:
        return 200
    extra_sqft = area - 500
    extra_units = int((extra_sqft + 249) // 250)  
    return 200 + 100 * extra_units


def inspect_roof(material):
    
    if not isinstance(material, str):
        return -1
    m = material.strip().lower()
    if m == "tile":
        return 500
    if m == "shingle":
        return 600
    return -1


def install_appliances(number_appliance, haul_old_appliance=False):
    
    if not isinstance(number_appliance, int) or number_appliance <= 0:
        return -1
    haul = bool(haul_old_appliance)  
    return number_appliance * 100 + (500 if haul else 0)


def yard_cleanup(front_area, back_area):
    
    if (not isinstance(front_area, (int, float)) or
        not isinstance(back_area, (int, float)) or
        front_area < 0 or back_area < 0):
        return -1

    front_cost = 100 if front_area <= 500 else 150
    back_cost  = 125 if back_area <= 400 else 175
    return front_cost + back_cost


def clean_garage(garage_width):
    
    if not isinstance(garage_width, int):
        return -1
    return {1: 200, 2: 300, 3: 375}.get(garage_width, -1)
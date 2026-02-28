import math

def calculate_slab(data):

    # Concrete volume
    volume = data.length * data.breadth * data.thickness

    # Steel calculation (two-way slab)
    bars_x = math.ceil(data.breadth / data.steel_spacing) + 1
    bars_y = math.ceil(data.length / data.steel_spacing) + 1

    total_length = (bars_x * data.length) + (bars_y * data.breadth)
    steel_weight = (data.steel_diameter ** 2 / 162) * total_length

    # Cost calculations
    concrete_amount = volume * data.rcc_rate
    steel_amount = steel_weight * data.steel_rate

    total_cost = concrete_amount + steel_amount

    return {
        "volume": volume,
        "steel_weight": steel_weight,
        "concrete_amount": concrete_amount,
        "steel_amount": steel_amount,
        "total_cost": total_cost
    }



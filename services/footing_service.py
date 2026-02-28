import math

def calculate_footing(data):

    length = data.length
    breadth = data.breadth

    # Quantity Calculations
    excavation = (length + 0.6) * (breadth + 0.6) * data.excavation_depth
    pcc = length * breadth * data.pcc_thickness
    rcc = length * breadth * data.footing_depth

    # Steel Calculation
    bars_x = math.ceil(breadth / data.steel_spacing) + 1
    bars_y = math.ceil(length / data.steel_spacing) + 1

    total_length = (bars_x * length) + (bars_y * breadth)
    steel_weight = (data.steel_diameter ** 2 / 162) * total_length

    # Cost Calculations
    excavation_amount = excavation * data.excavation_rate
    pcc_amount = pcc * data.pcc_rate
    rcc_amount = rcc * data.rcc_rate
    steel_amount = steel_weight * data.steel_rate

    total_cost = (
        excavation_amount +
        pcc_amount +
        rcc_amount +
        steel_amount
    )

    return {
        "excavation": excavation,
        "pcc": pcc,
        "rcc": rcc,
        "steel": steel_weight,
        "excavation_amount": excavation_amount,
        "pcc_amount": pcc_amount,
        "rcc_amount": rcc_amount,
        "steel_amount": steel_amount,
        "total_cost": total_cost
    }

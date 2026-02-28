from services.footing_service import calculate_footing
from services.slab_service import calculate_slab


def generate_project_boq(data):

    footing_data = data.footing
    slab_data = data.slab


    footing_result = calculate_footing(footing_data)
    slab_result = calculate_slab(slab_data)

    boq = [

        {
            "item_no": 1,
            "description": "Excavation for Footing",
            "unit": "m3",
            "quantity": round(footing_result["excavation"], 2),
            "rate": footing_data.excavation_rate,
            "amount": round(footing_result["excavation_amount"], 2)
        },

        {
            "item_no": 2,
            "description": "PCC below Footing",
            "unit": "m3",
            "quantity": round(footing_result["pcc"], 2),
            "rate": footing_data.pcc_rate,
            "amount": round(footing_result["pcc_amount"], 2)
        },

        {
            "item_no": 3,
            "description": "RCC Footing",
            "unit": "m3",
            "quantity": round(footing_result["rcc"], 2),
            "rate": footing_data.rcc_rate,
            "amount": round(footing_result["rcc_amount"], 2)
        },

        {
            "item_no": 4,
            "description": "Footing Reinforcement Steel",
            "unit": "kg",
            "quantity": round(footing_result["steel"], 2),
            "rate": footing_data.steel_rate,
            "amount": round(footing_result["steel_amount"], 2)
        },

        {
            "item_no": 5,
            "description": "RCC Slab Concrete",
            "unit": "m3",
            "quantity": round(slab_result["volume"], 2),
            "rate": slab_data.rcc_rate,
            "amount": round(slab_result["concrete_amount"], 2)
        },

        {
            "item_no": 6,
            "description": "Slab Reinforcement Steel",
            "unit": "kg",
            "quantity": round(slab_result["steel_weight"], 2),
            "rate": slab_data.steel_rate,
            "amount": round(slab_result["steel_amount"], 2)
        }

    ]

    grand_total = footing_result["total_cost"] + slab_result["total_cost"]

    return {
        "boq": boq,
        "grand_total": round(grand_total, 2)
    }

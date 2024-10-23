descriptions = {
    "DEPT": "Depth",
    "AC": "Sonic Transit Time",
    "CALI": "Caliper",
    "DEN": "Bulk Density",
    "GR": "Gamma Ray",
    "NEU": "Neutron Porosity",
    "RDEP": "Deep Resistivity",
    "RMED": "Medium Resistivity",
    "FREQ": "Frequency",
}

def map_code_to_description(code: str) -> str:
    return descriptions[code]
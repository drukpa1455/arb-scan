import pandas as pd
from typing import Dict

def calculate_ratios(data_dict: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    ratios_dict = {}

    for company, data in data_dict.items():
        ratios_dict[company] = data[f'Ratio_{company}']

    return ratios_dict

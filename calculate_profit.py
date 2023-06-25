import pandas as pd
from typing import Dict, List, Tuple

def calculate_profit(ratios_dict: Dict[str, pd.Series], fx_rate: float) -> Dict[str, List[Tuple[int, int, float]]]:
    """
    Calculates profit opportunities based on the ratios.

    Parameters:
    - ratios_dict (dict): A dictionary containing the ratios for each company.
    - fx_rate (float): The exchange rate.

    Returns:
    - profit_dict (dict): A dictionary containing the profit opportunities for each combination of companies.
    """
    profit_dict = {}

    companies = list(ratios_dict.keys())
    for i in range(len(companies)):
        for j in range(i + 1, len(companies)):
            buy_ratios = ratios_dict[companies[i]]
            sell_ratios = ratios_dict[companies[j]]
            profit_opportunities = []

            for buy_index, buy_ratio in buy_ratios.iteritems():
                for sell_index, sell_ratio in sell_ratios.iteritems():
                    if sell_index > buy_index:
                        profit = (sell_ratio / buy_ratio) * fx_rate
                        profit_opportunities.append((buy_index, sell_index, profit))

            profit_dict[f"{companies[i]}-{companies[j]}"] = profit_opportunities

    return profit_dict

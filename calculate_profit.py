import itertools
from typing import Dict, List, Tuple
import pandas as pd

def calculate_profit(ratios_dict: Dict[str, pd.Series], fx_rate: float) -> Dict[str, List[Tuple[int, int, float]]]:
    profit_dict = {}

    for combination in generate_power_set(list(ratios_dict.keys())):
        buy_index, sell_index, profit = find_optimal_trade(ratios_dict, combination)
        profit_dict[combination] = [(buy_index, sell_index, profit)]

    return profit_dict

def generate_power_set(input_set: List[str]) -> List[Tuple[str]]:
    power_set = []
    for r in range(1, len(input_set) + 1):
        power_set.extend(itertools.combinations(input_set, r))
    return power_set

def find_optimal_trade(ratios_dict: Dict[str, pd.Series], combination: Tuple[str]) -> Tuple[int, int, float]:
    buy_index = -1
    sell_index = -1
    max_profit = 0.0

    for i, ratio in enumerate(ratios_dict[combination[0]]):
        for j in range(i + 1, len(ratios_dict[combination[0]])):
            if ratios_dict[combination[0]][j] > ratio:
                if (ratios_dict[combination[1]][j] / ratios_dict[combination[1]][i]) * ratio > max_profit:
                    buy_index = i
                    sell_index = j
                    max_profit = (ratios_dict[combination[1]][j] / ratios_dict[combination[1]][i]) * ratio

    return buy_index, sell_index, max_profit

from typing import List, TypedDict


class AutoTakeProfitData(TypedDict):
    activated: bool
    number_of_orders: int
    scale_from: float
    scale_to: float

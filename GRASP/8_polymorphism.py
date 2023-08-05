from typing import Callable
from pprint import pprint as pp


ConversionFunc = Callable[[float], None]

def convert(input_val: float, converter: ConversionFunc) -> None:
    converter(input_val)

def in_cm(input_val: float) -> None:
    pp(input_val * 2.54)

def miles_km(input_val: float) -> None:
    pp(input_val * 1.609)

convert(323.34, miles_km)
# miles_km is a callable function



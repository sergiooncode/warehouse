from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    availability_in_units: int

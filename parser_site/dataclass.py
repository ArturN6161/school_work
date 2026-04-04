from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: str
    link: str
    sku: str
    full_path: str
    path: str

from dataclasses import dataclass
import datetime

@dataclass(frozen=True)
class User:
    name: str
    phone_number: int
    password: str

@dataclass(frozen=True)
class Transaction:
    amount: float
    date: datetime
    category: int 

@dataclass(frozen=True)
class Category:
    name: str

@dataclass(frozen=True)
class Transaction_Details:
    amount: float
    date: datetime
    description: str
    category_id: int
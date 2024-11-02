from dataclasses import dataclass

@dataclass
class TenderDTO:
    tenderId: str
    title: str
    description: str
    amount: float
    status: str

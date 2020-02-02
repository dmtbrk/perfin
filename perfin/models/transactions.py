from perfin.models.base import BaseModel


class Transaction(BaseModel):
    def __init__(self, amount: int):
        self.amount: int = amount

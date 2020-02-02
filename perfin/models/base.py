class BaseModel:
    def __repr__(self):
        return f'{self.__class__.__name__}({" ".join([f"{prop}={val}" for prop, val in self.__dict__.items()])})'

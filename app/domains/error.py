import dataclasses

@dataclasses.dataclass
class Error:
    message: str
    data: dict

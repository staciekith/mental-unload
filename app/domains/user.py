import dataclasses

@dataclasses.dataclass
class User:
    id: str
    email: str
    name: str

from dataclasses import dataclass
@dataclass(frozen=True)
class Dutes():
    id: int
    name: str
    description: str
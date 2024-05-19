from dataclasses import dataclass
@dataclass(frozen=True)
class Seekers():
    user_id: int
    vac_id: int
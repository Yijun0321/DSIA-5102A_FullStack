from pydantic import BaseModel


class Pokemon(BaseModel):
    Types: str
    Abilities: str
    Tier: str
    HP: int
    Defense: int
    Special_Attack: int
    Special_Defense: int
    Speed: int
    Next_Evolution: int
    Moves: int
    
    class Config:
        orm_mode = True

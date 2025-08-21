from pydantic import BaseModel

class Role(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }

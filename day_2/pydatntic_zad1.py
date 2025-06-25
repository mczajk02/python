from pydantic import BaseModel
from typing import List, Dict
# uv pip install pydantic

class Payload(BaseModel):
    names: List[str]
    options: Dict[str, int]

data ={
    "names" : ["Ala", "Ola", "Kalafiora"],
    "options" : {"limit":10, "offset": 5}
}

payload = Payload(**data)
print(payload)
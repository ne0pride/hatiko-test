from pydantic import BaseModel

class IMEICheckRequest(BaseModel):
    imei: str
    token: str

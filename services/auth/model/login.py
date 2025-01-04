from pydantic import BaseModel, Field, ConfigDict


class Login(BaseModel):
    model_config = ConfigDict(populate_by_name=True,extra="forbid")
    email :str
    password : str




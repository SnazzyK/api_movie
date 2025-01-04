from configparser import ConfigParser
from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class RegisterRequests(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    email :str
    full_name : str = Field(alias = "fullName")
    password : str
    password_repeat : str = Field(alias = "passwordRepeat")

class RegisterResponse(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True)

    id: UUID
    email: str
    full_name: str = Field(alias="fullName")
    roles: List[str]
    verified: bool
    created_at: datetime = Field(alias="createdAt")
    banned: bool


class LoginResponse(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True)

    user: RegisterResponse
    access_token: str = Field(alias="accessToken")
    expires_in: int = Field(alias="expiresIn")

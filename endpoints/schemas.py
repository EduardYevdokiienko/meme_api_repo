from pydantic import BaseModel


class ResponseSchema(BaseModel):
    id: int
    info: object
    tags: list
    text: str
    updated_by: str
    url: str


class TokenGetResponse(BaseModel):
    token: str
    user: str


class ResponseSchemaFull(BaseModel):
    data: list[ResponseSchema]

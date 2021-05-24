import re
from datetime import datetime
from utils import token_generator
from pydantic import BaseModel, validator

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    api_key: str = token_generator()
    create_at: datetime = datetime.now()

    class Config:
        validate_assignment = True

    @validator("name")
    def name_validation(self, value: str) -> str:
        numbers_list = list(range(10))
        if any(map(lambda x: x in value, numbers_list)):
            raise ValueError("ФИО не может содержать цифр")
        return value

    @validator("email")
    def email_validation(self, value: str) -> str:
        regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(regex, value):
            return value
        raise ValueError("Некорректный e-mail")
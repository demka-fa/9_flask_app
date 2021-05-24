import json
from typing import Tuple, Union

from models import User, AuthUser


class Storage:
    """Класс для работы с коллекцией пользователей"""

    def __init__(self, file_path: str = "./data/db.json") -> None:
        self.file_path = file_path
        self.data = []
        self.read_collection()

    def read_collection(self) -> None:
        """Чтение данных с файла в self.data"""
        with open(self.file_path, "r") as stream:
            buf = stream.read()
        buf = [] if buf is None else json.loads(buf)
        self.data = [User.parse_raw(item) for item in buf]

    def write_collection(self) -> None:
        """Запись данных с self.data в файл"""
        buf = json.dumps(self.data)
        with open(self.file_path, "w") as stream:
            stream.write(buf)

    def user_auth(self, check_user: AuthUser) -> Tuple[bool, Union[User, None]]:
        """Метод для авторизации пользователя в системе"""
        for user in self.data:
            if user.email == check_user.email and user.password == check_user.password:
                return True, user
        return False, None

    def user_reg(self, user: User) -> None:
        """Метод регистрации пользователей"""
        self.data.append(user)
        self.write_collection()

    def clear(self) -> None:
        """Отчищает файл авторизации от всех записей"""
        self.data = []
        self.write_collection()

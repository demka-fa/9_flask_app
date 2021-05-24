from flask import Flask, request
from pydantic import ValidationError

from storage import Storage
from models import User, AuthUser

app = Flask(__name__)
data_storage = Storage()


@app.route("/users/auth", methods=["GET"])
def user_authorization():
    auth_user = AuthUser.parse_raw(request.json)
    # TODO проврека на авторизацию
    pass


@app.route("/users/reg", methods=["POST"])
def user_registration():
    """Управляющая логика обработки входящего запроса на Flask"""

    try:
        new_user = User.parse_raw(request.json)
    except ValidationError as e:
        return e.json()

    print(new_user)
    return new_user.json()


if __name__ == "__main__":
    app.run(debug=False, port=80)

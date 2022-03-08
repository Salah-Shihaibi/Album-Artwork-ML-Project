class CustomError(Exception):
    def __init__(self):
        self.msg = "Internal server error."
        self.status_code = 500

    def response(self):
        return {"msg": self.msg, "status_code": self.status_code}, self.status_code


class PasswordTooShortError(CustomError):
    def __init__(self):
        self.msg = "Password should be 5 characters or longer."
        self.status_code = 400


class UsernameTakenError(CustomError):
    def __init__(self):
        self.msg = "Username is already in use."
        self.status_code = 400


class EmailTakenError(CustomError):
    def __init__(self):
        self.msg = "Email address is already in use."
        self.status_code = 400


class EmailInvalidError(CustomError):
    def __init__(self):
        self.msg = "Email address invalid."
        self.status_code = 400


class NoUserFoundError(CustomError):
    def __init__(self):
        self.msg = "User/password combination is not valid."
        self.status_code = 400


class IncorrectPasswordError(CustomError):
    def __init__(self):
        self.msg = "User/password combination is not valid."
        self.status_code = 400


class IncorrectRequestBodyError(CustomError):
    def __init__(self):
        self.msg = "Credentials invalid format."
        self.status_code = 400


class SQLErrorHandler(CustomError):
    def __init__(self, error_code):
        self.status_code = 400
        if error_code == "42883":
            self.msg = "Database ERROR: Invalid input."
        if error_code == "23502":
            self.msg = "Database ERROR: Data not provided."

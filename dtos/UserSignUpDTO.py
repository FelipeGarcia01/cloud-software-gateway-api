class UserSignUpDTO:
    def __init__(self, username, password1, password2, email):
        self.user = username
        self.password1 = password1
        self.password2 = password2
        self.email = email

    @staticmethod
    def from_json(json_dct):
        return UserSignUpDTO(json_dct['username'],
                             json_dct['password1'],
                             json_dct['password2'],
                             json_dct['email'])


class UserLogInDTO:
    def __init__(self, username, password):
        self.user = username
        self.password = password

    @staticmethod
    def from_json(json_dct):
        return UserLogInDTO(json_dct['username'],
                            json_dct['password'])

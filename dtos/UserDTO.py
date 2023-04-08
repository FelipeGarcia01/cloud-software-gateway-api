class UserDTO:
    def __init__(self, username, password):
        self.user = username
        self.password = password

    @staticmethod
    def from_json(json_dct):
        return UserDTO(json_dct['user'],
                       json_dct['pass'])

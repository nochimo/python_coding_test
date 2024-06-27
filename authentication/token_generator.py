import aux.config


class tokenGenerator:
    @staticmethod
    def get_token(user, password):
        if user == 'potato' and password == 'tomato':
            return aux.config.authConfig.token

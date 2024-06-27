from faker import Faker

import aux.config


class FakeDatabaseConnection:
    def __init__(self, token, num_rows):
        self.token = token
        self.fake = Faker()
        self.num_rows = num_rows

    def authenticate(self):
        # Simulate token authentication
        if self.token == aux.config.authConfig.token:
            return True
        else:
            raise ValueError("Invalid token")

    def fetch_from_database(self):
        raise NotImplementedError("Subclasses should implement this method")

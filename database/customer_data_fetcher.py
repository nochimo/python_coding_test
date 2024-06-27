from database.fake_database_connection import FakeDatabaseConnection
import random


class CustomerDataFetcher(FakeDatabaseConnection):
    def __init__(self, token, num_rows=100):
        super().__init__(token, num_rows)

    def fetch_from_database(self):
        self.authenticate()
        customers = []
        # Calculate the number of null entries (10%)
        null_entries_count = max(1, int(self.num_rows * 0.10))
        for _ in range(self.num_rows):
            if null_entries_count > 0 and random.random() < 0.10:
                customer_id = None
                customer_name = None
                customer_email = None
            else:
                customer_id = self.fake.uuid4()
                customer_name = self.fake.uuid4()
                customer_email = self.fake.email()

            customer = {
                'customer_id': customer_id,
                'customer_name': customer_name,
                'customer_email': customer_email
            }
            customers.append(customer)
        return customers

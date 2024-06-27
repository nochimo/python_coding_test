from database.fake_database_connection import FakeDatabaseConnection
import random


class OrderDataFetcher(FakeDatabaseConnection):
    def __init__(self, token, num_rows=1000):
        super().__init__(token, num_rows)

    def fetch_from_database(self):
        self.authenticate()
        orders = []
        # Calculate the number of null entries (10% of num_orders)
        null_entries_count = max(1, int(self.num_rows * 0.10))

        for _ in range(self.num_rows):
            if null_entries_count > 0 and random.random() < 0.10:
                order_id = None
                customer_id = None
                null_entries_count -= 1
            else:
                order_id = self.fake.uuid4()
                customer_id = self.fake.uuid4()

            order = {
                'order_id': order_id,
                'customer_id': customer_id,
                'order_date': self.fake.date_this_year(),
                'order_amount': round(random.uniform(20.0, 500.0), 2)
            }
            orders.append(order)

        return orders

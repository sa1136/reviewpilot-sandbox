from app.models import Order


class OrderRepository:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, order: Order) -> Order:
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO orders (customer_id, customer_email, currency, total_cents)"
                " VALUES (%s, %s, %s, %s) RETURNING id",
                (order.customer_id, order.customer_email, order.currency, order.total_cents),
            )
            order.id = cur.fetchone()[0]
        self.conn.commit()
        return order

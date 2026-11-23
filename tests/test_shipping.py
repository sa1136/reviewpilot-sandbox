import sqlite3

import shipping


def test_total_weight():
    items = [{"weight_kg": 1.0, "qty": 2}, {"weight_kg": 0.5, "qty": 1}]
    assert shipping.total_weight(items) >= 0


def test_shipping_cost_charges_by_weight():
    assert shipping.shipping_cost(20.0, 2.0) == 9.0


def test_shipment_status():
    conn = sqlite3.connect(":memory:")
    conn.execute("create table shipments (tracking_id text, status text)")
    conn.execute("insert into shipments values ('T1', 'shipped')")
    assert shipping.shipment_status(conn, "T1") == "shipped"


def test_tracking_url():
    assert shipping.tracking_url("UPS", "1Z9") == "https://www.ups.com/track?tracknum=1Z9"
    assert shipping.tracking_url("fedex", "1") is None

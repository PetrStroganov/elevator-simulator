from types import SimpleNamespace
from simulation import activate_requests


def test_passenger_appears_at_arrival_time():
    passenger = SimpleNamespace(arrival_time=10, status="pending")

    activate_requests([passenger], current_time=10)

    assert passenger.status == "waiting"


def test_passenger_does_not_appear_early():
    passenger = SimpleNamespace(arrival_time=10, status="pending")

    activate_requests([passenger], current_time=9)

    assert passenger.status == "pending"


def test_riding_passenger_keeps_status():
    passenger = SimpleNamespace(arrival_time=5, status="riding")

    activate_requests([passenger], current_time=10)

    assert passenger.status == "riding"
from models import Passenger, Passenger_Status
from simulation import activate_requests


def test_passenger_appears_at_arrival_time():
    passenger = Passenger("Иван", 1, 5, 10)

    activate_requests([passenger], current_time=10)

    assert passenger.status == Passenger_Status.WAITING


def test_passenger_does_not_appear_early():
    passenger = Passenger("Иван", 1, 5, 15)

    activate_requests([passenger], current_time=10)

    assert passenger.status == Passenger_Status.PENDING


def test_going_passenger_keeps_status():
    passenger = Passenger("Иван", 1, 5, 10)
    passenger.status = Passenger_Status.GOING

    activate_requests([passenger], current_time=15)

    assert passenger.status == Passenger_Status.GOING

def test_passenger_waiting_after_arrival_time():
    passenger = Passenger("Иван", 1, 5, 10)

    activate_requests([passenger], current_time=15)

    assert passenger.status == Passenger_Status.WAITING
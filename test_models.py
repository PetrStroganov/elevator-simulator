from models import Passenger, Elevator, Passenger_Status, Direction, Elevator_Status, Elevator_type
import pytest


def test_negative_capacity():
    with pytest.raises(ValueError):
        Elevator(1, 1, Elevator_type.BASIC, 0, 1, "defoult")



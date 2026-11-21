#from models import Passenger, Elevator, Passenger_Status, Direction, Elevator_Status, Elevator_type
#import pytest
#
#
#def test_negative_capacity():
#    with pytest.raises(ValueError):
#        Elevator(1, 1, Elevator_type.BASIC, -1, 1, "defoult")
#
#
#def test_negative_speed():
#    with pytest.raises(ValueError):
#        Elevator(1, -1, Elevator_type.BASIC, 5, 1, "defoult")
#
#
#def test_elevator_data():
#    lift = Elevator(1, 1, Elevator_type.BASIC, 5, 1, "defoult")
#    assert lift.id == 1
#    assert lift.speed == 1
#    assert lift.type == Elevator_type.BASIC
#    assert lift.capacity == 5
#    assert lift.position == 1
#    assert lift.algorithm == "defoult"
#    assert lift.status == Elevator_Status.STOP
#    assert lift.direction == Direction.STAND
#    assert lift.next_direction == Direction.STAND
#    assert len(lift.passengers) == 0
#
#
#def test_passenger_data():
#    nikita = Passenger("Nikita", 1, 42, 4)
#    assert nikita.name == "Nikita"
#    assert nikita.start_floor == 1
#    assert nikita.end_floor == 42
#    assert nikita.appear_time == 4
#    assert nikita.status == Passenger_Status.WAITING


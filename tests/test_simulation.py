from models import Elevator, Elevator_type, Passenger, Passenger_Status
from simulation import activate_requests, assign_requests, process_stop


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


def test_boarding_removes_reservation():
    elevator = Elevator(
        id=1,
        speed=1,
        type=Elevator_type.BASIC,
        capacity=2,
        position=1,
        algorithm="fifo",
    )
    first = Passenger("Иван", 1, 5, 0)
    second = Passenger("Олег", 1, 6, 0)

    activate_requests([first, second], current_time=0)

    assign_requests([first], [elevator])
    process_stop(elevator)

    assert elevator.passengers == [first]
    assert elevator.assigned_requests == []
    assert first.status == Passenger_Status.GOING

    assign_requests([second], [elevator])

    assert second.assigned_elevator_id == elevator.id
    assert elevator.assigned_requests == [second]


def test_elevator_boards_multiple_passengers():
    elevator = Elevator(
        id=1,
        speed=1,
        type=Elevator_type.BASIC,
        capacity=2,
        position=1,
        algorithm="fifo",
    )
    passengers = [
        Passenger("Иван", 1, 5, 0),
        Passenger("Олег", 1, 6, 0),
        Passenger("Антон", 1, 7, 0),
    ]

    activate_requests(passengers, current_time=0)
    assign_requests(passengers, [elevator])
    process_stop(elevator)

    assert elevator.passengers == passengers[:2]
    assert elevator.assigned_requests == []
    assert passengers[0].status == Passenger_Status.GOING
    assert passengers[1].status == Passenger_Status.GOING
    assert passengers[2].status == Passenger_Status.WAITING
    assert passengers[2].assigned_elevator_id is None


def test_repeated_assignment_does_not_duplicate_requests():
    elevator = Elevator(
        id=1,
        speed=1,
        type=Elevator_type.BASIC,
        capacity=3,
        position=1,
        algorithm="fifo",
    )
    passenger = Passenger("Иван", 1, 5, 0)
    activate_requests([passenger], current_time=0)

    assign_requests([passenger], [elevator])
    assign_requests([passenger], [elevator])

    assert elevator.assigned_requests == [passenger]
    assert passenger.assigned_elevator_id == elevator.id

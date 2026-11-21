from models import Passenger, Elevator, Passenger_Status, Direction, Elevator_Status, Elevator_type


def step_in_1_second(elevator):
    if not elevator.passengers:
        elevator.status = Elevator_Status.STOP
        elevator.direction = Direction.STAND
        return False
    if elevator.next_direction == Direction.UP:
        next_stop = 10000000000000000000
        for i in elevator.passengers:
            next_stop = min(next_stop, i.end_floor)
    elif elevator.next_direction == Direction.DOWN:
        next_stop = 0
        for i in elevator.passengers:
            next_stop = max(next_stop, i.end_floor)
    else:
        return False
    difference = next_stop - elevator.position
    if abs(difference) <= elevator.speed:
        elevator.position = next_stop
        elevator.status = Elevator_Status.STOP
        elevator.direction = Direction.STAND
        return True

    elevator.status = Elevator_Status.MOVE
    if difference > 0:
        elevator.direction = Direction.UP
        elevator.position += elevator.speed
    else:
        elevator.direction = Direction.DOWN
        elevator.position -= elevator.speed
    return False



from dataclasses import dataclass, field
from enum import Enum


class Passenger_Status(Enum):  # (1)
    WAITING = 'Ждёт'
    GOING = 'Едет'
    ARRIVED = 'Приехал'
    PENDING = 'Ждет время своего появления'


class Elevator_type(Enum):  # (2)
    BASIC = "Обычный"
    STRONG = "Грузовой"


class Elevator_Status(Enum):  # (3)
    STOP = "На месте"
    MOVE = "В движении"


class Direction(Enum):  # (4)
    UP = 1
    DOWN = -1
    STAND = 0


@dataclass
class Passenger:  # Модель пассажира
    name: str
    start_floor: int
    end_floor: int
    appear_time: float
    status: Passenger_Status = Passenger_Status.PENDING

    def __post_init__(self):
        if self.start_floor == self.end_floor:
            raise ValueError("Этаж отправления и назначения совпадают")

    @property
    def direction(self):
        if self.end_floor > self.start_floor:
            return Direction.UP
        return Direction.DOWN


@dataclass
class Elevator:
    id: int
    speed: float
    type: Elevator_type  # (2)
    capacity: int
    position: float
    algorithm: str
    status: Elevator_Status = Elevator_Status.STOP  # (3)
    direction: Direction = Direction.STAND  # (4)
    next_direction: Direction = Direction.STAND
    passengers: list = field(default_factory=list)

    def __post_init__(self):
        if self.speed <= 0 or self.capacity <= 0:
            raise ValueError("Скорость и вместимость должны превышать 0")

    def has_space(self):
        return self.capacity > len(self.passengers)

    def board(self, passenger):
        if self.status != Elevator_Status.STOP:
            return False
        if self.position != passenger.start_floor:
            return False
        if passenger.status != Passenger_Status.WAITING:
            return False
        if not self.has_space():
            return False
        if self.next_direction == Direction.STAND:
            self.next_direction = passenger.direction
        elif self.next_direction != passenger.direction:
            return False
        self.passengers.append(passenger)
        passenger.status = Passenger_Status.GOING
        return True

    def go_out(self, floor):
        if self.status != Elevator_Status.STOP:
            return []
        not_leave = []
        leave = []
        for i in self.passengers:
            if i.end_floor == floor:
                i.status = Passenger_Status.ARRIVED
                leave.append(i)
            else:
                not_leave.append(i)
        self.passengers = not_leave
        if not self.passengers:
            self.next_direction = Direction.STAND
        return leave



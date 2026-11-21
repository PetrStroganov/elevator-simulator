from models import Elevator_Status, Passenger_Status, Direction


def activate_requests(passengers, current_time):
    """Переводит появившихся пассажиров в состояние ожидания.

    Args:
        passengers: Список объектов Passenger, изменяемых функцией.
        current_time: Текущее модельное время в секундах.

    Returns:
        None.
    """
    for passenger in passengers:
        if (
            passenger.status == Passenger_Status.PENDING
            and passenger.appear_time <= current_time
        ):
            passenger.status = Passenger_Status.WAITING


def assign_requests(passengers, elevators):
    """Назначает ожидающих пассажиров подходящим лифтам.

    Под каждую назначенную заявку резервируется одно место.
    Лифт с заявками или пассажирами получает дополнительные вызовы
    только в том же направлении и впереди своего текущего положения.

    Args:
        passengers: Список объектов Passenger.
        elevators: Список объектов Elevator с уникальными id.

    Returns:
        None. Назначения записываются в объекты пассажиров и лифтов.
    """
    for passenger in sorted(passengers, key=lambda p: p.appear_time):
        if passenger.status != Passenger_Status.WAITING:
            continue

        if passenger.assigned_elevator_id is not None:
            continue

        suitable_elevators = []

        for elevator in elevators:
            reserved_places = (
                len(elevator.passengers)
                + len(elevator.assigned_requests)
            )

            if reserved_places >= elevator.capacity:
                continue

            route_direction = elevator.next_direction

            if (
                route_direction == Direction.STAND
                and elevator.assigned_requests
            ):
                route_direction = elevator.assigned_requests[0].direction

            if route_direction != Direction.STAND:
                if passenger.direction != route_direction:
                    continue

                distance_to_pickup = (
                    passenger.start_floor - elevator.position
                )

                if distance_to_pickup * route_direction.value < 0:
                    continue

            suitable_elevators.append(elevator)

        if not suitable_elevators:
            continue

        selected_elevator = min(
            suitable_elevators,
            key=lambda e: (
                abs(e.position - passenger.start_floor),
                e.id,
            ),
        )

        selected_elevator.assigned_requests.append(passenger)
        passenger.assigned_elevator_id = selected_elevator.id

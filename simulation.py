from models import Passenger_Status


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

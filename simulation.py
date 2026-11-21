from models import Passenger_Status


def activate_requests(passengers, current_time):
    for passenger in passengers:
        if (
                passenger.status == Passenger_Status.PENDING
                and passenger.appear_time <= current_time
        ):
            passenger.status = Passenger_Status.WAITING

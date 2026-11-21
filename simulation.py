def activate_requests(passengers, current_time):
    for passenger in passengers:
        if (
            passenger.status == "pending"
            and passenger.arrival_time <= current_time
        ):
            passenger.status = "waiting"

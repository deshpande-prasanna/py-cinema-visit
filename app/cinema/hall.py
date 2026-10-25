from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, *args: int, **kwargs: int) -> None:
        if kwargs:
            hall_number, *_ = kwargs.values()
        else:
            hall_number, *_ = args
        self.number = hall_number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            if isinstance(customer, dict):
                my_customer = Customer(name=customer.get("name"),
                                       food=customer.get("food"))
            else:
                my_customer = Customer(name=customer.name, food=customer.food)
            my_customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)

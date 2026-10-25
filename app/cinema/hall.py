from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            if isinstance(customer, dict):
                (Customer(name=customer.get("name"),
                         food=customer.get("food"))
                 .watch_movie(movie_name))
            else:
                (Customer(name=customer.name, food=customer.food)
                 .watch_movie(movie_name))

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)

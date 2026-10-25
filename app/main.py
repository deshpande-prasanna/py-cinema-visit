from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    my_cinema_hall = CinemaHall(hall_number)
    my_cleaner = Cleaner(cleaner)

    for customer in customers:
        my_customer = Customer(name=customer.get("name"),
                               food=customer.get("food"))
        CinemaBar.sell_product(my_customer, my_customer.food)

    my_cinema_hall.movie_session(movie, customers, my_cleaner)

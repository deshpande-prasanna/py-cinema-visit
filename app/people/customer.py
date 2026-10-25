class Customer:
    def __init__(self, *args, **kwargs: str) -> None:
        if kwargs:
            self.name = kwargs.get("name")
            self.food = kwargs.get("food")
        else:
            self.name = args[0]
            self.food = args[1]

    def watch_movie(self, movie: str) -> None:
        self.movie = movie
        print(f'{self.name} is watching "{self.movie}".')

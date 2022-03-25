class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []
    
    def add_favourite(self, favourite_film):
        self.favourites.append(favourite_film)
    
    def remove_favourite(self, film_to_remove):
        self.favourites.remove(film_to_remove)
    
    def get_favourites(self):
        return self.favourites
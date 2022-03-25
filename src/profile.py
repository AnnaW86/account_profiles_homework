class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []
    
    def add_favourite(self, favourite_movie):
        self.favourites.append(favourite_movie)
    
    def remove_favourite(self, movie_to_remove):
        self.favourites.remove(movie_to_remove)
    
    def get_favourites(self):
        return self.favourites
class Account:
    def __init__(self, first_name, second_name, email_address):
        self.first_name = first_name
        self.second_name = second_name
        self.email_address = email_address
        self.profiles = []
        self.archived_profiles = []

    def add_profile(self, new_profile):
        self.profiles.append(new_profile)
    
    def remove_profile(self, old_profile):
        self.archived_profiles.append(old_profile)
        self.profiles.remove(old_profile)
    
    def list_profiles(self):
        return self.profiles
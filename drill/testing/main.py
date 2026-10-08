import requests

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self,username, email):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = email
        return True

    def get_user(self, username):
        return self.users.get(username)

    
def get_weather(city):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}")
    if response.status_code == 200:
        return response.json()  
    else:
        raise ValueError("Could not retrieve weather data") 




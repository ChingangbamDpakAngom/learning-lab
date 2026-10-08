from main import UserManager, get_weather
import pytest

@pytest.fixture
def user_manager():
    "create a fresh instance of Usermanager before each test"
    return UserManager()

# user_manager = UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("johndoe", "john@example.com") == True
    assert user_manager.get_user("johndoe") == "john@example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("johndoe", "john@example.com")
    with pytest.raises(ValueError, match="Username already exists"):
        user_manager.add_user("johndoe", "jane@example.com")


def test_get_weather(mocker):
    #mock reqests.get to return a mock response
    mock_get = mocker.patch("main.requests.get")

    # set return value of the mock response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"location": {"name": "London"}, "current": {"temp_c": 15}}

    #call function
    result = get_weather("London")

    # assertions
    assert result["location"]["name"] == "London"
    mock_get.assert_called_once_with("https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London")


def test_get_weather_error(mocker):
    # the unhappy path: the API answers with an error status
    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.status_code = 404

    with pytest.raises(ValueError, match="Could not retrieve weather data"):
        get_weather("Nowhere")
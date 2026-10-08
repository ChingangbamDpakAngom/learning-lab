import pytest
from db import Database

@pytest.fixture
def db():
    database = Database()  # create a fresh instance of Database before each test
    yield database  # provide the fixture value to the test functions
    database.data.clear()  # clean up after the test

def test_add_user(db):
    db.add_user("user1", "Alice")
    assert db.get_user("user1") == "Alice"

def test_add_duplicate_user(db):
    db.add_user("user1", "Alice")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user("user1", "Bob")

def test_delete_user(db):
    db.add_user("user1", "Alice")
    db.delete_user("user1")
    assert db.get_user("user1") is None


from db import save_user

def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user("Alice", 30)

    # must match db.py exactly: same filename, same SQL text (spaces included)
    mock_conn.assert_called_once_with("User.db")
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, age) VALUES (?,?)", ("Alice", 30)
    )
    mock_conn.return_value.commit.assert_called_once()   # the insert was saved
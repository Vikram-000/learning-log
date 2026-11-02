from testing_pytest.user import UserManager
import pytest

@pytest.fixture
def Usermanager():
    print("Creating usermanager")
    return UserManager()

@pytest.fixture
def user_data():
    user = {
        "name" : "Vikram",
        "email" : "vikram@gmail.com",
        "age" : 21
    }

    return user

@pytest.fixture
def registered_user(user_data, Usermanager):
    u = Usermanager
    u.add_user(**user_data)

    return u 

def test_get_user(registered_user, user_data):
    assert registered_user.get_user("vikram@gmail.com") == user_data

def test_count_users(registered_user):
    assert registered_user.count_users() == 1

def test_delete_user(registered_user, user_data):
    assert registered_user.delete_user(user_data["email"]) == True  # Can also just type email instead of user_data["email"] (Did this for fun)
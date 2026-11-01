from testing_pytest.user import UserManager
import pytest

@pytest.fixture
def temp():
    u = UserManager()
    user = {
                "name": "Vikram",
                "email": "vikram@gmail.com",
                "age": 100
    }
    return u, user

def test_add_user(temp):
    u, user = temp
    with pytest.raises(ValueError, match="Name cannot be empty"):
        assert u.add_user("", user["email"], user["age"])

    with pytest.raises(ValueError, match="Invalid email"):
        assert u.add_user(user["name"], "vikramgmail.com", user["age"])

    with pytest.raises(ValueError, match="User must be at least 18"):
        assert u.add_user(**{**user, "age": 17}) 

def test_get_user(temp):
    u, user = temp
    u.add_user(**user)
    assert u.get_user("vikram@gmail.com") == user

def test_get_all_users(temp):
    u, user = temp
    u.add_user(**user)
    assert u.get_all_users() == [user]

def test_count_users(temp):
    u, user = temp
    u.add_user(**user)
    assert u.count_users() == 1

def test_delete_user(temp):
    u, user = temp
    u.add_user(**user)
    assert u.delete_user("vikram@gmail.com") == True
    
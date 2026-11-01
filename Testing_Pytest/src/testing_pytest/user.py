
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email, age):
        if not name:
            raise ValueError("Name cannot be empty")

        if "@" not in email:
            raise ValueError("Invalid email")

        if age < 18:
            raise ValueError("User must be at least 18")

        user = {
            "name": name,
            "email": email,
            "age": age
        }

        self.users.append(user)
        return user

    def get_user(self, email):
        for user in self.users:
            if user["email"] == email:
                return user

        return None

    def delete_user(self, email):
        user = self.get_user(email)

        if user:
            self.users.remove(user)
            return True

        return False

    def get_all_users(self):
        return self.users

    def count_users(self):
        return len(self.users)

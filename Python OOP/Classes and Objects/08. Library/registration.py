from project.user import User
from project.library import Library


class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)


    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return f"We could not find such user to remove!"
        library.user_records.remove(user)


    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user = next(filter(lambda x: x.user_id == user_id, library.user_records))
            if user.username == new_username:
                return f"Please check again the provided username - it should be different than the username used so far!"
            user.username = new_username

            try:
                if user.username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books[user.username]
            except StopIteration:
                return
            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        except StopIteration:
            return f"There is no user with id = {user_id}!"










# pyutils/collections.py


class UserGroup:
    """
    Custom iterable collection for users.
    """

    def __init__(self, users=None):

        self.users = users or []

    def __iter__(self):

        return iter(self.users)

    def __len__(self):

        return len(self.users)

    def add(self, user):

        self.users.append(user)
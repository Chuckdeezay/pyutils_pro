# pyutils/models.py


# =========================================================
# BASE MODEL
# =========================================================

class BaseModel:
    """
    Base class for all domain models.
    """

    def __repr__(self):

        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):

        return self.__repr__()


# =========================================================
# USER MODEL
# =========================================================

class User(BaseModel):
    """
    Represents a system user.
    """

    def __init__(self, user_id: int, name: str, email: str):

        self.user_id = user_id
        self.name = name
        self.email = email

    # -----------------------------------------------------
    # COMPARISON METHODS
    # -----------------------------------------------------

    def __eq__(self, other):

        return self.user_id == other.user_id

    def __lt__(self, other):

        return self.user_id < other.user_id

    # -----------------------------------------------------
    # DICT-LIKE BEHAVIOR
    # -----------------------------------------------------

    def __getitem__(self, key):

        return getattr(self, key)

    def __setitem__(self, key, value):

        setattr(self, key, value)

    def __contains__(self, item):

        return item in self.__dict__


# =========================================================
# CALLABLE OBJECT
# =========================================================

class UserFormatter:
    """
    Callable formatter object.
    """

    def __call__(self, user):

        return f"{user.user_id} | {user.name} | {user.email}"


# =========================================================
# PROPERTY EXAMPLE
# =========================================================

class Account:
    """
    Demonstrates property-based validation.
    """

    def __init__(self, owner: str, balance: float):

        self.owner = owner
        self._balance = balance

    @property
    def balance(self):

        return self._balance

    @balance.setter
    def balance(self, value):

        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value


# =========================================================
# CUSTOM DESCRIPTOR
# =========================================================

class PositiveNumber:
    """
    Descriptor enforcing positive numbers.
    """

    def __set_name__(self, owner, name):

        self.name = name

    def __get__(self, instance, owner):

        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):

        if value < 0:
            raise ValueError(f"{self.name} cannot be negative")

        instance.__dict__[self.name] = value


# =========================================================
# PRODUCT MODEL USING DESCRIPTORS
# =========================================================

class Product(BaseModel):
    """
    Product model using descriptors.
    """

    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(
        self,
        name: str,
        price: float,
        quantity: int
    ):

        self.name = name
        self.price = price
        self.quantity = quantity
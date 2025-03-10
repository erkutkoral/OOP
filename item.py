import csv

class Item:
  # The pay rate after %20 discount
  pay_rate = 0.8
  all = []

  def __init__(self, name: str, price: float, quantity = 0):
    # Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than or equal to 0!"
    assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0!"

    # Also added here "__" before name attribute as part of property decorator
    self.__name = name
    self.__price = price
    self.quantity = quantity

    # Actions to execute
    Item.all.append(self)

  @property
  def price(self):
    return self.__price

  def apply_discount(self):
    self.__price = self.__price * self.pay_rate

  def apply_increment(self, increment_value):
    self.__price = self.__price + self.__price * increment_value


  @property
  # Property Decorator = Read-Only Attribute
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  def calculate_total_price(self):
    return self.price * self.quantity

  # Creating a class method
  @classmethod
  def instantiate_from_csv(cls):
    with open('items.csv', 'r') as f:
      reader = csv.DictReader(f)
      items = list(reader)

    for item in items:
      Item(
          name = item.get("name"),
          price = float(item.get("price")),
          quantity = int(item.get("quantity"))
      )

  # Creating a static method
  @staticmethod
  def is_integer(num):
    # We will count out the floats that are point zero
    # For i.e: 5.0, 10.0
    if isinstance(num, float):
      # Count out the floats that are point zero
      return num.is_integer()

    elif isinstance(num, int):
      return True

    else:
      return False

  # Using __repr__() magic method to adjust print statement
  def __repr__(self):
    return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
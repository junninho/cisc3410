from Bag import Bag # import Bag

class Bagger:
  def __init__(self, items):
    self.items = items
    self.bags = []

  # check order adds a soft drink if potato chips is in card and milk if oreo cookies is in card
  def check_order(self):
    for item in self.items:
      if item["name"] == "potato chips":
        add_suggestion = input("Would you like to add a soft drink to your order? ").lower()
        if add_suggestion == "y":
          self.items.append({"name": "soft drink", "container_type": "plastic bottle", "size": "large", "frozen": False})
      elif item["name"] == "oreo cookies":
        add_suggestion = input("Would you like to add a milk to your order? ").lower()
        if add_suggestion == "y":
          self.items.append({"name": "milk", "container_type": "plastic bottle", "size": "large", "frozen": False})

  # get bag at index
  def get_bag(self, index):
    if index < len(self.bags):
      bag = self.bags[index]
    else:
      bag = Bag()
      self.bags.append(bag)

    return bag

  # sort items and bag according to bagging_order
  def bag_items(self):
    small = []
    medium = []
    medium_frozen = []
    large = []
    large_bottles = []

    bagging_order = [large_bottles, large, medium_frozen, medium, small]

    self.check_order()
    
    for item in self.items:
      if item["size"] == "small":
        small.append(item)
      elif item["size"] == "medium":
        if item["frozen"]:
          medium_frozen.append(item)
        else:
          medium.append(item)
      elif item["size"] == "large":
        if item["container_type"] == "plastic bottle":
          large_bottles.append(item)
        else:
          large.append(item)

    for group in bagging_order:
      index = 0
      bag = self.get_bag(index)

      for item in group:
        while not bag.add_item(item):
          index += 1
          bag = self.get_bag(index)

  # stringify bagger output
  def __str__(self):
    output_string = ""
    for bag in self.bags:
      output_string = output_string + "Bag" + str(self.bags.index(bag) + 1) + ":\n" + str(bag) + "\n"

    return output_string
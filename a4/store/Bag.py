class Bag:
  # initiate local variables establishing assumptions where bag can hold a maximum of 8 and each size has an associated number 
  def __init__(self):
    self.items = []
    self.space_remaining = 8
    self.size_values = {"small": 1, "medium": 2, "large": 3}

  # adds item to bag if space remaining
  def add_item(self, item):
    if self.space_remaining >= self.size_values[item["size"]]:
      self.items.append(item)
      self.space_remaining -= self.size_values[item["size"]]
      return True
    return False

  # stringify bag output
  def __str__(self):
    output_string = ""

    for item in self.items:
      output_string = output_string + item["name"] + "\n" 

    return output_string
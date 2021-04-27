from Bagger import Bagger # import Bagger

# 3 test cases classified as customer(x)
customer1 = [
        {"name": "bread", "container_type": "plastic bag", "size": "medium", "frozen": False},
        {"name": "glop", "container_type": "jar", "size": "small", "frozen": False},
        {"name": "granola", "container_type": "cardboard box", "size": "large", "frozen": False},
        {"name": "ice cream", "container_type": "cardboard carton", "size": "medium", "frozen": True},
        {"name": "potato chips", "container_type": "plastic bag", "size": "medium", "frozen": False}
]

customer2 = [
        {"name": "waffles", "container_type": "carboard box", "size": "large", "frozen": False},
        {"name": "mac and cheese", "container_type": "cardboard box", "size": "medium", "frozen": False},
        {"name": "orange juice", "container_type": "plastic bottle", "size": "large", "frozen": False},
        {"name": "ice cream", "container_type": "cardboard carton", "size": "medium", "frozen": True},
        {"name": "oreo cookies", "container_type": "plastic bag", "size": "medium", "frozen": False},
        {"name": "bread", "container_type": "plastic bag", "size": "medium", "frozen": False},
        {"name": "granola", "container_type": "cardboard box", "size": "large", "frozen": False},
        {"name": "potato chips", "container_type": "plastic bag", "size": "medium", "frozen": False}
]

customer3 = [
        {"name": "waffles", "container_type": "carboard box", "size": "large", "frozen": False},
        {"name": "granola", "container_type": "cardboard box", "size": "large", "frozen": False},
        {"name": "orange juice", "container_type": "plastic bottle", "size": "large", "frozen": False},
]

# driving agent
def agent(customer):
    bagger = Bagger(customer) # create new bagger
    bagger.bag_items() # bag items
    print(bagger) # print bagger output

# use agent to process each "customer"
agent(customer1)
agent(customer2)
agent(customer3)
from items import *
from map import rooms
inventory = [item_id, item_laptop, item_money]

current_room = rooms["Reception"]

current_weight = 0
for i in inventory:
    current_weight += i["weight"]

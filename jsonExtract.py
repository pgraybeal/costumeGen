#! python3
# import json files for items and dl the pertinent info

import json
slotJsons = {'2h': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-2h.json',
             'ammo': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-ammo.json',
             'body': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-body.json',
             'cape': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-cape.json',
             'feet': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-feet.json',
             'hands': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-hands.json',
             'head': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-head.json',
             'legs': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-legs.json',
             'neck': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-neck.json',
             'ring': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-ring.json',
             'shield': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-shield.json',
             'weapon': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-weapon.json'}
items = []
stats = {}
itemSlots = {}

"""equipment": {"attack_stab": 0, "attack_slash": 0, "attack_crush": 0,
              "attack_magic": 0, "attack_ranged": 8, "defence_stab": 0,
              "defence_slash": 0, "defence_crush": 0, "defence_magic": 0,
              "defence_ranged": 0, "melee_strength": 0, "ranged_strength": 0,
              "magic_damage": 0, "prayer": 0, "slot": "2h", "requirements": {"ranged": 1}},
"""


def getSlotType(statsDict):
    for slotType in statsDict:
        for item in statsDict[slotType]:
            itemSlots.setdefault(item, statsDict[slotType][item]['slot'])


def extractStats(jsonDict):
    for slotType, jsonUrl in jsonDict.items():
        try:
            from urllib.request import urlopen
        except ImportError:
            from urllib2 import urlopen
        response = urlopen(jsonUrl)
        rawData = response.read().decode("utf-8")
        data = json.loads(rawData)
        # print(data2h)
        stats.setdefault(slotType, {})

        for k, v in data.items():
            for k1, v1 in v.items():
                if k1 == "name":
                    if v1 not in items:
                        items.append(v1.lower())
                if k1 == "equipment":
                    stats[slotType].setdefault(v["name"].lower(), v1)


def getStats(itemName):
    itemType = itemSlots[itemName.lower()]
    print(stats[itemType][itemName.lower()])


def main():
    extractStats(slotJsons)
    getSlotType(stats)
    getStats('Maple longbow')
    getStats('yew Longbow')


if __name__ == "__main__":
    main()
